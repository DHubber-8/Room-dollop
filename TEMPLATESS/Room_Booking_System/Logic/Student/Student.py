class Student(object):
    pass
def check_student_login(username, password):
    # This function only cares about student verification
    if username == 'student' and password == 'password123':
        return True
    return False



