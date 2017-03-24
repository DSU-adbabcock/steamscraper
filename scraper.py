
import requests
import sys
import codecs
from bs4 import BeautifulSoup

pages = int(sys.argv[1])
curPage = 1

titles_master = []
prices_master = []
sales_master = []

for page in range(1, pages+1):
	page = requests.get("http://store.steampowered.com/search/?specials=1&page=" + str(page))
	
	soup = BeautifulSoup(page.content, 'html.parser')

	results = soup.find(id="search_results") #subdivides html for easier parsing
	
	title_tags = results.select('div.search_name span.title') #pulls html for titles
	titles = [tt.get_text() for tt in title_tags] #pulls text from html
	titles_master.extend(titles) #appends list of titles from this page to the master list

	price_tags = results.select('div.search_price strike')
	prices = [pt.get_text() for pt in price_tags]
	prices_master.extend(prices)

	sale_tags = results.select('div.search_discount span')
	sales = [st.get_text() for st in sale_tags]
	sales_master.extend(sales)

	curPage = curPage+1

print '\nTitles: '
print  ' @'.join(titles_master).encode('utf-8') 
#	printing as a plain list causes weird formatting, using .join fixes this
#	.encode('utf-8') fixes errors from weird characters
#	'@' is used as a delimiter because some titles contain commas, dashes, etc
	
print '\nOriginal prices: \n', ' @'.join(prices_master)

print '\nDiscounts: \n', ' @'.join(sales_master)
	
