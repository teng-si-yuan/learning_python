import unittest
from ball import Ball

class TestBall(unittest.TestCase):

	def test_regular_ball(self):
		regular_ball = Ball()
		self.assertEqual(regular_ball.ball_type, 'regular')

	# def test_super_ball(self):
	# 	self.assertEqual(ball([1], 99), ([], [1]))

if __name__ == '__main__':
	unittest.main()