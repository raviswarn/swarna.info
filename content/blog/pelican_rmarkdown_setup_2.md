---
title: How to Write Pelican Blog Posts using RMarkdown & Knitr, 2.0
author: Michael Toth
date: 2017-06-14
category: R
tags: R, Pelican, Blog
summary: A clean & easy workflow for getting R analyses published as on a Pelican blog
output: html_document
---



[Back in January]({filename}pelican_rmarkdown_setup.md) I wrote a post discussing how to get RMarkdown and Pelican to work together to make the R analysis > blog post workflow a bit easier. While I had high hopes, I was never really happy with the setup I put together then, so I set out to update it. 

In this post I'm going to talk about my new, improved way of publishing Pelican blog posts using RMarkdown. I'm assuming you already have a Pelican blog set up, so I won't be covering that in today's post. If you're interested but haven't yet set up a blog for yourself, it's quite straightforward! I recommend checking out these links:

* [Official Pelican Guide](http://docs.getpelican.com/en/stable/quickstart.html)
* [Detailed Pelican Setup by Duncan Lock](http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/)


### Issue with Old Setup

The setup I recommended in my prior post used a Pelican plugin called rmd_reader to convert .Rmd files to standard .md files that Pelican could read. For taking a static .Rmd post and creating a published post, this worked pretty well. One of my favorite things about my Pelican setup, though, was using the development server feature. Basically, this runs a web server locally, monitoring your content directory for any changes, and automatically regenerates your site whenever it finds a change. This feature did not play nice with the rmd_reader plugin. When you start the development server, rmd_reader starts converting any .rmd files to .md files. This action would trigger the development server to restart, as it identified changes in the content directory, and you'd find yourself stuck in an infinite loop of regeneration. Admittedly, it's a minor issue, and I probably could have hacked together a solution, but I didn't want to make changes to the base Pelican code or the rmd_reader code, because I wanted this to be portable to other systems. So in the end, I decided I needed another solution. 


### New Solution & Setup

The challenge is to find a way to run your .Rmd code, producing any desired figures and code chunks, then store the results in a .md file that is readable by Pelican. I remembered having read about how David Robinson built [his site](http://varianceexplained.org/) using a [custom R script](https://github.com/dgrtwo/dgrtwo.github.com/blob/master/_scripts/knitpages.R) to convert each .Rmd file to a .md file using knitr commands, and I set out to see if I could modify that for my purposes. 

Below is the final knitpages.R file I'm using, having made a few minor changes to David's file, which was optimized for Jekyll blogs:


```r
#!/usr/local/bin/Rscript --vanilla

# compiles all .Rmd files in _R directory into .md files in blog directory,
# if the input file is older than the output file.

# run ./knitpages.R to update all knitr files that need to be updated.
# run this script from your base content directory

library(knitr)

KnitPost <- function(input, outfile, figsfolder, cachefolder, base.url="/") {
  opts_knit$set(base.url = base.url)
  fig.path <- paste0(figsfolder, sub(".Rmd$", "", basename(input)), "/")
  cache.path <- file.path(cachefolder, sub(".Rmd$", "", basename(input)), "/")
  
  opts_chunk$set(fig.path = fig.path)
  opts_chunk$set(cache.path = cache.path)
  opts_chunk$set(fig.cap = "center")
  render_markdown()
  knit(input, outfile, envir = parent.frame())
}

knit_folder <- function(infolder, outfolder, figsfolder, cachefolder, force = F) {
  for (infile in list.files(infolder, pattern = "*.Rmd", full.names = TRUE)) {
    
    print(infile)
    outfile = paste0(outfolder, "/", sub(".Rmd$", ".md", basename(infile)))
    print(outfile)
    
    # knit only if the input file is the last one modified
    if (!file.exists(outfile) | file.info(infile)$mtime > file.info(outfile)$mtime) {
        KnitPost(infile, outfile, figsfolder, cachefolder)
    }
  }
}

knit_folder("_R", "blog", "figures/", "_caches")
```

The only real change to David's script is updating `render_jekyll()` to `render_markdown()`. I also had to change the path to the Rscript executable (first line), which you may need to do based on your OS. Run `which Rscript` from your terminal to find the correct path.

You should modify the knit_folder command at the bottom to reflect your own blog's directory structure. Here's how this script works:

1) The script finds all .Rmd files in your infolder, ignoring old & unchanged files
2) New & updated files are passed to the KnitPost function, which runs the Rmd file, saving any generated images to the figsfolder directory and storing any cached data to the cachefolder. 
3) An output .md file is created in the outfolder directory with links to any figures generated by R

### New Process

Here's my updated process for publishing today:

1) From the content directory of my blog, I run knitpages.R, which will convert any new or updated .Rmd files to Pelican-readable .md files
2) Next I generate my Pelican site
3) When I'm satisfied with the results locally, I can easily push to my web server and `make publish` from there to generate my site

I like this solution because it's a bit cleaner and requires less overhead than the one I wrote about previously. I've noticed that personally one of the biggest issues preventing me from publishing more frequently has been friction in the publishing process. This solution goes a long way toward solving that, and I hope this helps me increase my frequency of publishing. I'd like to extend a big thanks to David for sharing his knitpages.R code and examples on his blog, it made the process of setting this up so much easier!
