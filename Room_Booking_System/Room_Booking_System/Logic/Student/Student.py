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
            {"id": 1, "name": "Lecture Hall B.1.1", "category": "Lecture Halls", "time": "09:00AM - 10:00AM", "desc": "Large seating, capacity 200"},
            {"id": 2, "name": "Computer Lab A.2.3", "category": "Computer Labs", "time": "10:00AM - 11:00AM", "desc": "Equipped with 30 PCs"},
            {"id": 3, "name": "Study Room A.3.5", "category": "Study Rooms", "time": "11:00AM - 12:00PM", "desc": "Small room, capacity 5"},
            {"id": 4, "name": "Lecture Hall B.1.2", "category": "Lecture Halls", "time": "01:00PM - 02:00PM", "desc": "Medium seating, capacity 100"},
            {"id": 5, "name": "Computer Lab A.2.4", "category": "Computer Labs", "time": "02:00PM - 03:00PM", "desc": "Equipped with 20 PCs"},
            {"id": 6, "name": "Meeting Room A.3.6", "category": "Multipurpose Halls", "time": "03:00PM - 04:00PM", "desc": "Medium room, capacity 10"}
        ]

