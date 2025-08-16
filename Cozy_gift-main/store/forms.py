from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile
class UserInfoForm(forms.ModelForm):
  phone = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),required=False)
  address1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address 1'}),required=True)
  address2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address 2'}),required=False)
  city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),required=True)
  state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),required=True)
  zipcode = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),required=True)
  country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),required=True)
	
  class Meta:
    model = Profile
    fields = ('phone','address1','address2','city','state','zipcode','country')
	
# class ChangePasswordForm(SetPasswordForm):
# 	class Meta:
# 		model = User
# 		field = ['new_password1','new_password2']
# 	def __init__(self, *args, **kwargs):
# 			super(ChangePasswordForm, self).__init__(*args, **kwargs)

# 			self.fields['new_password1'].widget.attrs['class'] = 'form-control'
# 			self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
# 			self.fields['new_password1'].label = ''
# 			self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 			self.fields['new_password2'].widget.attrs['class'] = 'form-control'
# 			self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 			self.fields['new_password2'].label = ''
# 			self.fields['new_password2'].help_text = '<br/><span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = (
            '<small>Password should be at least 6 characters. No complex rules required.</small>'
        )

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = (
            '<br/><span class="form-text text-muted"><small>Re-enter the password for verification.</small></span>'
        )

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 6:
            raise ValidationError("Password must be at least 6 characters.")
        return password1

    def clean_new_password2(self):
        password2 = self.cleaned_data.get('new_password2')
        if password2 != self.cleaned_data.get('new_password1'):
            raise ValidationError("The two password fields must match.")
        return password2
    
class UpdateUserForm(UserChangeForm):
	password = None
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),required=False)

	class Meta:
			model = User
			fields = ('username', 'first_name', 'last_name','email')

	def __init__(self, *args, **kwargs):
			super(UpdateUserForm, self).__init__(*args, **kwargs)

			self.fields['username'].widget.attrs['class'] = 'form-control'
			self.fields['username'].widget.attrs['placeholder'] = 'User Name'
			self.fields['username'].label = ''
			self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(
#         label="", 
#         widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
#         required=True  # Email is not optional
#     )
#     first_name = forms.CharField(
#         label="", 
#         max_length=100, 
#         widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
#         required=True  # First name is not optional
#     )
#     last_name = forms.CharField(
#         label="", 
#         max_length=100, 
#         widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
#         required=False  # Last name is now optional
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['placeholder'] = 'User Name'
#         self.fields['username'].label = ''
#         self.fields['username'].help_text = '<small>Up to 150 characters. Letters, digits, and @/./+/-/_ only.</small>'

#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password1'].label = ''
#         self.fields['password1'].help_text = (
#             '<small>At least 8 characters. Avoid common passwords and personal info.</small>'
#         )

#         self.fields['password2'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['password2'].label = ''
#         self.fields['password2'].help_text = '<small>Re-enter the password for verification.</small>'
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
        required=False  # Email is now optional
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
        required=False  # First name is now optional
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
        required=False  # Last name is optional
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<small>Up to 150 characters. Letters, digits, and @/./+/-/_ only.</small>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<small>Password length can be reduced (e.g., 6+ characters). Avoid common passwords.</small>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<small>Re-enter the password for verification.</small>'

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 6:  # Minimum length can be 6 characters
            raise ValidationError("Password must be at least 6 characters.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if password2 != self.cleaned_data.get('password1'):
            raise ValidationError("The two password fields must match.")
        return password2
