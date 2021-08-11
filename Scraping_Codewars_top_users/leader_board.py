import urllib.request
from bs4 import BeautifulSoup
class LeaderBoard:
	def __init__(self):
		self.position = []

	def scrape(self):
		with urllib.request.urlopen('https://www.codewars.com/users/leaderboard/') as response:
   			html = response.read()
   			soup = BeautifulSoup(html, 'html.parser')
   			rows = soup.find_all('tr')
   			# cells = rows[1].children[0].text
   			print(rows[1].get('data-username'))
   			print(rows[1])
   			for child in rows[1].children:
   				print(child.text)
 
leader_board = LeaderBoard()
leader_board.scrape()