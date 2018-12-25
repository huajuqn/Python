import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    try:
        r = requests.get(url, headers=send_headers)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def fillUnivList(soup, allUniv):
    data = soup.find_all('div',{'class':re.compile('shadow-dark')})
    for div in data:
        singleUniv = []
        div1 = div.find('div',{'style':'margin-left: 2.5rem;'})
        rank = div1.get_text().strip()
        singleUniv.append(rank.split(' ')[0])

        h3 = div.find('h3')
        singleUniv.append(h3.get_text().strip())
        ldiv = div.find_all('div',{'style':'padding-right: 0.5rem;'})
        singleUniv.append(ldiv[0].strong.string)
        singleUniv.append(ldiv[1].strong.string)
        addrp=div.find_all('p',{'class':"display-block block-normal text-small"})
        singleUniv.append(addrp[0].get_text().strip())
        allUniv.append(singleUniv)
        
        
        
def printUnivList(allUniv,shat="none"):
    print("{:<10}{:<20}{:<10}{:<10}{:<10}".format("排名","学校名称","学费","培养规模","地址"))
    for u in allUniv:
        if shat=="fill":
            if 4000<=eval(u[2][1:])<=5000:
                print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(u[0],u[1],u[2],u[3],u[4]))
        elif shat=="addr":
            if u[4][-2:]=="CA":
                print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(u[0],u[1],u[2],u[3],u[4]))
                
        else:
            print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(u[0],u[1],u[2],u[3],u[4]))


def main(num,shat):
    allUniv = []
    url = 'https://www.usnews.com/best-colleges/rankings/national-universities'

    for i in range(1, num+1):
        ri = url + '?_page=' + str(i)
        html = getHTMLText(ri)
        soup = BeautifulSoup(html, 'html.parser')
        fillUnivList(soup, allUniv)
    printUnivList(allUniv,shat)


#main(4,"fill")
main(4,"addr")
main(4,"none")
