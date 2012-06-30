from django.template.response import TemplateResponse
from django.shortcuts import redirect
from models import get_all_posts, Post

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
            return redirect('post/' + str(post.id))
        else:
            error = "Please enter both the title and body."
            context = {
                    'subject': subject,
                    'content': content,
                    'error': error}
            return render_template(request, 'newpost.html', context=context)

def allposts(request):
    posts = get_all_posts()
    params = {'posts': posts}
    return render_template(request, 'home.html', context=params)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render_template(request, 'post.html', context=context)

