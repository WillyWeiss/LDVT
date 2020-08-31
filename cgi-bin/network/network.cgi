#!/bin/bash
#File Name: network.cgi
#File Purpuse: Caputure networking statistics from main operating system and display into HTML form.
#File Highlights: Use and external Python script to obtain and show informations. 
#Created by: Willy Weiss
#Contact me on Linkedin: https://www.linkedin.com/in/willy-weiss/
#Contact me on Github: https://github.com/WillyWeiss

## General CGI Header
echo "Content-type: text/html"
echo ""
echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
## CGI SYTLE
echo '<style type="text/css"> '
echo '.tg  {border-collapse:collapse;border-spacing:0;}                                                          '
echo '.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;'
echo '  overflow:hidden;padding:10px 5px;word-break:normal;}                                                     '
echo '.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;'
echo '  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}                                  '
echo '.tg .tg-baqh{text-align:center;vertical-align:top}                                                         '
echo '</style>                                                                                                   '
echo '</head>'

## Start of body
echo '<body>'

## Start of table
echo ' <table class="tg" style="margin-right: auto; margin-left: auto;">                                               '
echo ' <thead>                                                         '
echo '   <tr>                                                           '
echo '     <th class="tg-baqh" colspan="4">Network Traffic Monitor</th> '
echo '   </tr>                                                          '
echo ' </thead>                                                         '
echo ' <tbody>                                                          '
echo '   <tr>                                                           '
echo '     <td class="tg-baqh" colspan="2">Card Name</td>               '
echo '     <td class="tg-baqh">RX</td>                                  '
echo '     <td class="tg-baqh">TX</td>                                  '
echo '   </tr>                                                          '
echo '   <tr>                                                           '


## Place here the names of your ethernet card
echo '     <td class="tg-baqh" colspan="2">Ethernet</td>'
## Track your RX TX packets using the general form
## cat /sys/class/net/YOUR_CARD_NAME/statistics/rx_packets
## cat /sys/class/net/YOUR_CARD_NAME/statistics/tx_packets
echo '     <td class="tg-baqh">' $(cat /sys/class/net/enp2s0/statistics/rx_packets) '</td>                                  '
echo '     <td class="tg-baqh">' $(cat /sys/class/net/enp2s0/statistics/tx_packets) '</td>                                  '
echo '   </tr>                                                          '
echo '   <tr>                                                           '


## Same for the second card
echo '     <td class="tg-baqh" colspan="2">Wifi</td>                  '
echo '     <td class="tg-baqh">' $(cat /sys/class/net/wlp3s0/statistics/rx_packets) '</td>                                  '
echo '     <td class="tg-baqh">' $(cat /sys/class/net/wlp3s0/statistics/tx_packets) '</td>                                  '
echo '   </tr>                                                          '
echo '   <tr>                                                           '
echo '     <td class="tg-baqh" colspan="4">DNS Check</td>               '
echo '   </tr>                                                          '
echo '   <tr>                                                           '
echo '     <td class="tg-baqh" colspan="4">' $(python3 cgi-bin/dns.py) '</td>             '
echo '   </tr>                                                          '
echo ' </tbody>                                                         '
echo ' </table>                                                         '
echo '</body>'
echo '</html>'

