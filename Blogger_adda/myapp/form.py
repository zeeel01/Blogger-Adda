
from django.db.models.base import Model
from myapp.models import Blog, CommentBlog
from django import forms
from django.contrib.auth.forms import (UserCreationForm,AuthenticationForm,PasswordChangeForm)
from django.contrib.auth.models import User
from django.forms import ModelForm, fields, widgets

class BloggerRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}),label='Confirm Password')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control','placeholder':'abc_1'}),
        'email':forms.TextInput(attrs={'class':'form-control','placeholder':'abc@email.com'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'abc'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'xyz'})
        }
        labels={
            'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email'
            
        }

class BloggerLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}),label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter User Password'}),label='Password')
    class Meta:
        model = User
        fields = ['username','password']

class ChangeMyPass(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}),label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}),label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}),label='Re-enter Password')
    fields = ['old_password','new_password1','new_password2']

class UploadBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ['category','title','content','img']
        widgets={
           'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Write Subject'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Write blog here....'}),
            'img':forms.FileInput()
        }
        labels = {'author':'Author','title':'Subject','category':'Category','content':'Content','img':'Image for Blog'}


class CommentForm(forms.ModelForm):

    class Meta:
        model=CommentBlog
        fields=['new_comment']
        widgets={'new_comment':forms.Textarea(attrs={'class':'form-control col-lg-12','placeholder':'Write your comment...','rows':'3','style':'resize:none'})}
