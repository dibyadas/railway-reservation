import pickle
class train:
    def __init__(self,name = '',num = 0,arr_time = '',dep_time = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0,fare_1ac = 0, fare_2ac = 0 ,fare_sl = 0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}
        self.fare = {'1AC' : fare_1ac,'2AC' : fare_2ac ,'SL' : fare_sl}
    def print_seat_availablity(self):
    	print("No. of seats available in 1AC :- "+str(seats['1AC']))
    	print("No. of seats available in 2AC :- "+str(seats['2AC']))
    	print("No. of seats available in SL :- "+str(seats['SL']))
    def check_availabilty(self,coach=''):
    	if coach == '':
    		print_seat_availablity()
    		coach = input("Enter the coach(1AC/2AC/SL) :-")
    	else:
    		if seats[coach] > 0:
    			return True
    		else:
    			return False
    def book_ticket(self,coach = '',no_of_tickets = 0):
    	seats[coach] -= no_of_tickets
    	return True


class user:
	def __init__(self,uid = 0,name = '',hometown = '',cell_num = '',pwd = '',acc_num = ''):
		self.uid = uid
		self.name = name
		self.hometown = ''
		self.cell_num = ''
		self.pwd = pwd
		self.acc_num = acc_num
		self.history = {}
	# def book_ticket(self.)


class ticket:
	def __init__(self,)


def book_ticket():
	uid = int(input("Enter your User ID = "))
	if uid in users:		
		print("Welcome ",users[uid].name," !")






t1 = train('odisha',12345,'12:34','22:12','Wed',30,23,43,2205,320,234)
t2 = train('howrah',12565,'02:34','23:12','Mon',33,4,12,3434,435,234)
t3 = train('bangalore',22353,'11:56','03:12','Fri',33,24,77,455,325,533)
trains = {t1.num:t1,t2.num:t2,t3.num:t3}
# trains.update({int(input("Enter the train number=")) : train(input("Enter the train name="),34353,'12:34','11:52','Wed',11,35,76)})
# print(train_dict[12565].name)
u1 = user(1212,'dibya das','cuttack','7478021777','dibyadas')
users={u1.uid : u1}

train_file = open("t.pkl",'wb')
user_file = open("u.pkl",'wb')
pickle.dump(trains,train_file)
pickle.dump(users,user_file)
train_file.close()
user_file.close()



print("--------------------------------------------------Welcome to Railway Reservation Portal----------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("Choose one of the following option:-")
print("1.Book Ticket")
print("2.Cancel Ticket")
print("3.Check PNR ")
print("4.Check seat availibity")
print("5.Administrator mode")
print("6.Create new account")
option = int(input("Option = "))
if option == 1:
	book_ticket()



#main()

