import urllib.request
from bs4 import BeautifulSoup
class LeaderBoard:
	def __init__(self):
		self.position = []

	def scrape(self):
		with urllib.request.urlopen('https://www.codewars.com/users/leaderboard/') as response:
   			html = response.read()
   			soup = BeautifulSoup(html, 'html.parser')
   			print(soup.prettify())

leader_board = LeaderBoard()
leader_board.scrape()