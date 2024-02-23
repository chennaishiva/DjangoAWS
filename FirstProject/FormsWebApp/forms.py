from django import forms

class RegisterForms(forms.Form):
    Firstname = forms.CharField(max_length=20)
    Lastname = forms.CharField(max_length=20)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=12)
    Confirm_password = forms.CharField(max_length=12)

class UserForms(forms.Form):
    firstName = forms.CharField(max_length= 20, min_length=8)
    salary = forms.IntegerField()
    email = forms.EmailField()
    height = forms.DecimalField(max_digits=5, decimal_places=2)
    terms = forms.BooleanField()
    dob = forms.DateField(input_formats=["%y-%m-%d"])
    time = forms.TimeField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    hobbies = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('Books', 'Books'),
                                                 ('Cricket','cricket'),
                                                 ('football', 'football')])
    Resume = forms.FileField()
    password = forms.CharField(min_length=8, max_length=14, widget=forms.PasswordInput)
    websitelink = forms.URLField()
    picture = forms.ImageField()