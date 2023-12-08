import requests
import bs4
from bs4 import BeautifulSoup

url = 'https://www.feastogether.com.tw/booking/Ajoy/shareinfo/e7d1a364-7504-4e76-80ca-2a768a0dd7e5'

# print整個網頁的HTML內容
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())  

#for link in soup.find_all('a'):
#    print(link.get('href'))

#送出這個 Cookie 便可以達到直接進入
#自行填入要傳入的cookie

#headers = {"cookie" : "over18=1"} 
#request = requests.get(url, headers = headers)

#解析網頁
#request = requests.get(url)
#data = bs4.BeautifulSoup(request.text, "html.parser")


#抓資料
#print(data)

#抓標題
#print(data.title)

#純文字
#print(data.title.text)

#解析網頁原始碼
#data = bs4.BeautifulSoup(request.text, "html.parser")
#titles = data.find_all("div", class_ = "title")

#利用for迴圈印出
#for title in titles:
#    if title.a != None:
#        print(title.a.string)


