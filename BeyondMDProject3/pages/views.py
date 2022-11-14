from django.shortcuts import render, redirect
from django.contrib import messages
from . import views
from . models import Reviews
import tmdb_api

def index(request):
    """
    index is the landpage, it will call the API and display the data
    """
    movie = tmdb_api.get_movie_info()
    return render(request, 'index.html', { "title": movie[0], "poster": movie[1], "release": movie[2] })

def profile(request):
    """
    there is a profile component in which you can view all the reviews you've left on movies
    """
    your_reviews = readFromDatebase()
    if not your_reviews:
        messages.add_message(request, messages.INFO, "You have not left any reviews yet.")
    return render(request, 'profile.html', { "reviews": your_reviews })

def addToDatabase(request): #CREATE
    """
    we have the data using request.POST and are creating a field/row for reviews
    then save/add/insert/etc. that field/row into the database using django's ORM .save()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make a POST request with the data needed
        user_review = request.POST
        add_review = Reviews(movie_title=user_review["title"], poster=user_review["poster"], rating=user_review["rating"], comment=user_review["comment"])
        add_review.save()
    # the return statement will always happen regardless if it is a POST or GET request
    return redirect(index)

def readFromDatebase(): #READ
    # query the database for all the reviews using django's ORM .all()
    # then and convert the result to a list as this makes it easier to parse through
    your_reviews = list(Reviews.objects.all())
    return your_reviews

def updateToDatabase(request): #UPDATE
    """
    query the database to first get the review that needs to be updated
    update said review with the new rating/comment
    then save the updated review back to the database using django's ORM .save()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make a POST request with the data needed
        review_id = request.POST["id"]
        update_review = Reviews.objects.get(id=review_id)
        update_review.rating = request.POST["rating"]
        update_review.comment = request.POST["comment"]
        update_review.save()
    # the return statement will always happen regardless if it is a POST or GET request
    return redirect(profile)

def deleteFromDatabase(request): #DELETE
    """
    query the database to first get the review that needs to be deleted
    then delete the review from the database using django's ORM .delete()
    """
    if request.method == "POST":
        # a user may find out this specific URL and doesn't make a POST request with the data needed
        review_id = request.POST["id"]
        delete_review = Reviews.objects.get(id=review_id)
        delete_review.delete()
    # the return statement will always happen regardless if it is a POST or GET request
    return redirect(profile)