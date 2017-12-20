Title: Installing and Running Shiny Server from Source on 32-bit Ubuntu
Date: 2016-03-20 20:00
Authors: Michael Toth
Modified: 2016-03-20 20:00
Category: R
Tags: R, Projects, Shiny
Slug: installing-and-running-shiny-server-from-source-on-32-bit-ubuntu
author_gplusid: 103836786232018210272
Summary: A detailed guide to the exact steps I took to get a shiny server running on my 32-bit cloud-based ubuntu server on Digital Ocean.  

I recently migrated this site from a shared web hosting service to [DigitalOcean](https://m.do.co/c/e38e89eb35d9) because I was interested in learning about how to host my own site and how web servers work. I also wanted to play with and host shiny applications on my own site, rather than relying on a third-party service provider. 

In this post I'll talk about the steps I followed to get my shiny server running on a 32-bit Ubuntu DigitalOcean cloud instance. This article assumes that you have

* A 32-bit Ubuntu OS with space available. For this I was using a DigitalOcean instance, but this should work just as well on a local computer or another provider's service
* A decent understanding of the Linux command line
* (Optional) A running nginx server that is serving your current site (where you want to deploy your shiny apps)  



## Installing Required Dependencies
Before proceeding with the installation, make sure that you have all of the required dependencies installed on your machine. The following software is all needed (sudo apt-get install any of the below that are missing). If you run into any issues below, double check that you've installed the below (with the specified versions) properly

* python 2.6 or 2.7
* cmake >= 2.8.10
* gcc
* g++
* git  



## R Installations
Assuming you don't have R installed, you'll need to do that. We'll need r-base and r-devel both installed for some shiny apps to run properly, so let's do that:

```bash
sudo apt-get update
sudo apt-get install r-base r-base-dev
```

Next we'll install the shiny R package.  While we could start up an R session and simply run install.packages('shiny') from that instance, that would install the shiny package only for one user. Instead, we'll run the command below which will install the shiny package for all users on the machine:

```bash
sudo su - -c "R -e \"install.packages('shiny', repos='http://cran.rstudio.com/')\""
```

When I ran the above command, the packages downloaded but did not install. After some investigation, I realized this was because my instance was running out of memory, so I added some swap space to the instance and ran the command again, which completed successfully. You may or may not have this issue, but if you do, the below command gives you 1GB swap space which should allow your installation to complete.

```bash
sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
sudo /sbin/mkswap /var/swap.1
sudo /sbin/swapon /var/swap.1
```  


## Shiny Server 32-bit Installation from Source
RStudio provides a convenient .deb install with pre-compiled binaries for 64-bit architecture, but if you're running 32-bit architecture you'll need to build shiny server from source as described below. This involves manually compiling the required binary files and making some changes to setup directories and config files. This can be a bit complicated (luckily not *too* complicated), so if you do have 64-bit architecture/OS you can follow the [simpler instructions from RStudio](https://www.rstudio.com/products/shiny/download-server/) to install directly. Otherwise, follow along with my instructions below

cd into the directory where you'd like the shiny-server repository. I'll be installing mine to ~/dev, but any location will work. Note that this location will be temporary, so your decision here is not too important.  

```bash
cd ~/dev

# Clone the repository from GitHub and cd into the new directory
git clone https://github.com/rstudio/shiny-server.git
cd shiny-server

# Add the bin directory to the path so we can reference
DIR=`pwd`
PATH=$DIR/bin:$PATH

PYTHON=`which python`

# If Python version is not 2.6.x or 2.7.x, you'll need to modify to 
# reference one of these versions (e.g. which python26). This may
# or may not require you to install a new Python version.  For more
# details, review the "Python" section of the RStudio documentation: 
# https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source
$PYTHON --version

# Use cmake to prepare the make step. Modify the "--DCMAKE_INSTALL_PREFIX"
# if you wish the install the software at a different location.
mkdir tmp; cd tmp
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DPYTHON="$PYTHON" ../

# Recompile the npm modules included in the project
make
mkdir ../build
(cd .. && ./bin/npm --python="$PYTHON" rebuild)
# Need to rebuild our gyp bindings since 'npm rebuild' won't run gyp for us.
(cd .. && ./bin/node ./ext/node/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js --python="$PYTHON" rebuild)

# Install the software at the predefined location
sudo make install
```  


##Configuration
Now we've successfully installed Shiny Server in the location we defined above. You can now safely delete the shiny-server git repo if you would like. There are a few configuration issues we need to finalize before we can use shiny-server, which we'll cover next.

```bash
# Place a shortcut to the shiny-server executable in /usr/bin. 
# As /usr/bin should already be in your PATH variable, you won't need
# to permanently modify your PATH to reflect the change we made above
sudo ln -s /usr/local/shiny-server/bin/shiny-server /usr/bin/shiny-server

#Create shiny user on your system. On some systems, you may need to specify the full path to 'useradd'
sudo useradd -r -m shiny

# Create log, config, and application directories for shiny
sudo mkdir -p /var/log/shiny-server
sudo mkdir -p /srv/shiny-server
sudo mkdir -p /var/lib/shiny-server
sudo chown shiny /var/log/shiny-server
sudo mkdir -p /etc/shiny-server
```

Shiny server will look for resources in certain file paths. Certain log directories and application directories can be modified in a configuration file stored at /etc/shiny-server/shiny-server.conf. By default, there will be no file at that location. The RStudio instructions claim that the default configuration(link) will be used if no file exists, but that was not the case for me and I received an error message when trying to run. If the same happens for you, simply copy the default configuration into /etc/shiny-server/shiny-server.conf and you should be all set.

Get the RStudio Upstart script which will allow you to run shiny in the background as you would for running your nginx or other server. This will let you run shiny automatically when you boot your system, or to run it continuously on Digital Ocean

```bash
sudo wget https://raw.github.com/rstudio/shiny-server/master/config/upstart/shiny-server.conf\
  -O /etc/init/shiny-server.conf
```

Place any shiny scripts in the /srv/shiny-server/your_app
Write a little bit about how you can now run shiny server to serve sites on http://ip_addr:3838/your_app
Starting and stopping shiny server
```bash
sudo start shiny-server
sudo stop shiny-server
```  

## (Optional) Serving to a custom domain with clean URLs (no :3838 links)
Now we have shiny installed and configured properly. You'll still need to set it up to serve the files to your actual website address however. I updated my nginx configuration (/etc/nginx/sites-enabled/default or /etc/nginx/sites-enabled/<yoursite>) to add a block for shiny. This allows you to host on yoursite/shiny. This is a reverse proxy and allows you to get around porting issues  

```bash
location /shiny/ {
	proxy_pass http://127.0.0.1:3838/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
}
```

I drew heavily on the following sources in navigating this process:  

* [Installation](https://www.rstudio.com/products/shiny/download-server/)  
* [Shiny Administrator's Guide](http://docs.rstudio.com/shiny-server/)  
* [Digital Ocean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-shiny-server-on-ubuntu-14-04)  
* [Building from Source](https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source)  
* [Blog for Digital Ocean Setup](http://deanattali.com/2015/05/09/setup-rstudio-shiny-server-digital-ocean/)  
