from bs4 import BeautifulSoup
from datetime import datetime
import re
import requests

# Come back and format for Command

r = requests.get('http://www.chezpanisse.com/menus/cafe-menu/')

all_p = soup.find_all('p')

# Get date and make usable
m_date = str(all_p[0])
m_date = m_date.replace('<p>','').replace('</p>','')
m_date = m_date.replace('<!-- menu start --><br/>\n','')
m_date = str(re.search('\w+ \d+, \d+$', m_date).group(0))
m_date = datetime.strptime(m_date, '%B %d, %Y').date()

menu = []

for p in all_p[1:]:
    p = str(p)
    item = {}
    if "service charge" in p:
        break
    elif "<strong>Side orders: </strong>" in p:
        pass
    else:
        strip_p = p.replace('<p>','').replace('</p>','').replace('<br/>','')
        clean = strip_p.split('$')
        item['date'] = m_date
        item['food'] = clean[0]
        item['price'] = clean[1]
        item['raw'] = p
        item['raw_date'] = str(all_p[0])
        menu.append(item)
