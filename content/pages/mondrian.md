Title: Mondrian
Date: 2016-03-14 23:00
Status: hidden

<!DOCTYPE html>

<html>

<head>
	<meta charset="utf-8">
	<title>Michael Toth - Mondrian Painting</title>
</head>

<style>

.palette #red, .palette #blue, .palette #yellow, .palette #white, .palette #black {
    border: solid 2px black;
    height: 50px; width: 50px;
    margin: 5px;
}

.palette #red {
    background-color: red;
}

.palette #blue {
    background-color: #1919FF;
}

.palette #yellow {
    background-color: yellow;
}

.palette #white {
    background-color: white;
}

.palette #black {
    background-color: black;
}

.palette {
    border: solid 2px black;
    border-radius: 10px;
    margin: 0px 100px 50px 0px;
    width: 64px;
    display: inline-block;
    vertical-align: top;
}

.palette .container {
    padding: 0;
    margin: 0;
}

.canvas {
    border: solid 2px black;
    border-radius: 10px;
    padding: 10px;
    display: inline-block;
}

.canvas .container {
    border: solid 3px black;
    padding: 0px;
    margin: 0px;
    width: 524px;
    float: right;
}

#row1box1 {border: solid 3px black; height: 120px; width: 181px; float:left;}
#row1box2 {border: solid 3px black; height: 120px; width: 119px; float:left;}
#row1box3 {border: solid 3px black; height: 120px; width: 75px; float:left;}
#row1box4 {border: solid 3px black; height: 120px; width: 125px; float:left;}
#row2box1 {border: solid 3px black; height: 80px; width: 125px; float:left; clear: both}
#row2box2 {border: solid 3px black; height: 80px; width: 50px; float:left;}
#row2box3 {border: solid 3px black; height: 80px; width: 200px; float:left;}
#row2box4 {border: solid 3px black; height: 80px; width: 125px; float:left;}
#row3box1 {border: solid 3px black; height: 140px; width: 125px; float:left; clear: both}
#row3box2 {border: solid 3px black; height: 140px; width: 50px; float:left;}
#row3box3 {border: solid 3px black; height: 140px; width: 150px; float:left;}
#row3box4 {border: solid 3px black; height: 140px; width: 175px; float:left;}
#row4box1 {border: solid 3px black; height: 30px; width: 100px; float:left; clear: both}
#row4box2 {border: solid 3px black; height: 30px; width: 150px; float:left;}
#row4box3 {border: solid 3px black; height: 30px; width: 175px; float:left;}
#row4box4 {border: solid 3px black; height: 30px; width: 75px; float:left;}
#row5box1 {border: solid 3px black; height: 130px; width: 150px; float:left; clear: both}
#row5box2 {border: solid 3px black; height: 130px; width: 100px; float:left;}
#row5box3 {border: solid 3px black; height: 130px; width: 175px; float:left;}
#row5box4 {border: solid 3px black; height: 130px; width: 75px; float:left;}
</style>

<body>	
<div class="palette">
	<div class="container">
		<div id="red" onclick="selectColor('red')"></div>
		<div id="blue" onclick="selectColor('blue')"></div>
		<div id="yellow" onclick="selectColor('yellow')"></div>
		<div id="white" onclick="selectColor('white')"></div>
		<div id="black" onclick="selectColor('black')"></div>
	</div>
</div>
<div class="canvas">
	<div class="container">
		<div id = "row1box1" onclick="paint(this)"></div>
		<div id = "row1box2" onclick="paint(this)"></div>
		<div id = "row1box3" onclick="paint(this)"></div>
		<div id = "row1box4" onclick="paint(this)"></div>
		<div id = "row2box1" onclick="paint(this)"></div>
		<div id = "row2box2" onclick="paint(this)"></div>
		<div id = "row2box3" onclick="paint(this)"></div>
		<div id = "row2box4" onclick="paint(this)"></div>
		<div id = "row3box1" onclick="paint(this)"></div>
		<div id = "row3box2" onclick="paint(this)"></div>
		<div id = "row3box3" onclick="paint(this)"></div>
		<div id = "row3box4" onclick="paint(this)"></div>
		<div id = "row4box1" onclick="paint(this)"></div>
		<div id = "row4box2" onclick="paint(this)"></div>
		<div id = "row4box3" onclick="paint(this)"></div>
		<div id = "row4box4" onclick="paint(this)"></div>
		<div id = "row5box1" onclick="paint(this)"></div>
		<div id = "row5box2" onclick="paint(this)"></div>
		<div id = "row5box3" onclick="paint(this)"></div>
		<div id = "row5box4" onclick="paint(this)"></div>
	</div>
</div>
<br>
</body>
</html>


<script>
var myColor = 'white';

function selectColor(color) {
	myColor = color;
}

function paint(elem) {
	elem.style.backgroundColor = myColor;
}
</script>
