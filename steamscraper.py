
import requests
import sys
from bs4 import BeautifulSoup

pages = int(sys.argv[1])
curPage = 1

for page in range(1, pages+1):
	page = requests.get("http://store.steampowered.com/search/?specials=1&page=" + str(page))

	soup = BeautifulSoup(page.content, 'html.parser')

	results = soup.find(id="search_results")

	title_tags = results.select('div.search_name span.title')
	titles = [tt.get_text() for tt in title_tags]
	#titles

	price_tags = results.select('div.search_price strike')
	prices = [pt.get_text() for pt in price_tags]

	sale_tags = results.select('div.search_discount span')
	sales = [st.get_text() for st in sale_tags]

	print("\nPAGE " + str(curPage) + "------------------------------------------------------------------\n")
 
	print("\nTitles:")
	print(titles)

	print("\nOriginal prices:")
	print(prices)

	print("\nDiscounts:")
	print(sales)
	
	curPage = curPage+1
