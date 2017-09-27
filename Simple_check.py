from bs4 import BeautifulSoup
import re
import urllib2
from BeautifulSoup import BeautifulSoup
from getpass import getpass
from urllib import urlencode

import requests

url = "github.com/GoogleCloudPlatform/reliable-task-scheduling-compute-engine-sample"

r  = requests.get("https://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))


