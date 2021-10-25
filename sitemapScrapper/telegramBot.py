import tryFile
import requests

dataReceived = tryFile.runCrawler()


base_url = 'https://api.telegram.org/bot<YOUR_API_ID>/sendMessage?chat_id=-<YOUR_CHAT_ID>&text={}'.format(dataReceived)
response = requests.get(base_url)
print (response)


