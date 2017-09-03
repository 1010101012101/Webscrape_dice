# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:06:21 2017

Scraping the website for descriptions and relationship info 
https://www.dice.com/skills/browse

@author: Hsemu
"""
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

os.chdir('C:\\Users\Hsemu\Documents\Webscrape')
#Opening up the connection and grabbing the page
my_url="https://www.dice.com/skills/browse"


#Reduced link for getting to the pages inside website:
link_url="https://www.dice.com"    
    
#my_url="http://www.bunakara.com"

#Defining the function for parsing urls

def gethtmlpage(my_url):
    
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    
    #html Parsing
    page_soup=soup(page_html,"html.parser")
    return(page_soup);

#Parsing to html
url_split=my_url.split(".")
page_soup=gethtmlpage(my_url)


##Grabbing all the skills for opening to anotehr url
containers3=[]
getting_skills=[]
for elem in page_soup.find_all('a', href=re.compile('skills')):
    containers3.append(elem['href'])
    getting_skills.append(elem.text)

##Parsing each skills and getting the info
websitelinks=[]
websitelinks=[link_url+x for x in containers3]
gettingrelationship=[]
knowskills1=[]
knowskills2=[]
knowskills3=[]

filename="Dice_Scrape_skills.csv"
f=open(filename,"w")

headers="Skill"+"|"+"Relationship_1"+"|"+"Relationship_2"+"|"+"Relationship_3"+"\n"

f.write(headers)

#websitelinks=['https://www.dice.com/skills/ArchiCAD.html','https://www.dice.com/skills/Attention+to+detail.html','https://www.dice.com/skills/Automation.html']

for link in websitelinks:
    try:
        page_link=gethtmlpage(link)
        gettingrelationship=page_link.findAll("a",{"class":"toggle-bubble"})
        print(link)
        if(len(gettingrelationship)==3):
          knowskills1=gettingrelationship[0].text
          knowskills2=gettingrelationship[1].text
          knowskills3=gettingrelationship[2].text                   
          f.write(link+"|"+knowskills1+"|"+knowskills2+"|"+knowskills3+"\n")
        elif(len(gettingrelationship)==2):
          knowskills1=gettingrelationship[0].text
          knowskills2=gettingrelationship[1].text
          f.write(link+"|"+knowskills1+"|"+knowskills2+"\n")
        elif(len(gettingrelationship)==1):
          knowskills1=gettingrelationship[0].text  
          f.write(link+"|"+knowskills1+"\n")
        else:
          f.write(link+"|"+''+"\n")   
    except:
       pass
f.close()




