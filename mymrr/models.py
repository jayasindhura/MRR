from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, UserManager
from mymrr.utils import ROLES


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=50)
    is_staff = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name if full_name else self.email

    @property
    def full_name(self):
        return self.get_full_name()


class Reviewers_Age_Range(models.Model):
    Age_Range = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Age_Range)

class Reviewers_Occupation(models.Model):
    Occupation = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Occupation)

class Reviewer_Gender(models.Model):
    Reviewer_Gender = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Reviewer_Gender)

class Reviewers(models.Model):
    Reviewer_ID = models.CharField(max_length=100)
    Reviewer_First_Name = models.CharField(max_length=100)
    Reviewer_Last_Name = models.CharField(max_length=100)
    Reviewer_Gender = models.ForeignKey(Reviewer_Gender, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_Age_Range = models.ForeignKey(Reviewers_Age_Range, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_Occupation = models.ForeignKey(Reviewers_Occupation, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_City = models.CharField(max_length=50)
    Reviewer_State = models.CharField(max_length=50)
    Reviewer_Email = models.EmailField(max_length=100)
    Reviewer_Phone = models.CharField(max_length=50)
    Reviewer_Zipcode = models.CharField(max_length=50)
    #Book_count = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Reviewer_ID)

class Movie_Category(models.Model):
    Category_Name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Category_Name)

class Movie(models.Model):
    Movie_Title = models.CharField(max_length=100)
    Movie_Year = models.CharField(max_length=100)
    Category_Name = models.ForeignKey(Movie_Category, on_delete=models.CASCADE, default='', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Movie_Title)

class Rating_Scale(models.Model):
    Ratings = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Ratings)

class Movie_Ratings(models.Model):
    Movie_Title = models.ForeignKey(Movie, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_ID = models.ForeignKey(Reviewers, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_Age_Range = models.ForeignKey(Reviewers_Age_Range, on_delete=models.CASCADE, default='', blank=True, null=True)
    Reviewer_Occupation = models.ForeignKey(Reviewers_Occupation, on_delete=models.CASCADE, default='', blank=True, null=True)
    Rating = models.ForeignKey(Rating_Scale, on_delete=models.CASCADE, default='', blank=True, null=True)
    Review = models.TextField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Movie_Title)


