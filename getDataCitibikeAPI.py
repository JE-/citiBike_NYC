import requests
from datetime import datetime

url = 'https://www.citibikenyc.com/stations/json'
data = requests.get(url)
t = datetime.now()
with open('API_Data/' +str(t),'w') as f:
     f.write(data.text)
