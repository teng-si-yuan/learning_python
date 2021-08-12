import unittest
from leader_board import LeaderBoard

class TestLeaderBoard(unittest.TestCase):

	def test_champion(self):
		leader_board = LeaderBoard()
		leader_board.scrape()
		self.assertEqual(leader_board.position[0].rank, '#1')
		self.assertEqual(leader_board.position[0].name, 'g964')
		self.assertEqual(leader_board.position[0].clan, 'None')

	def test_runner_up(self):
		leader_board = LeaderBoard()
		leader_board.scrape()
		self.assertEqual(leader_board.position[1].rank, '#2')
		self.assertEqual(leader_board.position[1].name, 'myjinxin2015')
		self.assertEqual(leader_board.position[1].clan, '中国 长垣')

	def test_number_500(self):
		leader_board = LeaderBoard()
		leader_board.scrape()
		self.assertEqual(leader_board.position[499].rank, '#500')
		self.assertEqual(leader_board.position[499].name, 'arithmetric')
		self.assertEqual(leader_board.position[499].clan, '')

	def test_counts(self):
		leader_board = LeaderBoard()
		leader_board.scrape()
		self.assertEqual(len(leader_board.position), 500)

if __name__ == '__main__':
	unittest.main()