from bs4 import BeautifulSoup
import requests, sys, os

def getbody(url):
    try:
        r = requests.get(url=url)
        r.encoding = 'GBK'
        html = r.text
        soup = BeautifulSoup(html, features="html.parser")
        title = str(soup.find_all("h1")[0].get_text())
        body = str(soup.find_all(id="content")[0].get_text())
        # body = str(body).replace('<br>', "\r\n")
        # body = str(body).replace('<br/>', "\r\n")
        body = str(body).replace('\r', "")
        body = str(body).replace('\xa0'*4, "\r\n")
        body = body.split("https")[0]
        result = body #.split(title)[1]
    except(IndexError):
        title = result = ""
    return title, result

def getcontent(content_url):
    r = requests.get(url=content_url)
    r.encoding = 'GBK'
    html = r.text
    soup = BeautifulSoup(html, features="html.parser")
    a = (soup.find_all('dl')[0]).select("a")
    content_url = []
    for t in a[9:]:
        content_url.append("https://www.biqugexsw.com"+t.get("href"))
    return content_url

def processshow(index, total, cur=[0]):
    if (index*100)/total > cur[0]:
        cur[0] += 1
        print('\r', end='')
        print("============{}%===========".format(cur[0]), end='')

if __name__ == "__main__":
    content = getcontent("https://www.biqugexsw.com/7_7160/")
    text_name = "biquge.txt"
    # print(getbody(content[20]))
    try:
        os.remove(text_name)
    except(FileNotFoundError):
        pass
    with open(text_name, 'a', encoding="utf-8") as f:
        f.write("zhuixu"+"\n\n\n\n")
        for index, c in enumerate(content[:]):
            title, result = getbody(c)
            f.write("\n\n"+title+"\n\n")
            f.write(result)
            processshow(index, len(content))
    print("Finish!")
