from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Posts, Comments


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form'}),
            'email': forms.TextInput(attrs={'class': 'form'})
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('description','text')

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)