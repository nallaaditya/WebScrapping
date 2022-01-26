import json
import requests
from bs4 import BeautifulSoup

def getPropertyDetails(propertyDict):
    propertyPage=requests.get(propertyDict["propertyUrl"])
    propertySoup = BeautifulSoup(propertyPage.text, "html.parser")
    agencyInfo=propertySoup.find('div',attrs={'class':'account-content agency'})
    try:
        agencyName=agencyInfo.find('h4',attrs={'class':'heading account-name'}).text
        propertyDict["agencyName"]=agencyName
    except:
        propertyDict["agencyName"]=None
    try:
        agencyAddress1=agencyInfo.find('div',attrs={'class':'address'}).text
        try:
            agencyAddress2=agencyInfo.find('div',attrs={'class':'contact-info-child city-block'}).text
        except:
            agencyAddress2=None
        if(agencyAddress2==None):
            propertyDict["agencyAddress"]=agencyAddress1
        else:
            propertyDict["agencyAddress"]=agencyAddress1+" "+agencyAddress2
    except:
        propertyDict["agencyAddress"]=None
    try:
        agencyPhNo=agencyInfo.find('div',attrs={'class':'agency-phone phone-number'}).text
        propertyDict["agencyPhNO"]=agencyPhNo
    except:
        propertyDict["agencyPhNO"]=None
    print(propertyDict)

        
        
def getData(baseUrl,continentName,countryName,countryUrl):
    countryPage=requests.get(countryUrl)
    countrySoup = BeautifulSoup(countryPage.text, "html.parser")
    propertiesList=countrySoup.find_all('div',attrs={'class':'item-data'})
    for property in propertiesList:
        propertyName=property.find('a',attrs={'class':'link listing-title stretched-link'}).text
        propertyBody=property.find('div',attrs={'class':'item-body'})
        propertyUrl=baseUrl+propertyBody.find('a')['href']
        propertyPrice=property.find('span',attrs={'class':'title-price'}).text
        itemdict={}
        itemdict["propertyName"]=propertyName
        itemdict["propertyUrl"]=propertyUrl
        itemdict["propertyPrice"]=propertyPrice
        itemdict["continentName"]=continentName
        itemdict["countryName"]=countryName
        #print(itemdict)
        getPropertyDetails(itemdict)
        


