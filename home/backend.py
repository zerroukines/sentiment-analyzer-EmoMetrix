from django.contrib.auth.backends import ModelBackend
from .models import MyUser

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return None
        if user.password == password:
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None
