import urllib.request
class LeaderBoard:
	def __init__(self):
		self.position = []

	def scrape(self):
		with urllib.request.urlopen('https://www.codewars.com/users/leaderboard/') as response:
   			html = response.read()
   			print(html)

leader_board = LeaderBoard()
leader_board.scrape()