import instaloader
import uuid
from TikTokApi import TikTokApi
class User:
	igUsername = ""
	ttUsername = ""
	igProfile = None
	ttApi = None
	igLoader = None
	ttUserProfile = None
	userUUID = None
	igFollowingGraph = []
	#Creates a new user with the following usernames accross platforms.
	def __init__(self, igUsername=None, ttUsername=None):
		self.userUUID = uuid.uuid4()
		if igUsername:
			self.igUsername = igUsername
			self.igLoader =  instaloader.Instaloader()
			self.igProfile = instaloader.Profile.from_username(self.igLoader.context, igUsername)
		if ttUsername:
			self.ttApi = TikTokApi.get_instance()
			self.ttUsername = ttUsername
			self.ttUserProfile = self.ttApi.getUser(ttUsername)["userInfo"]
		
	def hasInstagram(self):
		return self.igUsername != None
	def hasTikTok(self):
		return self.ttUsername != None
	#Updates the following count graph. 
	def getCurrentInstagramFollowers(self):
		self.updateInstagramProfile()
		return self.igProfile.followers
	#Gets the number of followees
	def getCurrentInstagramFollowees(self):
		return self.igProfile.followees
	#Gets current profile name
	def getCurrentInstagramProfileName(self):
		return self.igProfile.full_name
	def updateInstagramProfile(self):
		self.igProfile = instaloader.Profile.from_username(self.igLoader.context, self.igUsername)
	def updateTikTokProfile(self):
		self.ttUserProfile = self.ttApi.getUser(self.ttUsername)["userInfo"]
	def getCurrentTikTokFollowers(self):
		self.updateTikTokProfile()
		return self.ttUserProfile["stats"]["followerCount"]
	def getCurrentUserJSON(self):
		return {
				"uuid" : str(self.userUUID),
				"ttUsername" :self.ttUsername,
				"igUsername" : self.igUsername
		}

