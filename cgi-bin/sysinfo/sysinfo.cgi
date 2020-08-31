#!/bin/bash

#File Name: sysinfo.cgi                                                
#Created by: Willy Weiss
#Contact me on Linkedin: https://www.linkedin.com/in/willy-weiss/
#Contact me on Github: https://github.com/WillyWeiss


## Start with your classic bash code
##Setup variable
host=$(hostname)
up=$(uptime | awk '{print $3}' | sed 's/,//')
manufacturer=$(cat /sys/class/dmi/id/chassis_vendor)
name=$(cat /sys/class/dmi/id/product_name)
version=$(cat /sys/class/dmi/id/product_version)
type=$(vserver=$(lscpu | grep Hypervisor | wc -l); if [ $vserver -gt 0 ]; then echo "VM"; else echo "Physical"; fi)
os=$(hostnamectl | grep "Operating System" | cut -d ' ' -f5-)
kernel=$(uname -r)
arch=$(arch)
cpuname=$(awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ \t]*//')
user=$(w | cut -d ' ' -f1 | grep -v USER | xargs -n1)
ip=$(hostname -I)

##End of Variable


##Start the CGI script by telling bash what type of file you will create
echo "Content-type: text/html"
echo ""

## Now place you HTML code inside echo statesments
#First we start with the main header of the HTML page. The head, title and styles will be defined in this section.
#You can always choose bettwen integrated style or external css file. Just keep all your HTML code inside echo statesments.
echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '<style type="text/css">                                                                                    '
echo '.tg  {border-collapse:collapse;border-spacing:0;}                                                          '
echo '.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;'
echo '  overflow:hidden;padding:10px 5px;word-break:normal;}                                                     '
echo '.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;'
echo '  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}                                  '
echo '.tg .tg-0pky{border-color:inherit;text-align:center;vertical-align:top}                                      '
echo '.tg .tg-baqh{text-align:center;vertical-align:top}'
echo '</style>                                                                                                   '
echo '</head>'
echo '<body>'

## Now continue with the main body of the page, fallwing the same principles as above.
## Beacuse of the CGI form of this script, now you can use the above variable`s output into the HTML page.
## I created a simple table in wich`s cell I place the output of the above variables.

echo '<table class="tg" style="position:absolute;top:0;left:0;width:100%;height:100%;">                                         '
echo '<thead>                                                    '
echo '  <tr>                                                     '
echo '    <th class="tg-baqh" colspan="2">System Information</th>'
echo '  </tr>                                                    '
echo '</thead>                                                   '
echo '<tbody>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Hostname</td>                      '
echo '    <td class="tg-baqh">' $host '</td>   '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Uptime</td>                        '
echo '    <td class="tg-baqh">' $up '</td>                       '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Manufacturer</td>                  '
echo '    <td class="tg-baqh">' $manufacturer '</td>             '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Product Name</td>                  '
echo '    <td class="tg-baqh">' $name '</td>                     '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Version:</td>                      '
echo '    <td class="tg-baqh">' $version '</td>                  '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Machine Type</td>                  '
echo '    <td class="tg-baqh">' $type '</td>                     '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Operating System:</td>             '
echo '    <td class="tg-baqh">' $os '</td>                       '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Kernel</td>                        '
echo '    <td class="tg-baqh">' $kernel '</td>                   '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Architecture</td>                  '
echo '    <td class="tg-baqh">' $arch '</td>                     '
echo '  </tr>                                                    '
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">Processor Name:</td>               '
echo '    <td class="tg-baqh">' $cpuname '</td>                  '
echo '  </tr> '                                                
echo '  <tr>                                                     '
echo '    <td class="tg-baqh">System Main IP</td>                '
echo '    <td class="tg-baqh">'$ip '</td>                        '
echo '  </tr>                                                    '
echo '</tbody>                                                   '
echo '</table>                                                   '
echo '</body>'
echo '</html>'
## Now simply exit the program. 
exit 0
