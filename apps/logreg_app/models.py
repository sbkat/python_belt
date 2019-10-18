from django.db import models
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        user_from_db = User.objects.filter(email=postData['email'])
        print('*******///////****')
        
        today = date.today()
        year = today.year
        update_year = int(year) - 13
        today = today.replace(year=update_year)
        
        if len(user_from_db) != 0:
            if postData['email'] == user_from_db[0].email:
                errors['email'] = "Email is already in database. Try again."
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be more than 2 characters."
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be more than 2 characters."
        if postData['dob'] == "":
            errors['dob'] = "Must enter a valid birthdate."
        if postData['dob'] > str(today):
            errors['dob'] = "Must be at least 13 years old to register."
        if len(postData['email']) < 5:
            errors['email'] = "Email is invalid."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match. Try again."
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user_from_db = User.objects.filter(email=postData['email_login'])

        if len(user_from_db) == 0:
            errors['email_login'] = "Email has not been registered."
        # if postData['password_login'] != user_from_db[0].password:
        #     errors['password_login'] = "Password does not match."
        if postData['email_login'] == '':
            errors['email_login'] = "Please enter an email address."
        if postData['password_login'] == '':
            errors['password_login'] = "Please enter a password."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishlistManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        if len(postData['item']) < 3 :
            errors['item'] = "A wish must consist of at least 3 characters"
        if len(postData['description']) < 1:
            errors['description'] = "A description must be provided!"
        return errors

class Wishlist(models.Model):
    wisher = models.ForeignKey(User, related_name="made_this_wish")
    wishes_granted = models.ManyToManyField(User, related_name="users_granted")
    users_liked = models.ManyToManyField(User, related_name="users_liked")
    item = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishlistManager()