import os
import re
from bs4 import BeautifulSoup
import requests
 
owd = os.getcwd()
os.chdir("C:/Users/Surbhi/Desktop")
soup = BeautifulSoup(open("AUGS-AGSR.html"), features="lxml")
val = input("Enter your course no.: ")
links = soup.find_all('a') 
for x in range(3, 312):
	fullLink = links[x].get('href')
	word= requests.get(fullLink).text
	if (word.find(val) != -1):
		res = requests.get(fullLink).content
		with open( val+".pdf", "wb" ) as code :
			code.write(res)
		break
