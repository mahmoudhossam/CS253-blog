from models import User

def get_user(username=None, userid=None):
    try:
        if username:
            user = User.objects.get(username=username)
        else:
            user = User.objects.get(id=userid)
        return user
    except User.DoesNotExist:
        return None
    
