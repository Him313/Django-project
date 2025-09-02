from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post


#to tell decorator where to redirect us when we are not logged in
@login_required(login_url="/login")
# Create your views here.
def home(request):
    posts = Post.objects.all()

    if request.method == "DELETE":    ### this will delete the post
        post_id = request.DELETE.get("post-id")
        print(post_id)
    return render(request, 'main/home.html', {"posts": posts}) 


## Test to check if an updation has been made
## or not
@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")   # ✅ always returns on success
        else:
            # form invalid → show errors
            return render(request, "main/create_post.html", {"form": form})
    else:
        # GET request → show empty form
        form = PostForm()
        return render(request, "main/create_post.html", {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid(): # check if form is valid or not
            user=form.save() 
            login(request, user) ## to create new use and login as per the form
            return redirect("/home")
    
    else:
        form= RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})



def logout_view(request):
    logout(request)   # clears the session
    return redirect("/login")  # redirect wherever you want