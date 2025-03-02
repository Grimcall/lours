from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class PasswordOnlyBackend(BaseBackend):
    def authenticate(self, request, password=None, **kwargs):
        if not password:
            return None
            
        # Check all users for matching password
        for user in User.objects.all():
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
