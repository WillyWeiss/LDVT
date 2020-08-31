#!/bin/bash
#File Name: sample.cgi
#File Purpuse: Use this file as templeate to test your own CGI scripts.
#File Highlights: Ensure a Hellow World functionality. 
#Created by: Willy Weiss
#Contact me on Linkedin: https://www.linkedin.com/in/willy-weiss/
#Contact me on Github: https://github.com/WillyWeiss

## First create a variable to be placed inside the webpage. Use pure BASH.
name=$(hostname)


## Now tell Bash what type of content you will like to display
echo "Content-type: text/html"
echo ""
## Now use your HTML code, but put everything inside an "echo" or "printf" statement
## Start with the HTML header. You can use even external css files.
echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '</head>'
echo '<body>'
## Use a simple echo statment as in your everyday coding.
echo "HELLO WORLD my name is $name"
echo '</body>'
echo '</html>'
## Exit your program as usual
exit 0
