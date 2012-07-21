from django.template.response import TemplateResponse, HttpResponse
from django.shortcuts import redirect
from django.core import serializers
from models import *
from hashing import hash_password
from valid import *
from users import get_user
from serialize import serialize_post
from time import time
from django.core.cache import cache

queried = None
key = 'posts'

def render_template(request, template, context={}):
    template = TemplateResponse(request, template, context=context)
    template.render()
    return template

def newpost(request):
    if request.method == 'GET':
        return render_template(request, 'newpost.html')
    elif request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']

        if subject and content:
            post = Post(subject=subject, content=content)
            post.save()
            cache.clear()
            return redirect('post/%d' % post.id)
        else:
            error = "Please enter both the title and body."
            context = {
                    'subject': subject,
                    'content': content,
                    'error': error}
            return render_template(request, 'newpost.html', context=context)

def allposts(request):
    global queried
    if key in cache:
        posts = cache.get(key)
    else:
        posts = get_all_posts()
        queried = time()
        cache.set(key, posts)

    params = {key: posts,
            'time': time() - queried}
    return render_template(request, 'home.html', context=params)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render_template(request, 'post.html', context=context)

def successful_login(request, user):
    r = redirect('/welcome')
    r.set_cookie('name', value='%s|%s' % (user.pk, user.hashed_pw))
    return r

def signup(request):
    signup_template = 'signup.html'

    if request.method == "GET":
        return render_template(request, signup_template)

    elif request.method == "POST":
        usr = request.POST['username']
        pw = request.POST['password']
        verify = request.POST['verify']
        email = request.POST['email']
        error_occurred = False
        c = {
                'usr': '',
                'usr_val': '',
                'email': '',
                'email_val': '',
                'pw': '',
                'pw_val': '',
                'verify': '',
                'verify_val': ''}
        if not valid_username(usr):
            c['usr'] = "This username is invalid."
            error_occurred = True
        else:
            c['usr_val'] = usr
        if not valid_email(email) and not email.strip() == "":
            c['email'] = "This email is invalid."
            error_occurred = True
        else:
            c['email_val'] = email
        if not valid_password(pw) :
            c['pw'] = "This password is inavlid."
            error_occurred = True
        else:
            c['pw_val'] = pw
        if verify != pw:
            c['verify'] = "These passwords do not match."
            error_occurred = True
        else:
            c['verify_val'] = verify
        if error_occurred:
            return render_template(request, signup_template, context=c)
        else:
            hashed = hash_password(pw)
            user = User(username=usr, hashed_pw=hashed[0], salt=hashed[1], email=email)
            user.save()
            return successful_login(request, user)            

def welcome(request):
    cookie = request.COOKIES['name']
    if cookie:
        user_id, cookie_hash = cookie.split('|')
        user = get_user(userid=user_id)
        if user and user.hashed_pw == cookie_hash:
            c = {'usr': user.username}
            return render_template(request, 'welcome.html', context=c)
    return redirect('/signup')

def login(request):
    if request.method == 'GET':
        return render_template(request, 'login.html')
    elif request.method == 'POST':
        usr = request.POST['username']
        pw = request.POST['password']
        user = get_user(username=usr)
        if user:
            hashed = hash_password(pw, salt=user.salt)[0]
            if hashed == user.hashed_pw:
                return successful_login(request, user)
        else:
            c = {'error': 'invalid login'}
            return render_template(request, 'login.html', context=c)


def logout(request):
    r = redirect('/signup')
    r.delete_cookie('name')
    return r


def post_json(request, post_id):
    post = Post.objects.get(pk=post_id)
    data = serialize_post(post)
    return HttpResponse(data, mimetype="application/json")

def all_json(request):
    posts = Post.objects.all()
    json_serializer = serializers.get_serializer("json")()
    data = json_serializer.serialize(posts, ensure_ascii=False)
    return HttpResponse(data, mimetype="application/json")
