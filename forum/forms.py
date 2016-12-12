from django.forms import ModelForm
from .models import ForumUser

class ForumUserForm(ModelForm):
    class Meta:
        model = ForumUser
        fields = ['user_name', 'password', 'email', 'nick']
