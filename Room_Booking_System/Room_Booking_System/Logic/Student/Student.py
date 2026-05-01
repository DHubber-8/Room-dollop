class Student(object):
    def __init__(self):
        pass
    def check_student_login(self,username, password):
    # This function only cares about student verification
        if username == 'student' and password == 'password123':
            return True
        return False

    def get_available_rooms(self):
        return [
            {"id": 1, "name": "Lecture Hall B.1.1", "capacity": 200 , "block": "B"},
            {"id": 2, "name": "Computer Lab A.2.3", "capacity": 30 , "block": "A"},
            {"id": 3, "name": "Study Room C.3.5", "capacity": 6 , "block": "C"},
            {"id": 4, "name": "Lecture Hall B.1.2", "capacity": 150 , "block": "B"},
            {"id": 5, "name": "Computer Lab A.2.4", "capacity": 25 , "block": "A"},
            {"id": 6, "name": "Multipurpose Hall A.3.6", "capacity": 250 , "block": "A"},
            {"id": 7, "name": "Study Room C.3.4", "capacity": 4 , "block": "C"},
            {"id": 8, "name": "Lecture Hall B.1.3", "capacity": 100 , "block": "B"},
            {"id": 9, "name": "Computer Lab A.2.5", "capacity": 20 , "block": "A"},
            {"id": 10, "name": "Multipurpose Hall B.1.7", "capacity": 300, "block": "B"},
            {"id": 11, "name": "Study Room C.3.6", "capacity": 5, "block": "C"}
        ]
        
    def get_current_bookings(self, username):
        return [
            # Upcoming Bookings
            {"id": "b1", "room_name": "Study Room C.3.4", "date": "15 May 2026", "time": "14:30 - 15:30", "status": "Confirmed", "category": "upcoming"},
            {"id": "b2", "room_name": "Computer Lab A.2.4", "date": "18 June 2026", "time": "10:30 - 12:30", "status": "Confirmed", "category": "upcoming"},
            {"id": "b3", "room_name": "Lecture Hall B.1.2", "date": "20 June 2026", "time": "09:30 - 11:30", "status": "Confirmed", "category": "upcoming"},
            
            # Past Bookings
            {"id": "b4", "room_name": "Lecture Hall B.1.1", "date": "10 Jan 2026", "time": "08:30 - 10:30", "status": "Completed", "category": "past"},
            
            # Cancelled Booking
            {"id": "b5", "room_name": "Study Room C.3.5", "date": "25 May 2026", "time": "13:30 - 15:30", "status": "Cancelled", "category": "cancelled"}
        ]

