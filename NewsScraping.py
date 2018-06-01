import requests
import pandas as pd
import numpy as np
import csv
from lxml import html

#url for link going to be extract
url = "https://aspermontlimited-editorial.cmail20.com/t/ViewEmail/j/89EB7EDD6D15B6662540EF23F30FEDED/A708CAEF102CF7A66707B176AE29F890"
#request url access
response = requests.get(url)
#parse the html docusment
doc = html.fromstring(response.text)

#summaries function to extract the story title
def titles():
    
    #xpath that will be extract
    paths = [
        
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/a',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td/a',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[5]/td/table[2]/tbody/tr[3]/td/a',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[7]/td/table[2]/tbody/tr[3]/td/a',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[12]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/a'
    ]
    
    #create an list to store the result
    res = []
    
    #a for loop to extract from the paths and convert a list into text
    for i in paths:
        title = doc.xpath(i)
        
        for n in title:
            titles = n.text
            res.append({titles.strip()})
    #convert a list into dataframe with pandas    
    df1 = pd.DataFrame(res)
    
    return df1

#summaries function to extract the story date  
def dates():
    
    #xpath that will be extract
    paths = [
        
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[5]/td/table[2]/tbody/tr[2]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[7]/td/table[2]/tbody/tr[2]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[12]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td'
        
    ]
    
    #create an list to store the result
    res = []
    
    #a for loop to extract from the paths and convert a list into text
    for i in paths:
        date = doc.xpath(i)
        
        for n in date:
            dates = n.text
            res.append({dates})
    #convert a list into dataframe with pandas  
    df2 = pd.DataFrame(res)
    
    return df2
        
#summaries function to extract the story summary
def summaries():
    
    #xpath that will be extract
    paths = [
        
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[5]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[5]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[5]/td/table[2]/tbody/tr[5]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[7]/td/table[2]/tbody/tr[5]/td',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[5]/td'
        
    ]
    
    #create an list to store the result
    res = []
    
    #a for loop to extract from the paths and convert a list into text
    for i in paths:
        summary = doc.xpath(i)
        
        for n in summary:
            summaries = n.text
            res.append({summaries.strip()})
    #convert a list into dataframe with pandas 
    df3 = pd.DataFrame(res)
    
    return df3

def urls():
    
    paths = [
        
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/a/@href',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td/a/@href',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[5]/td/table[2]/tbody/tr[3]/td/a/@href',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[6]/td/table/tbody/tr[7]/td/table[2]/tbody/tr[3]/td/a/@href',
        '/html/body/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr[12]/td/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/a/@href'
    ]
    
    #create an list to store the result
    res = []
    
    #a for loop to extract from the paths and convert a list into text
    for i in paths:
        urls = doc.xpath(i)
        
        for n in urls:
            #url = n.text
            #list4.append({urls})
            res.append(n)
        print(res)
    df4 = pd.DataFrame(res)
    #convert a list into dataframe with pandas 
    return df4

def main():
    urls()
    #conact the the three frames together
    result = pd.concat([titles(), dates(), summaries(), urls()], axis=1)
    
    #print out the result
    print(result)
    
    #export the result into .csv file
    result.to_csv('example.csv', encoding='utf-8', header = ['Title', 'Date', 'Summary', 'URL'])

    
if __name__ == "__main__":

    # calling main function
    main()

