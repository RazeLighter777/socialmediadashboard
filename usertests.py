import user
import unittest

testuser = "whitehouse"
testttuser = "papa_gut"
class TestUser(unittest.TestCase):
	def test_igFollower_count(self):
		user.User(testuser).getCurrentInstagramFollowers()
	def test_igUsername(self):
		self.assertEqual(user.User(testuser).getCurrentInstagramProfileName(),"The White House")
	def test_ttFollower_count(self):
		user.User(ttUsername=testttuser).getCurrentTikTokFollowers()
	def test_user_json(self):
		user.User(ttUsername=testttuser).getCurrentUserJSON()
if __name__== '__main__':
	unittest.main()
