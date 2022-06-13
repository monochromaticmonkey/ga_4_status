import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

#imput a list of sites that you would like to review

liste = ['https://nike.com/']

def gaStatus(liste):
    emp = []

    for i in liste:
        try:
            web_page = i

            # call get method to request that page
            page = requests.get(web_page)

            # with the help of beautifulSoup and html parser create soup
            soup = BeautifulSoup(page.content, "html.parser")

            child_soup = soup.find_all('script')

            #use regex to find "G-" which is the text that starts the GA4 code
            finder = re.findall(r"G-(.*?)", str(child_soup))

            if finder != []:
                emp.append({'website':i,'status':'G4 Ready'})
            else:
                emp.append({'website':i,'status':'Not G4 Ready'})
        except:
            pass

    return emp
