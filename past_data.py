from bs4 import BeautifulSoup
import requests
import  pandas as pd

years=[]
for i in range(1960, 2021,4):
    years.append(i)

web='https://en.wikipedia.org/wiki/UEFA_Euro_2020'

response= requests.get(web)
content=response.text
soup=BeautifulSoup(content,'lxml')

matches=soup.find_all('div', class_='footballbox') #find all gets multiple in a list with class_='footballbox'

home =[]
score=[]
away=[]

for match in matches:
    home.append(print(match.find('th',class_='fhome').get_text()))
    score.append(print(match.find('th',class_='fscore').get_text()))
    away.append(print(match.find('th',class_='faway').get_text()))


dict_football={'home':home,'score':score,'away':away}
df_football=pd.DataFrame(dict_football)
df_football['year']='2020'
print(df_football)
