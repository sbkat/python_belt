from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "logreg_app/index.html")

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    request.session['email'] = request.POST['email']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dob=request.POST['dob'], email=request.POST['email'], password=hashed_pw)
        new_user.save()
        return redirect('/wishes')
    
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    else: 
        user_from_db = User.objects.get(email=request.POST['email_login'])
        logged_user = user_from_db
        if bcrypt.checkpw(request.POST['password_login'].encode(), logged_user.password.encode()):
            request.session['email'] = logged_user.email
            return redirect('/wishes')
        else:
            return redirect('/')

def success(request):
    if "email" not in request.session:
        return redirect('/')
    else:
        context = {
            "this_user": User.objects.get(email=request.session['email']),
            "all_wishes": Wishlist.objects.all(),
        }
        return render(request, "logreg_app/welcome.html", context)

def new_wish(request):
    context = {
            "this_user": User.objects.get(email=request.session['email'])
        }
    return render(request, "logreg_app/new_wish.html", context)

def adding_a_wish(request):
    errors = Wishlist.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='wish')
        return redirect('/wishes/new')
    else:
        this_user = User.objects.get(email=request.session['email'])
        new_wish = Wishlist.objects.create(item=request.POST['item'],description=request.POST['description'], wisher=this_user)
        return redirect('/wishes')

def cancel(request):
    return redirect('/wishes')

def remove_wish(request, wish_id):
    this_wish = Wishlist.objects.get(id=wish_id)
    this_wish.delete()
    return redirect('/wishes')

def edit_wish_page(request, wish_id):
    context = {
            "this_user": User.objects.get(email=request.session['email']),
            "this_wish": Wishlist.objects.get(id=wish_id),
    }
    return render(request, "logreg_app/edit_wish.html", context)

def editing_wish(request, wish_id):
    errors = Wishlist.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='wish')
        return redirect('/wishes/edit/' + wish_id)
    else:
        this_wish = Wishlist.objects.get(id=wish_id)
        this_wish.item = request.POST['item']
        this_wish.description = request.POST['description']
        this_wish.save()
        return redirect('/wishes')

def stats(request):
    context = {
            "this_user": User.objects.get(email=request.session['email']),
            "all_user": User.objects.all(),
            "all_wishes": Wishlist.objects.all(),
    }
    return render(request, "logreg_app/stats.html", context)

def grant_wish(request, wish_id):
    this_user = User.objects.get(email=request.session['email'])
    this_wish = Wishlist.objects.get(id=wish_id)
    this_wish.wishes_granted.add(this_user)
    this_wish.save()
    return redirect('/wishes')

def like_wish(request, wish_id):
    this_user = User.objects.get(email=request.session['email'])
    this_wish = Wishlist.objects.get(id=wish_id)
    this_wish.users_liked.add(this_user)
    this_wish.save()
    return redirect('/wishes')

def logout(request):
    request.session.clear()
    return redirect('/')
