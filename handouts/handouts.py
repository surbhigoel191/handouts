import os
from bs4 import BeautifulSoup
import requests
owd = os.getcwd()
os.chdir("C:/Users/Surbhi/Desktop")
soup = BeautifulSoup(open("AUGS-AGSR.html"), features="lxml")

links = soup.find_all('a')
for x in range(3, 312):
	fullLink = links[x].get('href')
	res = requests.get(fullLink).content
	# print(fullLink)
	with open( "myfile.pdf", "wb" ) as code :
		code.write(res)