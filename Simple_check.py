from bs4 import BeautifulSoup

import requests

url = "www.google.com.sg/search?dcr=0&source=hp&q=python&oq=python&gs_l=psy-ab.3..0i131k1l3j0.6479.7949.0.8229.6.6.0.0.0.0.183.335.0j2.2.0....0...1.1.64.psy-ab..4.2.334....0.aT6b7NR6SS0"

r  = requests.get("https://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

mail.send_mail(sender=sender_address,
                   to="Umesh Kumar <umeshdhanwal@gmail.com>",
                   subject="Your account has been approved",
                   body="""Dear Umesh

Please let us know if you have any questions.

The example.com Team
""")
