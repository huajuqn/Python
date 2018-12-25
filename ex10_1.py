import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(name,a):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format("排名","学校名称","省市","总分","培养规模"))
    rang=0
    for i in range(len(allUniv)):
        u=allUniv[i]
        if name in u[a]:
            
            print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(u[0],u[1],u[2],u[3],u[6]))
            rang+=1
            if rang ==10:
                break
def main(name,a):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(name,a)
print("北京的大学有")
main("北京",2)
print("江西的大学有")
main("江西",2)
print("包含理工的大学有")
main("理工",1)
print("包含交通的大学有")
main("交通",1)
