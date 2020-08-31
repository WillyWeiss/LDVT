#File Name: script_2.gnuplot                                               
#File Purpuse: Plot data from sample3.csv intro a JPG image.
#File Highlights How to plot data from a csv file into a JPG using more the just 2 axis
#Created by: Willy Weiss
#Contact me on Linkedin: https://www.linkedin.com/in/willy-weiss/
#Contact me on Github: https://github.com/WillyWeiss

## First set the data separator, in this case comma.
set datafile separator ','

## Setup what data type will be on X axis
set xdata time 

## How the data will be formated?
set timefmt "%Y-%m-%dT%H:%M:%S"

## Set columnhead name and title (in this case we use the names from the first row of the file)
set key autotitle columnhead

##set name for X and Y axis
set ylabel "First Y Units" 
set xlabel 'Time'

## Set First Y units scale
set y2tics

## Will the text show in mirror, easy to ren in some situations?
## In this case NO. nomirror. 
set ytics nomirror

## Set the second Y Axis name
set y2label "Second Y Axis Value"

## How the line will be ploted, in which colos?
set style line 100 lt 1 lc rgb "grey" lw 0.5 
## How big will be the grid?

set grid ls 100 
# What is the minimum value of Y axis? ( Deafult is 0, in this case I demonstrate a dieferent value, so you can understand that the values can be diferent then 0)
set ytics 0.5

# What is the minimum value of X axis? ( Deafult is 0, in this case I demonstrate a dieferent value, so you can understand that the values can be diferent then 0)
set xtics 1 

## Set the output of the plot. In witch form will you like the see the graphs?
## In this case is demonstrated a JPEG output in wich you can adjust the resolution, font sise and font type.
set terminal jpeg small font arial size 800,600 

## Set the output path of the ploted data. 
set output '../../images/sample2.jpg'

## Set the line styles, so we can use them in the final plot
set style line 101 lw 3 lt rgb "#f62aa0" # style for targetValue (1) (pink)
set style line 102 lw 3 lt rgb "#26dfd0" # style for measuredValue (2) (light blue)
set style line 103 lw 4 lt rgb "#b8ee30" # style for secondYAxisValue (3) (limegreen)

## Final PLOT command. Here you specifly the file path and wich colums to be used as axis.
## As an english translation of the below command you can read:
### Plot file sample3.csv using colum 1 as X axis and colum 2 as the Y axis using line style 101 (declared above), also do the same using colum 1 for X axis and colum 3 for Y axis using line style 102, also do the same using colum 1 for X axis and colum 4 for Y axis using line style 102 ALSO place the values of X on the first X axis and the Y values on the SECOND Y Axis (declared above)
plot 'sample2.csv' using 1:2 with lines ls 101, '' using 1:3 with lines ls 102, '' using 1:4 with lines axis x1y2 ls 103




