class Staff(object):
    pass
def check_staff_login(username, password):
    # This function only cares about staff verification
    if username == 'staff' and password == 'password123':
        return True
    return False




