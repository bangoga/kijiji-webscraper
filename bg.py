#---- Simple Price Scrapper ----# 

import urllib.request
import bs4
import pandas as pd
import numpy as np  # np is the shortcut to be used. 
import matplotlib.pyplot as mp
import pandas as pd;

import csv
import collections
#--- Making this as a method

def getItemprice():
#---- Get all possible tags into the script
    try:
        searchurl=autoSearch()
        data = urllib.request.urlopen(searchurl)
        #-data = urllib.request.urlopen("https://www.kijiji.ca/v-1-bedroom-apartments-condos/ville-de-montreal/grand-3-1-2-sept-n-d-g-pres-du-metro-villa-maria-balcon/1276186407?null")
        details = data.read()
    except: 
      pass
    
    datasouped1 = bs4.BeautifulSoup(details,"lxml")
    datasouped = bs4.BeautifulSoup(details,"lxml")
    datasouped=datasouped.prettify()
    
    #---- datasouped is prettified to show the markup 
    
    datasouped1.title
    
    #-- Get tells you all the class type that is available. 
    #for item in datasouped1.find_all(itemprop="price"):
    allPrices=[]
    
    for item in datasouped1.find_all("div", { "class" : "price" }):
            print(item.get_text())
            allPrices.append(item.get_text())
            
            
    finalPrices=[]
    for item in allPrices:
        item= item.replace('\n','')
        item = item.replace(' ','')
        item=item.replace('$','')
        print(item)
        finalPrices.append(item)
         
    allPrices.clear()
     
     
         
    results= np.array(finalPrices)
   
    writer=csv.writer(open('C:/CSVfiles','wb'))
    length_list=len(finalPrices)
    i=0
    while i!=length_list :
        data = finalPrices[i]
        print(data)
        i=i+1
        writer.writerow([data])
    
   
    df = pd.DataFrame(results.reshape(50,2))


getItemprice()

from selenium import webdriver

#---------------------New Method ----------------#  
#driver = webdriver.PhantomJS()
def autoSearch():
    cDriver = webdriver.Chrome("chromedriver.exe")
    url = "https://www.kijiji.ca/?siteLocale=en_CA"
    searchclass = "inputKeyword-3403971570 inputKeyword__on-3728696649"
    
    cDriver.get(url)
    textbox= cDriver.find_element_by_css_selector(".inputKeyword-3403971570")
    textbox.send_keys("house")
    searchbtn=cDriver.find_element_by_css_selector(".searchSubmit-3685231415")
    searchbtn.click()
    
    currenturl=cDriver.current_url

    return currenturl
