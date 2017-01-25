class train:
    def __init__(self,name = '',num = 0,arr_time = '',dep_time = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}
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
# class user:
# 	def __init__
def main():
	t1 = train('odisha',12345,'12:34','22:12','Wed',30,23,43)
	t2 = train('howrah',12565,'02:34','23:12','Mon',33,4,12)
	t3 = train('bangalore',22353,'11:56','03:12','Fri',33,24,77)
	train_dict = {t1.num:t1,t2.num:t2,t3.num:t3}
	train_dict.update({int(input("Enter the train number=")) : train(input("Enter the train name="),34353,'12:34','11:52','Wed',11,35,76)})
	print(train_dict[12565].name)


main()

