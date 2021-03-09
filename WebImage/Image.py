from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import requests
from urllib.request import urlopen
import IPython

URL = "http://pudim.com.br/"
imglocal = "C:/Users/Jhony/PycharmProjects/MyPythonProject/WebImage/01.png"

#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                         '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
tittle = soup.find_all(classmethod('image'))

for c in tittle:
    for raw in c:
        print(raw,f'\n \n')
