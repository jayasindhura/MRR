from django import forms
from .models import Reviewers,Movie_Ratings,Movie
from .models import User
from django.forms.widgets import DateInput,DateTimeInput

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email).first()
        if user:
            if user.is_staff:
                user_role = "Staff"

            else:
                user_role = "Reviewers"
            raise forms.ValidationError(
                "{} with this email already exists, use another email.".format(
                    user_role
                )
            )
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Password should be minimum 6 characters long")

        if password != self.data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
        return password

class ReviewersForm(forms.ModelForm):
    class Meta:
        model = Reviewers
        fields = ('Reviewer_ID','Reviewer_First_Name', 'Reviewer_Last_Name','Reviewer_Gender','Reviewer_Age_Range','Reviewer_Occupation',  'Reviewer_City', 'Reviewer_State','Reviewer_Zipcode','Reviewer_Email','Reviewer_Phone')

class Movie_RatingsForm(forms.ModelForm):
   class Meta:
       model = Movie_Ratings
       fields = ('Movie_Title', 'Reviewer_ID', 'Reviewer_Age_Range', 'Reviewer_Occupation', 'Rating','created_date','Review', )
       widgets = {
           'created_date': DateInput(attrs={'type': 'date'}),
       }

class MovieForm(forms.ModelForm):
   class Meta:
       model = Movie
       fields = ('Movie_Title', 'Movie_Year', 'Category_Name')