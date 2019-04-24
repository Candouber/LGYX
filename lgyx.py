import requests
import re
import os

class LGYX(object):
    url = []

    def __init__(self):
        for i in range(29177934, 29178448):
            self.url.append('https://www.23wx.so/54_54486/' + str(i) + '.html')

    def __getitem__(self, item):
        return self.url[item]

def getpage():
    lgyx = LGYX()
    for i in lgyx:
        res = requests.get(i)
        if res.status_code == 200:
            con = res.content
            html = con.decode('gb2312',"ignore")
            parseurl(html)
        else:
            print('错误')

def parseurl(html):
    pattern = r'.*name="content">(.*?)</div>'
    artical = re.findall(pattern, html, re.S)
    content = re.sub(r'[&nbsp;<r>/]','', artical[0])
    save(content)

def save(artical):
    file = open('lgyx.txt', 'a')
    print(artical, file=file)
    file.close()

if __name__ == '__main__':
    getpage()
