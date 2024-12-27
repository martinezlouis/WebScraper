from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

service = Service("C:\\Users\\louis\\OneDrive - Year Up- BOS\\YearUp\\Mod 3\\Python\\Week17\\Project\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser") 

driver.quit()

results = []
other_results = []

for element in soup.findAll(attrs={'class': 'title'}):  
    name = element.find('a')  
    if name and name.text: 
        results.append(name.text.strip())

for b in soup.findAll(attrs={'class': 'preview'}): 
    if b.text: 
        other_results.append(b.text.strip())

df = pd.DataFrame({"Title": results, "Preview": other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

print("Data saved to names.csv")
