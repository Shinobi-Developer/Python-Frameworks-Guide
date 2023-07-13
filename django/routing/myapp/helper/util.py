from firstapp.models import Users

def isRepeated(username, email):
    repeatedUser = Users.objects.filter(email = email, username = username).first()
    
    if repeatedUser is None:
        return False
    else:
        return True