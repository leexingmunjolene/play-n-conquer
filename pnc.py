import cgi
import csv
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import google.appengine.ext.db
import random


class MainPage(webapp.RequestHandler):
	''''Home page handler'''
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
                <div class="title" id="fittext">
                    Play 'n' Conquer
                </div>
				<br>
                <div class="h2" id="fittext">
                    Permutations & Combinations
                </div>
				<div class="menu">
				<a rel="external" data-transition="slide" href="/tut0">Tutorial&nbsp;>&nbsp;</a><br><br>
				<a rel="external" data-transition="slide" href="/quiz">Quiz Game&nbsp;>&nbsp;</a><br><br>
				<a rel="external" data-transition="slide" href="/virtualcard">Virtual Card&nbsp;>&nbsp;</a><br><br>
				</div>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>
		''')
		

class Page1(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Zero
                </div>
                <div class="h2" id="fittext">
                    // Addition and Multiplication Principle
                </div>
				<div class="navi">
					<a rel="external" data-transition="slide" href="/tut1">&nbsp;>&nbsp;</a>
					<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Difference between Permutation and Combination</option>
					<option value="/tut2">Permutation</option>
					<option value="/tut3">Combination</option>
					<option value="/tut4">Special Cases</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<p>
				<b>Addition Principle</b>
				<br><br>
				Suppose there are <i>n<sub>1</sub></i> ways for the event <i>E<sub>1</sub></i> to occur, <i>n<sub>2</sub></i> ways for the event <i>E<sub>2</sub></i> to occur, and <i>n<sub>x</sub></i> ways for the event <i>E<sub>x</sub></i> to occur. If all these events are mutually exclusive (i.e. they are independent of each other; the happening of one event does not affect another event), then the number of ways for <i>E<sub>x</sub></i> to occur is <i>n<sub>1</sub></i> + <i>n<sub>2</sub></i> + ... + <i>n<sub>x</sub></i>.
				<br><br>
				+Animation
				<br><br>
				<b>Multiplication principle</b>
				<br><br>
				Suppose that an event <i>E</i> can be split into <i>k</i> sub-events <i>E<sub>1</sub></i>, <i>E<sub>2</sub></i>, <i>E<sub>3</sub></i>, ..., <i>E<sub>x</sub></i> in ordered stages (i.e. the outcome of one event will affect the outcome of the following events). If there are <i>n<sub>1</sub></i> ways for the event <i>E<sub>1</sub></i> to occur, <i>n<sub>2</sub></i> ways for the event <i>E<sub>2</sub></i> to occur, and <i>n<sub>x</sub></i> ways for the event <i>E<sub>x</sub></i> to occur, then the number of ways for event <i>E</i> to occur is <i>n<sub>1</sub></i> x <i>n<sub>2</sub></i> x ... x <i>n<sub>x</sub></i> .
				<br><br>
				+Animation
				</p>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>""")

class Page2(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    One
                </div>
                <div class="h2" id="fittext">
                    // Addition and Multiplication Principle
                </div>
				<div class="navi">
					<a rel="external" data-transition="slide" href="/tut0">&nbsp;<&nbsp;</a>
					&nbsp;
					<a rel="external" data-transition="slide" href="/tut2">&nbsp;>&nbsp;</a>
					<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut3">Permutation</option>
					<option value="/tut4">Combination</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut6">Special Cases</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<p>
				<span name="AP"><b>Addition Principle</b></span>
				<br><br>
				Suppose there are <i>n<sub>1</sub></i> ways for the event <i>E<sub>1</sub></i> to occur, <i>n<sub>2</sub></i> ways for the event <i>E<sub>2</sub></i> to occur, and <i>n<sub>x</sub></i> ways for the event <i>E<sub>x</sub></i> to occur. If all these events are mutually exclusive (i.e. they are independent of each other; the happening of one event does not affect another event), then the number of ways for <i>E<sub>x</sub></i> to occur is <i>n<sub>1</sub></i> + <i>n<sub>2</sub></i> + ... + <i>n<sub>x</sub></i>.
				<br><br>
				<span name="MP"><b>Multiplication principle</b></span>
				<br><br>
				Suppose that an event <i>E</i> can be split into <i>k</i> sub-events <i>E<sub>1</sub></i>, <i>E<sub>2</sub></i>, <i>E<sub>3</sub></i>, ..., <i>E<sub>x</sub></i> in ordered stages (i.e. the outcome of one event will affect the outcome of the following events). If there are <i>n<sub>1</sub></i> ways for the event <i>E<sub>1</sub></i> to occur, <i>n<sub>2</sub></i> ways for the event <i>E<sub>2</sub></i> to occur, and <i>n<sub>x</sub></i> ways for the event <i>E<sub>x</sub></i> to occur, then the number of ways for event <i>E</i> to occur is <i>n<sub>1</sub></i> x <i>n<sub>2</sub></i> x ... x <i>n<sub>x</sub></i> .
				<br><br>
				</p>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page3(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Two
                </div>
                <div class="h2" id="fittext">
                    // Difference between Permutation and Combination
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut1">&nbsp;<&nbsp;</a>
				&nbsp;
				<a rel="external" data-transition="slide" href="/tut3">&nbsp;>&nbsp;</a>
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Permutation</option>
					<option value="/tut3">Combination</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut6">Special Cases</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<p>
				<blockquote>
				A permutation is an ordered arrangement of a number of objects.<br>
				A combination is an unordered selection of a number of objects from a given set.<br>
				</blockquote>
				<br>
				Students <i>A</i>, <i>B</i> and <i>C</i> are representing their school at a seminar. At the seminar, students from the same schools are seated together. Given that there are 3 adjacent seats in a row, how many different ways can the students be arranged to ocuupy the seats?<br><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By listing all possible combinations:<br>
				<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ABC, ACB<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BAC, BCA<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CAB, CBA<br>
				<br>
				There are 6 different ordered arrangements to seat the three students. Each order is called a <b>permutation</b>.<br>
				<br><br><br>
				However, to the usher, it does not matter which order they are seated in so long as the three students sit as one group.<br>
				Hence, <i>A</i>, <i>B</i> and <i>C</i> are treated as one <b>combination</b>.<br>
				</p>
				<br><br><br>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page4(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Three
                </div>
                <div class="h2" id="fittext">
                    // Permutation
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut2">&nbsp;<&nbsp;</a>
				&nbsp;
				<a rel="external" data-transition="slide" href="/tut4">&nbsp;>&nbsp;</a>
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut4">Combination</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut6">Special Cases</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<p>
				From the exmaple in the previous page, there is a faster way to calculate the number of different arrangements three students can seat in a row. Listing all of the permutations can be tedious especially if it involves many objects. Imagine listing all the possible permutaions of 100 objects (quite impossible, don't even try).<br>
				<br>
				<i><sup>See the flash animation below for an illustrated example.</sup></i><br>
				<br>
				+Animation<br>
				<br>
				The first seat may be filled up in <b>3</b> different ways: A, B or C can sit in that sit.<br>
				After the first seat is filled, the second seat can be filled in only <b>2</b> ways as there are only two students left.<br>
				Finally, it leaves <b>1</b> student to fill up the last seat.<br>
				<br>
				The number of ways can be calculated by using the <a href="/tut1">multiplication principle</a>:<br>
				Therefore the number of ways<br>
				= <i>3</i> x <i>2</i> x <i>1</i><br>
				= <i>3!</i><br>
				= <b><i>6</i></b><br>
				</p>
				<blockquote>
				In general, the number of ways to arrange <i>n</i> different objects in a row<br>
				= <i>n!</i><br>
				= <i>n</i> x <i>(n-1)</i> x <i>(n-2)</i> x ... x <i>(n-r)</i> x <i>2 x 1</i>
				</blockquote>
				<p>
				Now that we know how to calculate the number of arrangements of <i>n</i> different objects in a row, how about the arrangement of a subset of different objects in a row?<br>
				<br>
				In order to do this, we can simply think of it has having less seats than students.<br>
				<br>
				<i><sup>See the flash animation below for an illustrated example.</sup></i><br>
				<br>
				+Animation<br>
				</p>
				<blockquote>
				In general, the number of ways to arrange <i>r</i> objects out of <i>n</i> objects in a row<br>
				= <i>n</i> x <i>(n-1)</i> x <i>(n-2)</i> x <i>(n-3)</i> x ... x <i>(n-r-1)</i>
				= <i>n!/(n-r)!</i><br>
				= <i><sup>n</sup>P<sub>r</sub></i>
				</blockquote>
				<p>
				What about calculating the number of arrangements of <i>n</i> different objects in a row, in which it is okay to repeat the object in the arrangement?<br>
				We can simply think of it as having all objects available when choosing for each 'seat'.<br>
				</p>
				<blockquote>
				For <i>n</i> number of different objects and <i>r</i> slots for the objects to be arranged, the number of different arrangements in a row<br>
				= <i>r<sup>n</sup></i><br>
				</blockquote>
				<p>
				When some objects are identical, in which they are not distinguishable, per say the word <i>EVE</i>.
				Suppose we name the two letter <i>E</i>s such that <i>EVE</i> becomes <i>E<sub>1</sub>VE<sub>2</sub></i>, we can disguish between the two <i>E</i>s.<br>
				Then the number of arrangements possible is <i>3!</i>.<br>
				However, the arrangements <i>E<sub>1</sub>VE<sub>2</sub></i> and <i>E<sub>2</sub>VE<sub>1</sub></i> are the same when we remove the numbering.<br>
				Since the duplicate arrangements are due to <i>2!</i> arrangements of the two <i>E</i>s, the number of arrangements<br>
				= <i>3!</i>/<i>2!</i><br>
				= 3<br>
				<p>
				<b>Arrangement with restrictions</b><br>
				<br>
				Sometimes, there are restrictions to be adhered to, such as two specific persons cannot seat next to each other, or that they must sit together.<br>
				For this, we have to deal with the restrictions first.<br>
				<br>
				See the flash example below:<br>
				<br>
				+Animation
				</p>
				<br><br><br>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page5(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Four
                </div>
                <div class="h2" id="fittext">
                    // Combination
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut3">&nbsp;<&nbsp;</a>
				&nbsp;
				<a rel="external" data-transition="slide" href="/tut5">&nbsp;>&nbsp;</a>
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut3">Permutation</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut6">Special Cases</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<p>
				Now that we know how to permutate, let's move on to <b>Combination</b>.<br>
				To re-cap:<br>
				A combination is an unordered selection of a number of objects from a given set. Just like the double cheeseburger set, it doesn't matter if you drink the coke first or eat the cheeseburger first -- it's all the same in your stomach anyway.<br>
				<br>
				<b>Combination of <i>r</i> objects from <i>n</i> different objects</b><br>
				<br>
				Let's say that from a group of 4 students, namely students <i>A</i>, <i>B</i>, <i>C</i>, and <i>D</i>, 3 students have to selected to represent the school at a seminar.<br>
				<br>
				By listing, we have 4 possible groups of 3 student representatives or combinations:<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>ABC</i><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>BCD</i><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>ACD</i><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>ABD</i><br>
				<br>
				+ research on more explanation<br>
				See the flash example below:<br>
				</p>
				<blockquote>
				In general, the number of combinations of <i>r</i> objects from n different objects is <i><sup>n</sup>C<sub>r</sub></i> .<br>
				The number of combinations of <i>(n-r)</i> objects from n different objects (i.e. <i><sup>n</sup>C<sub>(n-r)</sub></i>)also gives the same answer.
				</blockquote>
				<p>
				<b>Combination of at least 1 object from <i>n</i> objects</b><br>
				<br>
				Jolene intends to borrow at least one book from the library for her trip. She saw four interesting books. If she can borrow up to a maximum of 4 books, how many combinations of books can she borrow?<br>
				<br>
				We can approach this problem in two ways.<br>
				<br>
				Method 1: Consider borrowing 1,2,3 or 4 books<br>
				No. of combinations = <i><sup>4</sup>C<sub>1</sub></i> + <i><sup>4</sup>C<sub>2</sub></i> + <i><sup>4</sup>C<sub>3</sub></i> + <i><sup>4</sup>C<sub>4</sub></i><br>
				= 15<br>
				<br>
				Method 2: Consider whether to borrow or not borrow each book<br>
				No. of combinations = (2 x 2 x 2 x 2) - 1(where all books are not selected)<br>
				= 15<br>
				</p>
				<blockquote>
				Number of ways of choosing at least 1 object from <i>n</i> objects<br>
				= <i>2<sup>n</sup></i> - 1<br>
				= <i><sup>n</sup>C<sub>1</sub></i> + <i><sup>n</sup>C<sub>2</sub></i> + <i><sup>n</sup>C<sub>3</sub></i> + ... + <i><sup>n</sup>C<sub>n</sub></i><br>
				</blockquote>
				<p>
				<b>Partition / Grouping</b><br>
				<br>
				How many ways can a group of 6 students be divided into 3 groups<br>
				(i) containing 3, 2 and 1 students respectively?<br>
				(ii) containing 2 students in each group?<br>
				<br>
				For part (i), simply choose the required number of students for each group.<br>
				No. of ways = <i><sup>6</sup>C<sub>3</sub></i> x <i><sup>3</sup>C<sub>2</sub></i> x <i><sup>1</sup>C<sub>1</sub></i><br>
				= 60<br>
				<br>
				For part (ii), the groups are <i>indistinguishable</i>, where pairs are the same even when chosen in a different order.<br>
				Therefore, No. of ways = (<i><sup>6</sup>C<sub>2</sub></i> x <i><sup>4</sup>C<sub>2</sub></i> x <i><sup>2</sup>C<sub>2</sub></i>) / 3!<br>
				= 15<br>
				</p>
				<br><br><br>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page6(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Five
                </div>
                <div class="h2" id="fittext">
                    // Permutation with Combination
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut4">&nbsp;<&nbsp;</a>
				&nbsp;
				<a rel="external" data-transition="slide" href="/tut6">&nbsp;>&nbsp;</a>
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut3">Permutation</option>
					<option value="/tut4">Combination</option>
					<option value="/tut6">Special Cases</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<blockquote>
				In general, a permutation of <i>r</i> objects to be taken from <i>n</i> objects can be done by<br>
				(i) Choosing <i>r</i> objects from <i>n</i> objects, then<br>
				(ii) Arranging <i>r</i> objects in a row
				</blockquote>
				<p>
				Insert Animation here.
				</p>
				<p>
				A librarian has 8 fiction and 3 non-fiction books. She decides to display 4 fiction books and 1 non-fiction book.<br>
				How can the books be arranged if the non-fiction book cannot be placed at either end of the display?<br>
				<br>
				(i) Choose 4 fiction books out of the 8 available<br>
				(ii) Permutate the 4 fiction books<br>
				(iii) Choose 1 non-fiction book<br>
				(iv) There are 3 ways to slot this non-fiction book in<br>
				<br>
				Try it yourself!<br>
				Did you get 15120 as your answer?<br>
				</p>
				<br><br><br>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page7(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Six
                </div>
                <div class="h2" id="fittext">
                    // Special cases
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut5">&nbsp;<&nbsp;</a>
				&nbsp;
				<a rel="external" data-transition="slide" href="/tut7">&nbsp;>&nbsp;</a>
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut3">Permutation</option>
					<option value="/tut4">Combination</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut7">Summary</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<b>Selecting any number from <i>n</i> objects</b><br>
				<p>
				Jia Ying has three $1 coins, one $5 note and four $10 notes.<br>
				How many different amounts of money can she form with these?<br>
				<br>
				$1 --> 4 choices (0,1,2,3)<br>
				$5 --> 2 choices (0,1)<br>
				$10 --> 5 choices (0,1,3,4)<br>
				<br>
				No. of different amounts = (4 x 2 x 5) - 1<br>
				= 39 <br>
				</p>
				<b>Arrangements of objects in a circle</b><br>
				<br>
				<blockquote>
				The number of ways to arrange n different objects in a circle = (n-1)!<br>
				<i>(n-1) x (n-2) x ... x (n-r) x 2 x 1</i>
				</blockquote>
				<p>
				Insert Animation here.
				</p>
				<p>
				How many ways can 3 people be seating at a round table?<br>
				<br>
				No. of ways = (3-1)!<br>
				= 2<br>
				</p>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Page8(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <div data-role="page" id="page">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
                <div class="h1" id="fittext">
                    Seven
                </div>
                <div class="h2" id="fittext">
                    // Summary
                </div>
				<div class="navi">
				<a rel="external" data-transition="slide" href="/tut6">&nbsp;<&nbsp;</a>
				&nbsp;&nbsp;&nbsp;&nbsp;
				<br>
				<div align="right">
					<form name="link" data-mini="true" class="jump">
					<select data-mini="true" name="menu">
					<option selected>Jump to...</option>
					<option value="/tut1">Introduction</option>
					<option value="/tut2">Difference between Permutation and Combination</option>
					<option value="/tut3">Permutation</option>
					<option value="/tut4">Combination</option>
					<option value="/tut5">Permutation with Combination</option>
					<option value="/tut6">Special Cases</option>
					</select>
					<input type="button" data-mini="true" onClick="location=document.link.menu.options[document.link.menu.selectedIndex].value;" value="Go">
					</form>
				</div>
				</div>
				<b>Permutations</b>
				<blockquote>
				Arrange <i>n</i> different objects in a row<br>
				n!
				</blockquote>
				<blockquote>
				Arrange <i>r</i> from <i>n</i> different objects in a row<br>
				<i><sup>n</sup>P<sub>r</sub></i> or <i><sup>n</sup>C<sub>r</sub></i> x r!
				</blockquote>
				<blockquote>
				Arrange any number from <i>n</i> different objects<br>
				<i><sup>n</sup>C<sub>P</sub></i> + <i><sup>n</sup>P<sub>2</sub></i> + ... + <i><sup>n</sup>P<sub>n</sub></i><br>
				</blockquote>
				<blockquote>
				Arrange <i>n</i> objects with similar objects<br>
				n! / (n<sub>1</sub>!n<sub>2</sub>!...n<sub>k</sub>)
				</blockquote>
				<blockquote>
				Arrrange <i>n</i> different objects in a circle<br>
				(n-1)!
				</blockquote>
				<b>Combinations</b>
				<blockquote>
				Select <i>n</i> from <i>n</i> different objects<br>
				<i><sup>n</sup>C<sub>n</sub></i> = 1
				</blockquote>
				<blockquote>
				Select <i>r</i> from <i>n</i> different objects<br>
				<i><sup>n</sup>C<sub>r</sub></i>
				</blockquote>
				<blockquote>
				Select at least 1 object from <i>n</i> different objects<br>
				<i><sup>n</sup>C<sub>1</sub></i> + <i><sup>n</sup>C<sub>2</sub></i> + ... + <i><sup>n</sup>C<sub>n</sub></i><br>
				or<br>
				2<sup>n</sup> - 1
				</blockquote>
				<div class="footer">
				<br>J<sup>3</sup> &copy; 2012<br>
				</div>
            </div>
        </div>
	<script type="text/javascript">
		$("fittext").fitText();
	</script>
    </body>
</html>''')

class Quiz(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <!-- Home -->
        <div data-role="page" id="page1">
            <div data-role="form" style="padding: 15px" class= "container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
			<div class="h1" id="fittext">
                    Quiz
            </div>
				<div class="h2" id="fittext">
                    Game
                </div>
				<div align = center>
				<form method="POST" action="/quizqn" data-ajax="false">
					<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<h2>
								Please choose your question type.
							</h2>
							<input name="permutation" id="radio1" value="qt1" type="radio" />
							<label for="radio1">
								Permutation
							</label>
							<input name="combination" id="radio2" value="qt2" type="radio" />
							<label for="radio2">
								Combination
							</label>
							<input name="pnc" id="radio3" value="qt3" type="radio" />
							<label for="radio3">
								Permutation n Combination
							</label>
							 <input type="submit" data-inline="true" value="Enter Quiz!" />
						</fieldset>
					</form>	
					</div>
                </div>
            </div> 	
            </div>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>''')


class QuizQn(webapp.RequestHandler):
	def post(self):
		questions1=self.request.get('permutation')
		questions2=self.request.get('combination')
		questions3=self.request.get('pnc')
		
		if questions1 == 'qt1':
			try:
				p_questions = open("PERMUTATION.TXT" , "r")
				p_answers = open("PANS.TXT" , "r")

				questions = p_questions.readlines()
				answers = p_answers.readlines()

				#the number of lines in the file
				num_line = 0
				for lines in questions:
						num_line = num_line + 1

				#a list of question numbers
				store_list=[]

				for i in range(0, num_line):
						store_list.append(i)
				print(store_list)

				#get random questions in to qn_nums[]
				qn_nums=[]
				choosen = 0
				while (choosen < 6):
					num = random.randint(0,(len(store_list)-1))
					qn_nums.append(store_list[num])
					print(store_list)
					choosen = choosen + 1
					del store_list[num]
					print(qn_nums)


				qn1 = questions[qn_nums[0]]
				qn2 = questions[qn_nums[1]]
				qn3 = questions[qn_nums[2]]
				qn4 = questions[qn_nums[3]]
				qn5 = questions[qn_nums[4]]

				ans1_line = answers[qn_nums[0]]
				ans2_line = answers[qn_nums[1]]
				ans3_line = answers[qn_nums[2]]
				ans4_line = answers[qn_nums[3]]
				ans5_line = answers[qn_nums[4]]

				ans_choice1=ans1_line.split('*')
				ans_choice3=ans2_line.split('*')
				ans_choice2=ans3_line.split('*')
				ans_choice4=ans4_line.split('*')
				ans_choice5=ans5_line.split('*')
				
				realans1 = ans_choice1[0]
				realans2 = ans_choice2[0]
				realans3 = ans_choice3[0]
				realans4 = ans_choice4[0]
				realans5 = ans_choice5[0]
				
				random.shuffle(ans_choice1)
				random.shuffle(ans_choice2)
				random.shuffle(ans_choice3)
				random.shuffle(ans_choice4)
				random.shuffle(ans_choice5)
					

				
				p_questions.close()
				p_answers.close()


			except IOError:
				print('OH NO, PERMUTATION.TXT or PANS.TXT is misssing:(')
				
					
		if questions2 == 'qt2':
			try:
				c_questions = open("COMBINATION.TXT" , "r")
				c_answers = open("CANS.TXT" , "r")
			
				questions = c_questions.readlines()
				answers = c_answers.readlines()
				
				#the number of lines in the file
				num_line = 0
				for lines in questions:
						num_line = num_line + 1

				#a list of question numbers
				store_list=[]

				for i in range(0, num_line):
						store_list.append(i)
				print(store_list)

				#get random questions in to qn_nums[]
				qn_nums=[]
				choosen = 0
				while (choosen < 6):
					num = random.randint(0,(len(store_list)-1))
					qn_nums.append(store_list[num])
					print(store_list)
					choosen = choosen + 1
					del store_list[num]
					print(qn_nums)


				qn1 = questions[qn_nums[0]]
				qn2 = questions[qn_nums[1]]
				qn3 = questions[qn_nums[2]]
				qn4 = questions[qn_nums[3]]
				qn5 = questions[qn_nums[4]]

				ans1_line = answers[qn_nums[0]]
				ans2_line = answers[qn_nums[1]]
				ans3_line = answers[qn_nums[2]]
				ans4_line = answers[qn_nums[3]]
				ans5_line = answers[qn_nums[4]]

				ans_choice1=ans1_line.split('*')
				ans_choice2=ans2_line.split('*')
				ans_choice3=ans3_line.split('*')
				ans_choice4=ans4_line.split('*')
				ans_choice5=ans5_line.split('*')
				
				realans1 = ans_choice1[0]
				realans2 = ans_choice2[0]
				realans3 = ans_choice3[0]
				realans4 = ans_choice4[0]
				realans5 = ans_choice5[0]
				
				random.shuffle(ans_choice1)
				random.shuffle(ans_choice2)
				random.shuffle(ans_choice3)
				random.shuffle(ans_choice4)
				random.shuffle(ans_choice5)

				c_questions.close()
				c_answers.close()
				
			except IOError:
				print('OH NO, COMBINATION.TXT or CANS.TXT file is misssing:(')
				
		if questions3 == 'qt3':
			try:
				pnc_questions = open("PNC.TXT" , "r")
				pnc_answers = open("PNCANS.TXT" , "r")
				
				questions = pnc_questions.readlines()
				answers = pnc_answers.readlines()

				#the number of lines in the file
				num_line = 0
				for lines in questions:
						num_line = num_line + 1

				#a list of question numbers
				store_list=[]

				for i in range(0, num_line):
						store_list.append(i)
				print(store_list)

				#get random questions in to qn_nums[]
				qn_nums=[]
				choosen = 0
				while (choosen < 6):
					num = random.randint(0,(len(store_list)-1))
					qn_nums.append(store_list[num])
					print(store_list)
					choosen = choosen + 1
					del store_list[num]
					print(qn_nums)


				qn1 = questions[qn_nums[0]]
				qn2 = questions[qn_nums[1]]
				qn3 = questions[qn_nums[2]]
				qn4 = questions[qn_nums[3]]
				qn5 = questions[qn_nums[4]]

				ans1_line = answers[qn_nums[0]]
				ans2_line = answers[qn_nums[1]]
				ans3_line = answers[qn_nums[2]]
				ans4_line = answers[qn_nums[3]]
				ans5_line = answers[qn_nums[4]]

				ans_choice1=ans1_line.split('*')
				ans_choice2=ans2_line.split('*')
				ans_choice3=ans3_line.split('*')
				ans_choice4=ans4_line.split('*')
				ans_choice5=ans5_line.split('*')
				
				realans1 = ans_choice1[0]
				realans2 = ans_choice2[0]
				realans3 = ans_choice3[0]
				realans4 = ans_choice4[0]
				realans5 = ans_choice5[0]
				
				random.shuffle(ans_choice1)
				random.shuffle(ans_choice2)
				random.shuffle(ans_choice3)
				random.shuffle(ans_choice4)
				random.shuffle(ans_choice5)

				pnc_questions.close()
				pnc_answers.close()

			except IOError:
				print('OH NO, PNC.TXT or PNCANS.TXT files are missing:(')
				
				
			
		self.response.out.write('''<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
    </head>
    <body>
        <!-- Home -->
        <div data-role="page" id="page1">
            <div data-role="content" style="padding: 15px" class="container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div>
			<div class="h1" id="fittext">
                    Quiz
            </div>
				<div class="h2" id="fittext">
                    Questions
                </div>
				<div align= center>
				<form method="POST" action="/quizsubmit" data-ajax="false">
					<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<blockquote>
								Qn1. %s
							</blockquote>
							<input name="r1" id="q1a" value="%s" type="radio" />
							<label for="q1a">
								%s
							</label>
							<input name="r1" id="q1b" value="%s" type="radio" />
							<label for="q1b">
								%s
							</label>
							<input name="r1" id="q1c" value="%s" type="radio" />
							<label for="q1c">
								%s
							</label>
							<input name="r1" id="q1d" value="%s" type="radio" />
							<label for="q1d">
								%s
							</label>
						</fieldset>
					</div>'''%(qn1,ans_choice1[0],ans_choice1[0],ans_choice1[1],ans_choice1[1], ans_choice1[2],ans_choice1[2],ans_choice1[3],ans_choice1[3]))
					
		self.response.out.write('''<input type="hidden" name="qn1_realans" value="%s"/>'''%(realans1))
		
		self.response.out.write('''<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<blockquote>
								Qn2. %s
							</blockquote>
							<input name="r2" id="q2a" value="%s" type="radio" />
							<label for="q2a">
								%s
							</label>
							<input name="r2" id="q2b" value="%s" type="radio" />
							<label for="q2b">
								%s
							</label>
							<input name="r2" id="q2c" value="%s" type="radio" />
							<label for="q2c">
								%s
							</label>
							<input name="r2" id="q2d" value="%s" type="radio" />
							<label for="q2d">
								%s
							</label>
						</fieldset>
					</div>'''%(qn2,ans_choice2[0],ans_choice2[0],ans_choice2[1],ans_choice2[1],ans_choice2[2],ans_choice2[2],ans_choice2[3],ans_choice2[3]))
					
		self.response.out.write('''<input type="hidden" name="qn2_realans" value="%s"/>'''%(realans2))
		
		self.response.out.write('''<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<blockquote>
								Qn3. %s
							</blockquote>
							<input name="r3" id="q3a" value="%s" type="radio" />
							<label for="q3a">
								%s
							</label>
							<input name="r3" id="q3b" value="%s" type="radio" />
							<label for="q3b">
								%s
							</label>
							<input name="r3" id="q3c" value="%s" type="radio" />
							<label for="q3c">
								%s
							</label>
							<input name="r3" id="q3d" value="%s" type="radio" />
							<label for="q3d">
								%s
							</label>
						</fieldset>
					</div>'''%(qn3,ans_choice3[0],ans_choice3[0],ans_choice3[1],ans_choice3[1],ans_choice3[2],ans_choice3[2],ans_choice3[3],ans_choice3[3]))
			
		self.response.out.write('''<input type="hidden" name="qn3_realans" value="%s"/>'''%(realans3))
			
		self.response.out.write('''<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<blockquote>
								Qn4. %s
							</blockquote>
							<input name="r4" id="q4a" value="%s" type="radio" />
							<label for="q4a">
								%s
							</label>
							<input name="r4" id="q4b" value="%s" type="radio" />
							<label for="q4b">
								%s
							</label>
							<input name="r4" id="q4c" value="%s" type="radio" />
							<label for="q4c">
								%s
							</label>
							<input name="r4" id="q4d" value="%s" type="radio" />
							<label for="q4d">
								%s
							</label>
						</fieldset>
					</div>'''%(qn4,ans_choice4[0],ans_choice4[0],ans_choice4[1],ans_choice4[1],ans_choice4[2],ans_choice4[2],ans_choice4[3],ans_choice4[3]))
					
		self.response.out.write('''<input type="hidden" name="qn4_realans" value="%s"/>'''%(realans4))
		self.response.out.write('''<div data-role="fieldcontain">
						<fieldset data-role="controlgroup" data-type="vertical">
							<blockquote>
								Qn5. %s
							</blockquote>
							<input name="r5" id="q5a" value="%s" type="radio" />
							<label for="q5a">
								%s
							</label>
							<input name="r5" id="q5b" value="%s" type="radio" />
							<label for="q5b">
								%s
							</label>
							<input name="r5" id="q5c" value="%s" type="radio" />
							<label for="q5c">
								%s
							</label>
							<input name="r5" id="q5d" value="%s" type="radio" />
							<label for="q5d">
								%s
							</label>
						</fieldset>
					</div>'''%(qn5,ans_choice5[0],ans_choice5[0],ans_choice5[1],ans_choice5[1],ans_choice5[2],ans_choice5[2],ans_choice5[3],ans_choice5[3]))
					
		self.response.out.write('''<input type="hidden" name="qn5_realans" value="%s"/>'''%(realans5))
		self.response.out.write('''<input type="submit" data-inline="true" value="Submit" />
				</form>	
				</div>
			</div>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>
''')

		
class QuizSubmit(webapp.RequestHandler):
	def post(self):
		choosen_ans1=self.request.get('r1')
		choosen_ans2=self.request.get('r2')
		choosen_ans3=self.request.get('r3')
		choosen_ans4=self.request.get('r4')
		choosen_ans5=self.request.get('r5')
		
		final_ans1=self.request.get('qn1_realans')
		final_ans2=self.request.get('qn2_realans')
		final_ans3=self.request.get('qn3_realans')
		final_ans4=self.request.get('qn4_realans')
		final_ans5=self.request.get('qn5_realans')
		
		num_correct_ans=0
		if choosen_ans1==final_ans1:
			num_correct_ans=num_correct_ans+1
		if choosen_ans2==final_ans2:
			num_correct_ans=num_correct_ans+1
		if choosen_ans3==final_ans3:
			num_correct_ans=num_correct_ans+1
		if choosen_ans4==final_ans4:
			num_correct_ans=num_correct_ans+1
		if choosen_ans5==final_ans5:
			num_correct_ans=num_correct_ans+1
			
		self.response.out.write('''<!DOCTYPE html>
<html>
    <head>
          <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
        </script>
    </head>
    <body>
        <!-- Home -->
        <div data-role="page" id="page1">
            <div data-role="content" style="padding: 15px">
			<div data-role="form" style="padding: 15px" class= "container">
			<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div><span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
			<div class="h1" id="fittext">
                    Quiz
            </div>
				<div class="h2" id="fittext">
                    Score
                </div>
                <h1>
                    YOUR SCORE: 
					<div align= center>
					%s out of 5!
					</div>
					</div>
                </h1>
                <a data-role="button" data-transition="fade" href="/quiz">
                    TRY AGAIN!:D
                </a>
            </div>
        </div>
        <script>
            //App custom javascript
        </script>
    </body>
</html>'''%(num_correct_ans))

		


class VirtualCard(webapp.RequestHandler):
	def get(self):
		self.response.out.write('''<html>
	<head>
	<meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>
		P&C | Play 'n' Conquer
        </title>
        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.css" />
        <link rel="stylesheet" href="/static/tutorial_style.css" />
		<link href='http://fonts.googleapis.com/css?family=Dosis:200,300,400,600|The+Girl+Next+Door|Wire+One|Electrolize|Actor|Jura:400,600' rel='stylesheet' type='text/css'>
        <style>
            /* App custom styles */
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.1.1/jquery.mobile-1.1.1.min.js"></script>
        <script src="my.js"></script>
		<script src="jquery.fittext.js"></script>
	</head>
	<body>
	<div data-role="page" id="page">
	<div data-role="content" style="padding: 15px" class="container">
		<div class="title-mini">Play 'n' Conquer&nbsp;&nbsp;&nbsp;</div>
		<span class="home"><a rel="external" data-transition="fade" href="/">Home</a></span>
            <div class="h1" id="fittext">
                Virtual
            </div>
            <div class="h2" id="fittext">
                Cards
            </div>
		<form name="get" method="POST" action="/virtualcard2" data-ajax="false">
			<p>Enter value of cards (One text input for each card):<br>
			<input type="text" name="one" /></br>
			<input type="text" name="two" /></br>
			<input type="text" name="three" /></br>
			<input type="text" name="four" /></br>
			<input type="text" name="five" /></br>
			<input type="text" name="six" /></br>
			<input type="text" name="seven" /></br>
			<input type="text" name="eight" />
			<input type="submit" data-mini="true" value="&nbsp;&nbsp;Submit&nbsp;&nbsp;" data-inline="true"/>
			</p>
		</form>
	<div class="footer">
		<br>J<sup>3</sup> &copy; 2012<br>
	</div>
	</div>
	</div>
	</body>
</html>''')
		
class VirtualCard2(webapp.RequestHandler):
	def post(self):
		self.response.out.write('''<html>
  <head>
    <meta charset="utf-8">

    <title>Sort!</title>
	
    <style>body { background:#fff; font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; }</style>
	<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
	<script src="http://code.jquery.com/ui/1.8.21/jquery-ui.min.js"></script>
	<script src="jquery.ui.touch-punch.min.js"></script>

  </head>
  <body>

    <div class="container">
      
      <style>
              #sortable1, #sortable2 { list-style-type: none; margin: 0; padding: 0; float: left; margin-right: 10px; }
              #sortable1 li, #sortable2 li { margin: 0 5px 5px 5px; padding: 5px; font-size: 3.0em; width: 400px; }
              </style>
              <script>
              $(function() {
				$( "#sortable1, #sortable2" ).sortable({
				  cancel: ".label"
				});
				
                $( "#sortable1, #sortable2" ).sortable({
                  connectWith: ".connectedSortable"
                }).disableSelection();
              });
              </script>


            <div class="sorties">

            <ul id="sortable1" class="connectedSortable">
			  <li style="font-family: 'Arial Rounded', Helvetica; color: #333333; font-size: 2em;" class="label">Move to here</li>
            </ul>

            <ul id="sortable2" class="connectedSortable">
			  <li style="font-family: 'Arial Rounded',Helvetica; color: #333333; font-size: 2em;" class="label">Move from here</li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
              <li class="ui-state-highlight">
				%s
			  </li>
			  
            </ul>

			</div>
      
    </div>
    </body>
</html>'''% (self.request.get('one'),self.request.get('two'),self.request.get('three'), self.request.get('four'), self.request.get('five'), self.request.get('six'), self.request.get('seven'), self.request.get('eight')))
		
		
		

						

application = webapp.WSGIApplication([('/', MainPage),('/tut0', Page1),('/tut1', Page2),('/tut2', Page3),('/tut3', Page4),('/tut4', Page5),('/tut5', Page6),('/tut6', Page7),('/tut7', Page8),('/quiz', Quiz),('/virtualcard',VirtualCard),('/virtualcard2',VirtualCard2),('/quizqn',QuizQn),('/quizsubmit',QuizSubmit)], debug=True)

def main():
  run_wsgi_app(application)
  

if __name__ == "__main__":
  main()