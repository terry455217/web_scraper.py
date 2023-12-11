import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# 加載.env文件中的環境變量
load_dotenv()

# 從環境變量中獲取URL
url = os.getenv('URL')

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




#USER-AGENT

#新增USER-AGENT 可以偽裝成瀏覽器

headers = {
    "user-agent": "可以加入瀏覽器的headers"
}

#COOKIES

#夾帶COOKIES 可以跳過登入步驟

