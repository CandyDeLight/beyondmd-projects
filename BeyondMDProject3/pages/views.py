from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import views
from . models import Reviews
import tmdb_api

def login_page(request):
    """
    this will be the landing page
    user can login with their username and password
    """
    if request.method == "GET":
        return render(request, 'login_page.html')
    if request.method == "POST":
        user_info = request.POST
        user = authenticate(request, username=user_info["username"], password=user_info["password"])
        if user is not None:
            # if the username and password matches, it'll login
            # logging in allow us to get the current logged in user info (id, username, email, etc)
            login(request, user)
            return redirect(index)
        else:
            # if the username/password is incorrect it'll simply redirect them back to the login page
            return redirect(login_page)

def signup_page(request):
    """
    if users have not signed up before they can do so here with their username and password
    """
    if request.method == "GET":
        return render(request, 'signup_page.html')
    if request.method == "POST":
        user_info = request.POST
        # create_user() will save the record into the database
        user = User.objects.create_user(username=user_info["username"], password=user_info["password"])
        return redirect(login_page)

@login_required
def index(request):
    """
    index is the homepage of the app after logging in, it will call the API and display the data
    """
    movie = tmdb_api.get_movie_info()
    return render(request, 'index.html', { "title": movie[0], "poster": movie[1], "release": movie[2] })

@login_required
def profile(request):
    """
    there is a profile component in which the user can view all the reviews they have left
    """
    if request.method == "GET":
        your_reviews = readReviewFromDatebase(request.user.id)
        if not your_reviews:
            # if the user have not left any reviews a message will be displayed to let the user know
            messages.add_message(request, messages.INFO, "You have not left any reviews yet.")
        return render(request, 'profile.html', { "reviews": your_reviews, "username": request.user.username })

@login_required
def settings(request):
    """
    the settings page allows the user to change their username and or password
    """
    if request.method == "GET":
        return render(request, 'settings.html', { "username": request.user.username })
    if request.method == "POST":
        user_info = request.POST
        if user_info["username"] is not "":
            update_username = User.objects.get(id=request.user.id)
            update_username.username = user_info["username"]
            update_username.save()
            # instead of rendering the same page, we will redirect the user back to settings page
            return redirect(settings)
        if user_info["password"] is not "":
            # it's possible to save passwords as plaintext (but very bad security practice)
            # since passwords should be hashed and not plaintext we will use set_password()
            update_password = User.objects.get(id=request.user.id)
            update_password.set_password(user_info["password"])
            update_password.save()
            # set_password() ends the current user session so I have to redirect user to login page
            return redirect(login_page)

@login_required
def addReviewToDatabase(request): #CREATE
    """
    we have the data using request.POST and are creating a record for reviews
    then save/add/insert/etc. that record into the database using django's .save()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make the specific request
        # to prevent an error we can make sure that if it is the specific request
        # execute the following code block if the specific request is correct
        user_review = request.POST
        add_review = Reviews(movie_title=user_review["title"], poster=user_review["poster"], rating=user_review["rating"], comment=user_review["comment"], user_id=request.user.id)
        add_review.save()
    # the return statement will always happen regardless of the method type
    return redirect(index)

def readReviewFromDatebase(id): #READ
    """
    query the database for all the reviews left by the current logged in user using django's .all()
    and .filter() then and convert the result to a list as this makes it easier to parse through
    """
    your_reviews = list(Reviews.objects.all().filter(user_id=id))
    # instead of getting all the reviews that was left which is what I had before
    # we can now access just the reviews left by the filtering the result
    # with the current logged in user using their id/username (I choose id)
    return your_reviews

@login_required
def updateReviewToDatabase(request): #UPDATE
    """
    query the database to first get the review that needs to be updated
    update said review with the new rating/comment
    then save the updated review back to the database using django's .save()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make the specific request
        # to prevent an error we can make sure that if it is the specific request
        # execute the following code block if the specific request is correct
        user_review = request.POST
        update_review = Reviews.objects.get(id=user_review["id"])
        update_review.rating = user_review["rating"]
        update_review.comment = user_review["comment"]
        update_review.save()
    # the return statement will always happen regardless of the method type
    return redirect(profile)

@login_required
def deleteReviewFromDatabase(request): #DELETE
    """
    query the database to first get the review that needs to be deleted
    then delete the review from the database using django's .delete()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make the specific request
        # to prevent an error we can make sure that if it is the specific request
        # execute the following code block if the specific request is correct
        user_review = request.POST
        delete_review = Reviews.objects.get(id=user_review["id"])
        delete_review.delete()
    # the return statement will always happen regardless of the method type
    return redirect(profile)

@login_required
def logout_action(request):
    """
    this function will simply end the current logged in user session
    and redirect them back to the login page
    """ 
    logout(request)
    return redirect(login_page)