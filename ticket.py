import random
class ticket:
	def __init__(self,train,user,ticket_num):
		self.pnr = str(train.num)+str(user.uid)+str(random.randint(100,999))
		self.train_name = train.name
		self.user_name = user.name
		self.ticket_num = ticket_num
		user.history.update({self.pnr : self})
		ticket_dict.update({self.pnr : self})
		
from reserv import *
