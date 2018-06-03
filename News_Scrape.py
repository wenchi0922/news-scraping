import requests
import pandas as pd
import numpy as np
import csv
from lxml import html
from bs4 import BeautifulSoup

#url for link going to be extract
url = "//myurl"
#request url access
response = requests.get(url)
#parse the html docusment
soup = BeautifulSoup(response.content, "html.parser")
soups = soup.find_all("div", class_="story-content")
print(len(soups))

#summaries function to extract the story title
def getTitles():
    
    res = []
    
    for i in soups:
        titles = i.find_all("h3", class_="story-title")
        if titles:
            for n in titles:
                title = n.text
            
        else:
            
            title = "No data"
        
        res.append({title.strip()})
        
    df1 = pd.DataFrame(res)        
    print(df1)
    return df1
    
    
#summaries function to extract the story date  
def getDates():
    
    res = []
    
    for i in soups:
        dates = i.find_all("span", class_="timestamp")
        
        if dates:
            for n in dates:
                date = n.text
               
        else:
            
            date = "No data"
        
        res.append({date.strip()})
    
    df2 = pd.DataFrame(res)
    print (df2)
    return df2

#summaries function to extract the story summary
def getSummaries():
    
    res = []
    
    for i in soups:
        summaries = i.find_all("p")
        
        if summaries:
            for n in summaries:
                summary = n.text
        
        else:
            summary = "No data"
        
        res.append({summary.strip()})
        
    df3 = pd.DataFrame(res)
    print(df3)
    return df3
    

def urls():
    
    res = []
    
    #a for loop to extract from the paths and convert a list into text
    for i in soups:
        urls = i.find_all("a")
        
        for url in urls:
            links = url.get('href')
                    
        res.append({links.strip()})

    df4 = pd.DataFrame(res)
    print(df4)
    #convert a list into dataframe with pandas 
    return df4

def main():
    
    #conact the the three frames together
    result = pd.concat([getTitles(), getDates(), getSummaries(), urls()], axis=1)
    
    #print out the result
    #print(result)
    
    #export the result into .csv file
    result.to_csv('example.csv', encoding='utf-8', header = ['Title', 'Date', 'Summary', 'URL'])

    
if __name__ == "__main__":

    # calling main function
    main()
