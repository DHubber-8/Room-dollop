rooms = [
    {
        "room_id": 1,
        "name": "Lecture Hall B.1.1",
        "category": "Lecture Halls",
        "desc": "Large lecture hall with tiered seating, capacity 200. Equipped with projector and audio system.",
        "capacity": "200",
        "price": "50",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Lecture Hall B.1.1.jpg",
    },
    {
        "room_id": 2,
        "name": "Lecture Hall B.1.2",
        "category": "Lecture Halls",
        "desc": "Mid-size lecture hall with tiered seating, capacity 150. Equipped with projector and audio system.",
        "capacity": "150",
        "price": "40",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Lecture Hall B.1.2.jpg",
    },
    {
        "room_id": 3,
        "name": "Lecture Hall B.1.3",
        "category": "Lecture Halls",
        "desc": "Compact lecture hall with tiered seating, capacity 100. Equipped with projector and audio system.",
        "capacity": "100",
        "price": "30",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Lecture Hall B.1.3.jpg",
    },
    {
        "room_id": 4,
        "name": "Computer Lab A.2.3",
        "category": "Computer Labs",
        "desc": "Fully equipped computer lab with 30 PCs, high-speed internet, and printing facilities.",
        "capacity": "30",
        "price": "25",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Computer Lab A.2.3.jpg",
    },
    {
        "room_id": 5,
        "name": "Computer Lab A.2.4",
        "category": "Computer Labs",
        "desc": "Computer lab with 25 PCs, high-speed internet, and dual monitors at each station.",
        "capacity": "25",
        "price": "22",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Computer Lab A.2.4.jpg",
    },
    {
        "room_id": 6,
        "name": "Computer Lab A.2.5",
        "category": "Computer Labs",
        "desc": "Computer lab with 20 PCs and software suite for design and engineering applications.",
        "capacity": "20",
        "price": "20",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Computer Lab A.2.5.jpg",
    },
    {
        "room_id": 7,
        "name": "Multipurpose Hall A.3.6",
        "category": "Multipurpose Halls",
        "desc": "Spacious multipurpose hall suitable for events and presentations, capacity 250.",
        "capacity": "250",
        "price": "80",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Multipurpose Hall A.3.6.jpg",
    },
    {
        "room_id": 8,
        "name": "Multipurpose Hall B.1.7",
        "category": "Multipurpose Halls",
        "desc": "Large multipurpose hall for conferences and events, capacity 300. Full AV setup included.",
        "capacity": "300",
        "price": "100",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Multipurpose Hall B.1.7.jpg",
    },
    {
        "room_id": 9,
        "name": "Study Room C.3.4",
        "category": "Study Rooms",
        "desc": "Quiet study room with whiteboard, capacity 4. Ideal for small group sessions.",
        "capacity": "4",
        "price": "10",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Study Room C.3.4.jpg",
    },
    {
        "room_id": 10,
        "name": "Study Room C.3.5",
        "category": "Study Rooms",
        "desc": "Quiet study room with whiteboard and TV screen, capacity 6.",
        "capacity": "6",
        "price": "12",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Study Room C.3.5.jpg",
    },
    {
        "room_id": 11,
        "name": "Study Room C.3.6",
        "category": "Study Rooms",
        "desc": "Quiet study room with whiteboard and natural lighting, capacity 5.",
        "capacity": "5",
        "price": "10",
        "status": "Enabled",
        "selected_dates": "",
        "time_slots": "",
        "promotion_codes": "",
        "image": "PicturesRoom/Study Room C.3.6.jpg",
    },
]

next_room_id = 1


def create_room(room_data):
    global next_room_id

    room_data["room_id"] = next_room_id
    rooms.append(room_data)

    next_room_id += 1

    return room_data


def get_all_rooms():
    return rooms


def get_room_by_id(room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    return None


def update_room(room_id, updated_data):
    room = get_room_by_id(room_id)

    if room is None:
        return False

    room.update(updated_data)
    return True


def delete_room(room_id):
    room = get_room_by_id(room_id)

    if room is None:
        return False

    rooms.remove(room)
    return True


def get_room_by_id(room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room
    return None


def update_room(room_id, updated_data):
    for room in rooms:
        if room["room_id"] == room_id:
            room.update(updated_data)
            return True
    return False

def delete_room(room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            rooms.remove(room)
            return True
    return False