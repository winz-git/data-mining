from bs4 import  BeautifulSoup
from datetime import datetime
import urllib2
import re
import os, sys
import json


# library path
import lib

url = "http://bet.hkjc.com/marksix/Results.aspx?lang=en"
html = urllib2.urlopen(url).read()
bs = BeautifulSoup(html)

table = bs.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == '_ctl0_ContentPlaceHolder1_resultsMarkSix_markSixResultTable')
rows = table.findAll('tr')
#row = rows.findall(lambda tag: tag.has_attr('class') and tag['class'] == 'tableResult2')
#cols = rows.findAll('td', attrs={'class':'tableResult2'})
for tr  in table.findAll(lambda tag: tag.name == u"tr"):
   try:
        draw_date = datetime.strptime(tr('td')[2].contents[0].string,"%d/%m/%Y")
        #print "Subscription Date:", draw_date
   except:
        #print "Error in dateValue"
        draw_date = None



   for key in tr.findAll(lambda tag: tag.name == u"td" and tag.has_attr('align') and tag['align'] == 'right'):
        key_list = []
        key_str = key.text.strip()

        for td in key.findAll(lambda tag: tag.name ==u"td" and tag.has_attr('align') and tag['align'] == 'center'):
            num_str = td.find('img')['src'].replace('/marksix/info/images/icon/no_','').replace('_s.gif?CV=L115R2','')
            #print num_str.replace('/marksix/info/images/icon/no_','').replace('_s.gif?CV=L115R2','')
            if num_str == '/marksix/info/images/en/icon_special_no.gif?CV=L115R2':
                num_str = "+"

            key_list.append(num_str)



        print "Date:", draw_date, ", list=", key_list

        #print key
      

#print cols

#
# print db("", "", "", "", "../../data/datamining.db") 




