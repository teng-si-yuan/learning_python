import unittest
from leader_board import LeaderBoard

class TestLeaderBoard(unittest.TestCase):

	def test_counts(self):
		leader_board = LeaderBoard()
		leader_board.scrape()
		self.assertEqual(len(leader_board.position), 500)

if __name__ == '__main__':
	unittest.main()