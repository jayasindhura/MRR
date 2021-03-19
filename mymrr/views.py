from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse, HttpResponseRedirect, reverse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from mymrr.access_decorators_mixins import reviewer_access_required, staff_access_required


# Create your views here.
def staffSignup(request):
    if request.method == "GET":
        return render(request, "mymrr/staff_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_staff=True, role='staff'
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("mymrr:home_staff",))
        else:
            return render(
                request, "mymrr/staff_signup.html", {"errors": form.errors}
            )


def reviewerSignup(request):
    if request.method == "GET":
        return render(request, "mymrr/reviewer_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_reviewer=True, role="reviewer",
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("mymrr:home_reviewer",))
        else:
            return render(
                request, "mymrr/reviewer_signup.html", {"errors": form.errors}
            )


def reviewerLogin(request):
    if request.method == "GET":
        return render(request, "mymrr/reviewer_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "mymrr/reviewer_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_reviewer:
                    login(request, user)
                    return HttpResponseRedirect(reverse("mymrr:home_reviewer",))
                elif user.is_active and user.is_reviewer is False:
                    return render(
                        request,
                        "mymrr/reviewer_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Mentor"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "mymrr/reviewer_login.html", {"errors": form.errors})


def staffLogin(request):
    if request.method == "GET":
        return render(request, "mymrr/staff_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "mymrr/staff_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect(reverse("mymrr:home_staff",))
                elif user.is_active and user.is_reviewer is False:
                    return render(
                        request,
                        "mymrr/staff_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Staff"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "mymrr/staff_login.html", {"errors": form.errors})


def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'GET':
        return render(request, "mymrr/password_change_form.html", {"form": form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(
                request, "mymrr/password_change_done.html", {}
            )
        return render(
            request, "mymrr/password_change_form.html", {"errors": form.errors}
        )



def homepage(request):
    print('yessss')
    # return HttpResponse("test mymrr")
    return render(request, "mymrr/landing_page.html", {})
    #return render(request, "mymrr/home_reviewer.html", {})

# Create your views here.
now = timezone.now()
def home(request):
   return render(request, 'mymrr/home.html',
                 {'mymrr': home})

def home_reviewer(request):
   return render(request, 'mymrr/home_reviewer.html',
                 {'mymrr': home_reviewer})

def home_staff(request):
   return render(request, 'mymrr/home_staff.html',
                 {'mymrr': home_staff})

def user_logout(request):
    logout(request)
    return redirect(reverse("mymrr:homepage"))

@login_required
def reviewer_list(request):
    reviewer = Reviewers.objects.filter(created_date__lte=timezone.now())
    return render(request, 'mymrr/reviewer_list.html',
                 {'reviewers': reviewer})

@login_required
def reviewer_list_staff(request):
    reviewer = Reviewers.objects.filter(created_date__lte=timezone.now())
    return render(request, 'mymrr/reviewer_list_staff.html',
                 {'reviewers': reviewer})

@login_required
def reviewer_edit(request, pk):
   reviewer = get_object_or_404(Reviewers, pk=pk)
   if request.method == "POST":
       # update
       form = ReviewersForm(request.POST, instance=reviewer)
       if form.is_valid():
           reviewer = form.save(commit=False)
           reviewer.updated_date = timezone.now()
           reviewer.save()
           reviewer = Reviewers.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/reviewer_list.html',
                         {'reviewers': reviewer})
   else:
        # edit
       form = ReviewersForm(instance=reviewer)
   return render(request, 'mymrr/reviewer_edit.html', {'form': form})

@login_required
def reviewer_edit_staff(request, pk):
   reviewer = get_object_or_404(Reviewers, pk=pk)
   if request.method == "POST":
       # update
       form = ReviewersForm(request.POST, instance=reviewer)
       if form.is_valid():
           reviewer = form.save(commit=False)
           reviewer.updated_date = timezone.now()
           reviewer.save()
           reviewer = Reviewers.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/reviewer_list_staff.html',
                         {'reviewers': reviewer})
   else:
        # edit
       form = ReviewersForm(instance=reviewer)
   return render(request, 'mymrr/reviewer_edit_staff.html', {'form': form})


@login_required
def reviewer_delete(request, pk):
   reviewer = get_object_or_404(Reviewers, pk=pk)
   reviewer.delete()
   return redirect('mymrr:reviewer_list')

@login_required
def reviewer_delete_staff(request, pk):
   reviewer = get_object_or_404(Reviewers, pk=pk)
   reviewer.delete()
   return redirect('mymrr:reviewer_list_staff')

@login_required
def reviewer_new_staff(request):
   if request.method == "POST":
       form = ReviewersForm(request.POST)
       if form.is_valid():
           reviewer = form.save(commit=False)
           reviewer.created_date = timezone.now()
           reviewer.save()
           reviewers = Reviewers.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/reviewer_list_staff.html',
                         {'reviewers': reviewers})
   else:
       form = ReviewersForm()
       # print("Else")
   return render(request, 'mymrr/reviewer_new_staff.html', {'form': form})

@login_required
def movie_ratings_list(request):
   movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
   return render(request, 'mymrr/movie_ratings_list.html', {'movie_ratingss': movie_ratingss})

@login_required
def movie_ratings_list_staff(request):
   movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
   return render(request, 'mymrr/movie_ratings_list_staff.html', {'movie_ratingss': movie_ratingss})

@login_required
def movie_ratings_new(request):
   if request.method == "POST":
       form = Movie_RatingsForm(request.POST)
       if form.is_valid():
           movie_ratings = form.save(commit=False)
           movie_ratings.created_date = timezone.now()
           movie_ratings.save()
           movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_ratings_list.html',
                         {'movie_ratingss': movie_ratingss})
   else:
       form = Movie_RatingsForm()
       # print("Else")
   return render(request, 'mymrr/movie_ratings_new.html', {'form': form})

@login_required
def movie_ratings_new_staff(request):
   if request.method == "POST":
       form = Movie_RatingsForm(request.POST)
       if form.is_valid():
           movie_ratings = form.save(commit=False)
           movie_ratings.created_date = timezone.now()
           movie_ratings.save()
           movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_ratings_list_staff.html',
                         {'movie_ratingss': movie_ratingss})
   else:
       form = Movie_RatingsForm()
       # print("Else")
   return render(request, 'mymrr/movie_ratings_new_staff.html', {'form': form})

@login_required
def movie_ratings_edit(request, pk):
   movie_ratings = get_object_or_404(Movie_Ratings, pk=pk)
   if request.method == "POST":
       form = Movie_RatingsForm(request.POST, instance=movie_ratings)
       if form.is_valid():
           movie_ratings = form.save()
           # service.customer = service.id
           movie_ratings.updated_date = timezone.now()
           movie_ratings.save()
           movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_ratings_list.html', {'movie_ratingss': movie_ratingss})
   else:
       # print("else")
       form = Movie_RatingsForm(instance=movie_ratings)
   return render(request, 'mymrr/movie_ratings_edit.html', {'form': form})

@login_required
def movie_ratings_edit_staff(request, pk):
   movie_ratings = get_object_or_404(Movie_Ratings, pk=pk)
   if request.method == "POST":
       form = Movie_RatingsForm(request.POST, instance=movie_ratings)
       if form.is_valid():
           movie_ratings = form.save()
           # service.customer = service.id
           movie_ratings.updated_date = timezone.now()
           movie_ratings.save()
           movie_ratingss = Movie_Ratings.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_ratings_list_staff.html', {'movie_ratingss': movie_ratingss})
   else:
       # print("else")
       form = Movie_RatingsForm(instance=movie_ratings)
   return render(request, 'mymrr/movie_ratings_edit_staff.html', {'form': form})

@login_required
def movie_ratings_delete(request, pk):
   movie_ratings = get_object_or_404(Movie_Ratings, pk=pk)
   movie_ratings.delete()
   return redirect('mymrr:movie_ratings_list')

@login_required
def movie_ratings_delete_staff(request, pk):
   movie_ratings = get_object_or_404(Movie_Ratings, pk=pk)
   movie_ratings.delete()
   return redirect('mymrr:movie_ratings_list_staff')

@login_required
def movie_list(request):
   movies = Movie.objects.filter(created_date__lte=timezone.now())
   return render(request, 'mymrr/movie_list.html', {'movies': movies})

@login_required
def movie_list_staff(request):
   movies = Movie.objects.filter(created_date__lte=timezone.now())
   return render(request, 'mymrr/movie_list_staff.html', {'movies': movies})

@login_required
def movie_new(request):
   if request.method == "POST":
       form = MovieForm(request.POST)
       if form.is_valid():
           movie = form.save(commit=False)
           movie.created_date = timezone.now()
           movie.save()
           movies = Movie.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_list.html',
                         {'movies': movies})
   else:
       form = MovieForm()
       # print("Else")
   return render(request, 'mymrr/movie_new.html', {'form': form})

@login_required
def movie_new_staff(request):
   if request.method == "POST":
       form = MovieForm(request.POST)
       if form.is_valid():
           movie = form.save(commit=False)
           movie.created_date = timezone.now()
           movie.save()
           movies = Movie.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_list_staff.html',
                         {'movies': movies})
   else:
       form = MovieForm()
       # print("Else")
   return render(request, 'mymrr/movie_new_staff.html', {'form': form})

@login_required
def movie_edit(request, pk):
   movie = get_object_or_404(Movie, pk=pk)
   if request.method == "POST":
       form = MovieForm(request.POST, instance=movie)
       if form.is_valid():
           movie = form.save()
           # service.customer = service.id
           movie.updated_date = timezone.now()
           movie.save()
           movies = Movie.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_list.html', {'movies': movies})
   else:
       # print("else")
       form = MovieForm(instance=movie)
   return render(request, 'mymrr/movie_edit.html', {'form': form})

@login_required
def movie_edit_staff(request, pk):
   movie = get_object_or_404(Movie, pk=pk)
   if request.method == "POST":
       form = MovieForm(request.POST, instance=movie)
       if form.is_valid():
           movie = form.save()
           # service.customer = service.id
           movie.updated_date = timezone.now()
           movie.save()
           movies = Movie.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mymrr/movie_list_staff.html', {'movies': movies})
   else:
       # print("else")
       form = MovieForm(instance=movie)
   return render(request, 'mymrr/movie_edit_staff.html', {'form': form})

@login_required
def movie_delete(request, pk):
   movie = get_object_or_404(Movie, pk=pk)
   movie.delete()
   return redirect('mymrr:movie_list')

@login_required
def movie_delete_staff(request, pk):
   movie = get_object_or_404(Movie, pk=pk)
   movie.delete()
   return redirect('mymrr:movie_list_staff')



from django.http import HttpResponse
from django.views.generic import View
from mymrr.utils import render_to_pdf
from django.template.loader import get_template

def movie_ratings_summary_pdf(request):
    movie_ratingss = Movie_Ratings.objects.all()
    context = {'movie_ratingss': movie_ratingss,}
    template = get_template('mymrr/movie_ratings_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('mymrr/movie_ratings_summary_pdf.html', context)
    return pdf
