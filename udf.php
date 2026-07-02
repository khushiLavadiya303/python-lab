<?php
#simple function
function name()
{
	echo $name="hello hello";
}
name();
echo"<br>";

#argument function
#1. call by value
function add($num)
{
	echo $num=$num+5;
}
$x=20;
add($x);
echo"<br>";
echo $x;
echo"<br>";

#2.call by reference
function addone(&$num)
{
	echo $num=$num+5;
}
$x=20;
addone($x);
echo"<br>";
echo $x;
echo"<br>";

#return of function
function addtwo($a,$b)
{
	$c=$a*$b;
	return $c;
}
echo addtwo(5,2);
echo"<br>";

#variable function
function xyz($name)
{
	echo $name;
}
$a="xyz";
$a("xyz");

echo"<br>";

#default argument
function addthree($a,$b,$c=10)
{
	echo $a+$b+$c;

}
addthree(5,10);
echo"<br>";
#nesting function
function one($name)
{
	echo $name;
}
function two()
{
	echo"two is here";
	one("this is one");
}
two();

#array 
$a=array(23,25,28);
echo $a[2];
?>