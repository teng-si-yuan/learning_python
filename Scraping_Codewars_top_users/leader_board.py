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
			name = rows[1].get('data-username')
			for child in rows[1].children:
				if child.text.startswith("#"):
					rank = child.text
					continue
				if child.text.count(",") > 0:
					honor = child.text
					continue
				if child.text.count("kyu") == 0 and child.text.count("dan") == 0:
					clan = child.text
			print(name)
			print(rank)
			print(honor)
			print(clan)
 
leader_board = LeaderBoard()
leader_board.scrape()