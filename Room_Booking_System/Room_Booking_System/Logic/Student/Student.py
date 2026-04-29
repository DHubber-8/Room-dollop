class Student(object):
    def __init__(self):
        pass
    def check_student_login(self,username, password):
    # This function only cares about student verification
        if username == 'student' and password == 'password123':
            return True
        return False

    def get_available_rooms(self):
        # We moved your dummy database right here!
        return [
            {"id": 1, "name": "Lecture Hall B.1.1", "category": "Lecture Halls", "desc": "Capacity: 200 Pax"},
            {"id": 2, "name": "Computer Lab A.2.3", "category": "Computer Labs", "desc": "Capacity: 30 Pax"},
            {"id": 3, "name": "Study Room A.3.5", "category": "Study Rooms", "desc": "Capacity: 6 Pax"},
            {"id": 4, "name": "Lecture Hall B.1.2", "category": "Lecture Halls", "desc": "Capacity: 150 Pax"},
            {"id": 5, "name": "Computer Lab A.2.4", "category": "Computer Labs", "desc": "Capacity: 25 Pax"},
            {"id": 6, "name": "Meeting Room A.3.6", "category": "Multipurpose Halls", "desc": "Capacity: 20 Pax"}
        ]
        
    def get_current_bookings(self, username):
        return [
            {"id": "b1", "room_name": "Study Room A.3.4", "date": "15 Nov 2023", "time": "14:00 - 16:00", "status": "Confirmed"},
            {"id": "b2", "room_name": "Computer Lab A.2.4", "date": "18 Nov 2023", "time": "10:00 - 12:00", "status": "Confirmed"}
        ]

