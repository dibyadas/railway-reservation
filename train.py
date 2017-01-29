class train:
    def __init__(self,name = '', num = 0, arr_time = '',dep_time = '',src = '' ,des = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0,fare_1ac = 0, fare_2ac = 0 ,fare_sl = 0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.src = src
        self.des = des
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}
        self.fare = {'1AC' : fare_1ac,'2AC' : fare_2ac ,'SL' : fare_sl}
    def print_seat_availablity(self):
    	print("No. of seats available in 1AC :- "+str(self.seats['1AC']))
    	print("No. of seats available in 2AC :- "+str(self.seats['2AC']))
    	print("No. of seats available in SL :- "+str(self.seats['SL']))
    def check_availabilty(self,coach='',ticket_num = 0):
    	coach = coach.upper()
    	if coach not in ('SL','1AC','2AC'):
    		print_seat_availablity()
    		coach = input("Enter the coach(1AC/2AC/SL) :-")
    	else:
    		if self.seats[coach] == 0:
    			return False
    		elif self.seats[coach] >= ticket_num:
    			return True
    		else:
    			return False
    def book_ticket(self,coach = '',no_of_tickets = 0):
    	self.seats[coach] -= no_of_tickets
    	return True
