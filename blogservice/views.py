from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Posts, Comments
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .forms import *


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blogservice/signup.html'


def index(request):
    pp = Posts.objects.all()
    for p in pp:
        if p.likes > 1000000:
            p.likes = str(p.likes//1000000)+'M'
        elif p.likes > 1000:
            p.likes = str(p.likes//1000)+'K'
        elif p.views > 1000:
            p.views = str(p.views//1000)+'K'
        elif p.views > 1000000:
            p.views = str(p.views//1000000)+'M'

    post = Posts.objects.get(pk=1)
    print(post.likes)
    return render(request, "blogservice/index.html", {"posts": pp})


def about(request):
    return render(request, "blogservice/about.html")


def show_post(request, id):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        post = Comments(
            author_id=request.user.id,
            post_id=form.data['post_id'],
            text=form.data['text'],
            likes=0,
        )
        post.save()
        return redirect("home")
    else:
        form = AddCommentForm()
        post = Posts.objects.get(id=id)
        comments = Comments.objects.filter(post_id=id)
        return render(request, "blogservice/post.html", {'post': post, 'form': form, 'comments':comments})


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        post = Posts(
            user_id=request.user.id,
            description=form.data['description'],
            text=form.data['text'],
            likes=0,
            views=0
        )
        post.save()
        return redirect("home")
    else:
        form = AddPostForm()
        return render(request, "blogservice/addpost.html", {'form': form})


def likes(request):
    print("ok")
    return(request)

def comments(request,id):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        post = Comments(
            author_id=request.user.id,
            post_id=form.data['post_id'],
            text=form.data['text'],
            likes=0,
        )
        post.save()
        return redirect("home")
    else:
        form = AddCommentForm()
        post = Comments.objects.get(id=id)
        return render(request, "blogservice/post.html", {'post': post, 'form': form})

'''def sign_up(request):
    if request.method == "POST":
        user = Users()
        user.email = request.POST.get("email")
        user.login = request.POST.get("login")
        user.password = request.POST.get("password")
        user.save()
        print(user.login)
        return HttpResponseRedirect('/')
    else:
        return render(request, "blogservice/reg.html")'''


'''def sign_in(request):
    if request.method == 'POST':
        old_email = request.POST['email']
        old_password = request.POST['password']
        user = Users.objects.filter(mail=old_email)
        if user[0].password == old_password:
            return redirect(index)
        else:
            HttpResponseRedirect('/')
        return redirect(index)'''

