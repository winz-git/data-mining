#!/usr/bin/env python3

from bs4 import  BeautifulSoup
from datetime import datetime
from urllib.request import urlopen 
import re
import os, sys
import json


# library path
from library.sqlite import * 


url = "http://bet.hkjc.com/marksix/Results.aspx?lang=en"
html = urlopen(url).read()
bs = BeautifulSoup(html)

table = bs.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == '_ctl0_ContentPlaceHolder1_resultsMarkSix_markSixResultTable')

# validate if table exists
if(table != None):
    rows = table.findAll('tr')
    
    for tr  in table.findAll(lambda tag: tag.name == u"tr"):
       try:
            draw_date = datetime.strptime(tr('td')[2].contents[0].string,"%d/%m/%Y")
            
       except:
            
            draw_date = None
    
    
       if(tr != None):
    
           for key in tr.findAll(lambda tag: tag.name == u"td" and tag.has_attr('align') and tag['align'] == 'right'):
                key_list = []
                key_str = key.text.strip()
        
                for td in key.findAll(lambda tag: tag.name ==u"td" and tag.has_attr('align') and tag['align'] == 'center'):
                    num_str = td.find('img')['src'].replace('/marksix/info/images/icon/no_','').replace('_s.gif?CV=L115R2a','')
                    
                    """ replace separator """
                    if num_str == '/marksix/info/images/en/icon_special_no.gif?CV=L115R2a':
                       num_str = "+"
        
                    key_list.append(num_str)
        
        
        
                print("Date:",draw_date, ",list=",key_list)
                
                try:
                    # db connect
                    db = dbSqlite("","", "", "","./db/datamining.db")
                    
                    # ONLY if draw date DOES NOT EXISTS
                    if(db.record_exists("main.marksixresult","draw_date", draw_date) != None):        
                        db.insert("insert into main.marksixresult(draw_date, result) values(?,?)", (draw_date, json.dumps(key_list)))
                        db.commit()
                    
                    db.close()
                    
                except Exception as e:      
                    print("Error", e)
       else:
           print("No Result in Detail")
    
else:
    print("No Draw Result")
    
     
            
        

 




