from bs4 import BeautifulSoup
import requests, sys, os

def getbody(url):
    try:
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, features="html.parser")
        title = str(soup.find_all("h1")[0].get_text())
        body = str(soup.find_all(id="content")[0])
        body = str(body).replace('<br>', "\r\n")
        body = str(body).replace('<br/>', "\r\n")
        result = body
    except(IndexError):
        title = result = ""
    return title, result

def getcontent(content_url):
    html = requests.get(url=content_url).text
    soup = BeautifulSoup(html, features="html.parser")
    num_page = len(soup.find_all(id="list")[0].select("a"))
    content_url = []
    for t in soup.find_all(id="list")[0].select("a"):
        content_url.append("https://www.ddxs.cc"+t.get("href"))
    return content_url

def processshow(index, total, cur=[0]):
    if (index*100)/total > cur[0]:
        cur[0] += 1
        print('\r', end='')
        print("============{}%===========".format(cur[0]), end='')

if __name__ == "__main__":
    content = getcontent("https://www.ddxs.cc/ddxs/147989/")
    text_name = "biquge.txt"
    # print(getbody("https://www.ddxs.cc/ddxs/147989/2527263.html"))
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
