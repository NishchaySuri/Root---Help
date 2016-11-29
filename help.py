#!/usr/bin/env python

import webbrowser
import sys

if len(sys.argv)>=1:
    address=''.join(sys.argv[1])

if(sys.argv[2]=='-o'):
    webbrowser.open('https://root.cern.ch/doc/master/class'+address+'.html')

if(sys.argv[2]):
    import requests
    from bs4 import BeautifulSoup

    url='https://root.cern.ch/doc/master/class'+address+'.html'

    r=requests.get(url)

    soup=BeautifulSoup(r.content,'html.parser')

    search_results=soup.find_all("td",{"class":"memname"})



    for i in range(0,len(search_results)):
        if(sys.argv[2] in search_results[i].text):
            function_title=search_results[i].parent.parent.text
            function_title=function_title.replace("\n","")
            function_description=search_results[i].parent.parent.parent.parent.parent.parent.next_sibling
            print(" ")
            print(soup.title.text)
            print(" ")
            print(function_title)
            print(function_description.text)
            
