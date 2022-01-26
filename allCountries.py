from email.mime import base
import requests
from bs4 import BeautifulSoup
import getCountryData


#base url
baseUrl="https://www.properstar.com"
#page url
allCountriesUrl="https://www.properstar.com/all-countries"

#get the page data through requests;
allCountriesPage=requests.get(allCountriesUrl)

#creating a parsed tree using soup;
allCountriesSoup = BeautifulSoup(allCountriesPage.text, "html.parser")

continents=allCountriesSoup.find_all('div',attrs={'class':'continent'})

for continent in continents:
    #getting the current Continent Name;
    continentName=continent.find("h3").text
    #getting the list of countries listed in each continent;
    countries=continent.find_all('li',attrs={'class':'list-item'})
    #iterating through each continent
    for country in countries:
        #getting the country name
        countryName=country.find('span',attrs={'class':'country-name'}).text
        #get the url of homes in that country;
        countryUrl=baseUrl+country.find('a')['href']
        getCountryData.getData(baseUrl,continentName,countryName,countryUrl)
        break
    
        
        
    

