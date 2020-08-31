#File Name: script.gnuplot                                               
#File Purpuse: Plot data from sample1.csv intro a JPG image.
#File Highlights: Basic PLOT script to generate a simple 2 axis graphics with reference lines.The output will be a simple PNG image.
#Created by: Willy Weiss
#Contact me on Linkedin: https://www.linkedin.com/in/willy-weiss/
#Contact me on Github: https://github.com/WillyWeiss

## First set the data separator, in this case comma.
set datafile separator ','
## Set the data type and format of the X axis
set xdata time
set timefmt "%Y-%m-%dT%H:%M:%S"
## Set the title
set key autotitle columnhead # use the first line as title
set ylabel "First Y Units" # label for the Y axis
set xlabel 'Time' # label for the X axis
## Setup output
set terminal png 
set output '../../images/sample1.png'

## Final PLOT command. Here you specifly the file path and wich colums to be used as axis.
## As an english translation of the below command you can read:
## Plot file sample1.csv using colum 1 for X axis and colum 2 for Y axis, using lines as graphics (you can use other characters also) than do the same using colum 1 for X axis and colum 3 for Y axis using lines as graphs. 
plot 'sample1.csv' using 1:2 with lines, '' using 1:3 with lines
