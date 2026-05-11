rooms = []

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