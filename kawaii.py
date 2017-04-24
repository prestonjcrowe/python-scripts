# Prints all image urls for a search querry on zerochan.net
# up to a given page limit. Requires bs4 and urllib.
# To view images in a slideshow, pipe results to feh:
# python kawaii.py | xargs feh -z -D30

from bs4 import BeautifulSoup
import urllib
pageLimit = 5
currentPage = 1
querry = 'sailor moon'
rootUrl = 'http://www.zerochan.net'
querryString = rootUrl + '/search?q=' + querry

r = urllib.urlopen(querryString).read()
soup = BeautifulSoup(r, 'html.parser')

while(currentPage < pageLimit):
	for link in soup.find_all('img'): 
		each = link.get('src') 

		print(each)
		#for images up to 600 x 600, try:
		#print(each.replace('.240.', '.600.', 1))

	currentPage+=1
	
	if(currentPage == 2):
		querryString += '&p=2'
	else:
		if currentPage <= 10:
			querryString = querryString[:-1]
			querryString += str(currentPage)
		else:
			querryString = querryString[:-2]
			querryString += str(currentPage)

	r = urllib.urlopen(querryString).read()
	soup = BeautifulSoup(r, 'html.parser')
	