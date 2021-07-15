import unittest
from ball import Ball

class TestBall(unittest.TestCase):

	def test_regular_ball(self):
		regular_ball = Ball()
		self.assertEqual(regular_ball.ball_type, 'regular')

	def test_super_ball(self):
		super_ball = Ball('super')
		self.assertEqual(super_ball.ball_type, 'super')

if __name__ == '__main__':
	unittest.main()