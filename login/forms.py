from django import forms
from login.models import signup

class LoginForm(forms.Form):
   email = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      email = self.cleaned_data.get("email")
      user = signup.objects.filter(name = email)
      
      if not user:
         raise forms.ValidationError("User does not exist in our db!")
      return email