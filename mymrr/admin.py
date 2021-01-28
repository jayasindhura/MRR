from django.contrib import admin
from .models import User,Reviewers_Age_Range,Reviewers_Occupation,Reviewer_Gender,Reviewers,Movie_Category,Movie,Rating_Scale,Movie_Ratings

# Register your models here.
class UserList(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_reviewer')
    list_filter = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_reviewer')
    search_fields = ('first_name','last_name', 'email','username','is_active','created_on','role','is_staff','is_reviewer')
    ordering = ['first_name']

class ReviewersAgeRangeList(admin.ModelAdmin):
    list_display = ['Age_Range']
    list_filter = ['Age_Range']
    search_fields = ['Age_Range']
    ordering = ['Age_Range']

class ReviewersOccupationList(admin.ModelAdmin):
    list_display = ['Occupation']
    list_filter = ['Occupation']
    search_fields = ['Occupation']
    ordering = ['Occupation']

class ReviewerGenderList(admin.ModelAdmin):
    list_display = ['Reviewer_Gender']
    list_filter = ['Reviewer_Gender']
    search_fields = ['Reviewer_Gender']
    ordering = ['Reviewer_Gender']

class ReviewersList(admin.ModelAdmin):
    list_display = ('Reviewer_ID','Reviewer_First_Name', 'Reviewer_Last_Name','Reviewer_Gender','Reviewer_Age_Range','Reviewer_Occupation')
    list_filter = ('Reviewer_ID','Reviewer_First_Name', 'Reviewer_Last_Name','Reviewer_Gender','Reviewer_Age_Range','Reviewer_Occupation')
    search_fields = ('Reviewer_ID','Reviewer_First_Name', 'Reviewer_Last_Name','Reviewer_Gender','Reviewer_Age_Range','Reviewer_Occupation')
    ordering = ['Reviewer_ID']

class MovieCategoryList(admin.ModelAdmin):
    list_display = ['Category_Name']
    list_filter = ['Category_Name']
    search_fields = ['Category_Name']
    ordering = ['Category_Name']

class MovieList(admin.ModelAdmin):
    list_display = ('Movie_Title','Movie_Year','Category_Name')
    list_filter = ('Movie_Title','Movie_Year','Category_Name')
    search_fields = ('Movie_Title','Movie_Year','Category_Name')
    ordering = ['Movie_Title']

class RatingScaleList(admin.ModelAdmin):
    list_display = ['Ratings']
    list_filter = ['Ratings']
    search_fields = ['Ratings']
    ordering = ['Ratings']



class MovieRatingsList(admin.ModelAdmin):
    list_display = ('Movie_Title', 'Reviewer_ID','Reviewer_Age_Range','Reviewer_Occupation','Rating','Review')
    list_filter = ('Movie_Title', 'Reviewer_ID','Reviewer_Age_Range','Reviewer_Occupation','Rating','Review')
    search_fields = ('Movie_Title', 'Reviewer_ID','Reviewer_Age_Range','Reviewer_Occupation','Rating','Review')
    ordering = ['Movie_Title']

admin.site.register(User,UserList)
admin.site.register(Reviewers_Age_Range,ReviewersAgeRangeList)
admin.site.register(Reviewers_Occupation,ReviewersOccupationList)
admin.site.register(Reviewer_Gender,ReviewerGenderList)
admin.site.register(Reviewers,ReviewersList)
admin.site.register(Movie_Category,MovieCategoryList)
admin.site.register(Movie,MovieList)
admin.site.register(Rating_Scale,RatingScaleList)
admin.site.register(Movie_Ratings,MovieRatingsList)
