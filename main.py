import sys
import requests
from bs4 import BeautifulSoup


g = input("Enter poslaju tracking number : ") 

url = 'https://www.poslaju.com.my/track-trace-v2/'
myobj = {'trackingNo03': g}

x = requests.post(url, data = myobj)

start_of_table_idx = x.text.rfind('<table', 0, x.text.find('tbDetails'))
end_of_table_idx = x.text.rfind('</table>', x.text.find('tbDetails'), len(x.text))

soup = BeautifulSoup(x.text[start_of_table_idx:end_of_table_idx+len('</table>')], 'lxml')

for td in soup.tbody.tr.contents:
  print(td.text)
  