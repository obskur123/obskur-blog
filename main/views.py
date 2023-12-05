from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Image, Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpRequest
from nanoid import generate


@login_required(login_url='/blog/sign-in')
def posts(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, 'posts.html', {'posts': posts})


@login_required(login_url='/blog/sign-in')
def create_post(request: HttpRequest):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Post(title=title, body=body)
            post.save()

            for file in form.cleaned_data['files']:

                image = Image(file=file, post_id=post.id)

                image.save()

                print(image.file.url)

            return redirect('/blog/home')

    elif request.method == 'GET':
        return render(request, 'create_post.html', {'form': PostForm})


@login_required(login_url='/blog/sign-in')
def delete_post(request: HttpRequest, post_id: int):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        posts = Post.objects.all()
        return render(request, 'snippets/posts.html', {'posts': posts})


@login_required(login_url='/blog/sign-in')
def delete_comment(request: HttpRequest, comment_id):

    if request.method == 'DELETE':

        comment = get_object_or_404(Comment, id=comment_id)

        comment.delete()

        comments = Comment.objects.all()

        return render(request, 'snippets/comments.html', {'comments': comments})


@login_required(login_url='/blog/sign-in')
def sign_out(request: HttpRequest):
    logout(request)
    return redirect('/blog/sign-in')


@login_required(login_url='/blog/sign-in')
def toggle_archived(request: HttpRequest, post_id: int):

    post = get_object_or_404(Post, id=post_id)

    post.archived = not post.archived

    post.save()

    return render(request, 'snippets/toggle_archived_button.html', {'archived': post.archived, 'post_id': post.id})


def sign_in(request: HttpRequest):

    if request.user.is_authenticated:
        return redirect('/blog/home')

    if request.method == 'GET':
        return render(request, 'sign_in.html', {'form': AuthenticationForm})

    elif request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        print(form)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            print(user)

            if user is None:
                return render(request, 'sign_in.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect'})

            else:
                login(request, user)
                return redirect('/blog/home')
        else:
            print("not valid")
            return render(request, 'sign_in.html', {'form': AuthenticationForm, 'error': 'Username or password is incorrect'})


def add_comment(request: HttpRequest, post_id: int):
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            username = 'anon'
            admin = False

            if request.user.is_superuser:
                username = request.user.username
                admin = True

            comment = Comment(anon_user=username, admin=admin,
                              content=form.cleaned_data['content'], post_id=post_id)

            comment.save()

            comments = get_list_or_404(Comment.objects.filter(post_id=post_id))

            return render(request, 'snippets/comments.html', {'comments': comments})


def post(request: HttpRequest, post_id):

    p = get_object_or_404(Post, id=post_id)

    if p.archived and not request.user.is_superuser:
        return redirect('/blog/home')

    return render(request, 'post.html', {'post': p, 'form': CommentForm})


def home(request: HttpRequest):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'home.html', {'posts': posts})


def comments(request: HttpRequest, post_id: int):
    comments = get_list_or_404(Comment.objects.filter(post_id=post_id))
    return render(request, 'comments.html', {'comments': comments})
