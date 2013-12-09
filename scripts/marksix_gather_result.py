from bs4 import  BeautifulSoup
import urllib2

url = "http://bet.hkjc.com/marksix/Results.aspx?lang=en"
html = urllib2.urlopen(url).read()
bs = BeautifulSoup(html)

table = bs.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == '_ctl0_ContentPlaceHolder1_resultsMarkSix_markSixResultTable')
rows = table.findAll('tr')
#row = rows.findall(lambda tag: tag.has_attr('class') and tag['class'] == 'tableResult2')
#cols = rows.findAll('td', attrs={'class':'tableResult2'})
for tr  in table.findAll(lambda tag: tag.name == u"tr"):
   for key in tr.findAll(lambda tag: tag.name == u"td"):
        key_list = []
        key_str = key.text.strip()
        for td in key.findNextSiblings(lambda tag: tag.name ==u"td"):
            print td.string
            key_list.append(td.text)
        #key_list = map(float, key_list)

        print key
      

#print cols


