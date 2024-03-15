from django.shortcuts import render, redirect
from .models import User, Post
from .form import UserSignUpForm, UserSignInForm, PostForm, UpdatePost
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
# Create your views here.

def Main(request):
    return render(request, 'index.html' )

def dasboard(request):
    user_id = request.session.get('user_id')
    user_data = User.objects.get(id=user_id)
    post_data = Post.objects.filter(user=user_data)
    return render(request, 'dashboard.html', {'user': user_data, 'post_data':post_data})

def SignIn(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Check if a user with the provided email exists
            try:
                user = User.objects.get(email=email)
                
            except User.DoesNotExist:
                # User does not exist
                form.add_error(None, "Invalid email")
            else:
                # Now, you have the user object and can check the password
                print(password)
                print(user.password)
                if password == user.password:
                    # Password is correct
                    # Proceed with further actions
                    request.session['user_id'] = user.id # creating session
                    request.session['user_loggedin'] = True
                    return redirect("dashboard")  # Change "dashboard" to the URL name of your dashboard page
                    
                else:
                    # Password is incorrect
                    # Handle the case appropriately
                    form.add_error(None, "Invalid password.")
    else:
        form = UserSignInForm()
    return render(request, 'SignIn.html', {'form': form})

def SignUp(request):
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            member = User(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Save the new User object to the database
            member.save()
            return redirect("/")
        else:
            # Print form errors to check if there are any validation errors
            print(form.errors)
    else:
        form = UserSignUpForm()
    
    return render(request, 'SignUp.html', {'form': form})


def addPost(request, id):
    
    if request.method == 'POST':
        user = User.objects.get(id=id)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user  # Set the user field of the Post instance
            post.save()
            return redirect('dashboard')  # Redirect to success page or any other page
    else:
        form = PostForm()

    return render(request, 'addPost.html', {'form': form, 'id':id})

def deletePost(request, id):
    DeleteMember = Post.objects.get(id=id)
    DeleteMember.delete()
    return redirect("dashboard")

def Logout(request):

    if 'user_loggedin' in request.session:
        del request.session['user_loggedin']
        del request.session['user_id']
    return redirect("Main")

def updatePost(request, post_id):

    UpdateObj = Post.objects.get(id=post_id)

    if request.method == 'POST':

        form = UpdatePost(request.POST, instance=UpdateObj)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            print("Error") 
    else:
        form = UpdatePost(instance=UpdateObj)
    return render(request, 'updatePost.html', {'form': form, 'post_id': post_id})