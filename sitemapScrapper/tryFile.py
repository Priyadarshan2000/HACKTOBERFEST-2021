import requests
from bs4 import BeautifulSoup
import os
import time
def runCrawler():
    url = 'https://www.coingecko.com/sitemap1.xml'

    headers = {"Accept": "application/xml"}

    response = requests.request("GET", url, headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')

    d = soup.find_all("xhtml:link")

    if os.path.exists('./reference.txt'):
        for details in d:
            href = details.get('href')
            with open('freshRun.txt', 'ab') as f:
                f.write( href.encode('utf-8')+'\n'.encode('utf-8') )
            f.close()
    else:
        for details in d:
            href = details.get('href')
            with open('reference.txt','ab') as f:
                f.write( href.encode('utf-8')+'\n'.encode('utf-8') )
            f.close()
    try:
        with open('./reference.txt','rb') as d:
            read_first_line = d.readline()
            for last_read in d:
                pass
        refLastLine = last_read
        with open('./freshRun.txt','rb') as f:
            first_Line = f.readline()
            for last_line in f:
                pass
        freshLastLine =  (last_line)
        if refLastLine != freshLastLine:
            with open("freshRun.txt","rb") as f:
                with open("reference.txt", "wb") as f1:
                    for line in f:
                        f1.write(line)
            return (str(freshLastLine)[2:-1])
        else:
            return ('No new links added')
    except Exception as e:
        return e
if __name__ == '__main__':
    print (runCrawler())