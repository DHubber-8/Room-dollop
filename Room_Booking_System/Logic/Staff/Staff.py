class Staff(object):
    pass

    def check_staff_login(self, username, password):
    # This function only cares about staff verification
        if username == 'staff' and password == 'password123':
            return True
        return False

    def get_all_rooms(self):
        return [
            {"id": 1, "name": "Lecture Hall B.1.1", "category": "Lecture Halls", "desc": "Large seating, capacity 200"},
            {"id": 2, "name": "Computer Lab A.2.3", "category": "Computer Labs", "desc": "Equipped with 30 PCs"},
            {"id": 3, "name": "Study Room A.3.5", "category": "Study Rooms", "desc": "Small room, capacity 5"}
        ]




