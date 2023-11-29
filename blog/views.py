from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *
# Create your views here.
def createBlog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category_name = request.POST.get('category')
        print(category_name in CATEGORIES)
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        draft = request.POST.get('draft')
        blog = BlogPost(
                author = request.user,
                title = title,
                image = image,
                category = category_name,
                summary = summary,
                content = content,
                is_draft = False
            )
        if draft:
            blog.is_draft = True
            blog.save()
            messages.success(request,"Blog Saved as Draft!!")
            return redirect('create-blog')
        else:
            blog.save()            
            messages.success(request,"Blog Uploaded!!")
            return redirect('create-blog')
    
    return render(request,'blog/create-blog.html')

def draftBlog(request):
    blog = BlogPost.get_draft_post(request.user)

    context = {
        'blog':blog
    }
    return render(request,'blog/draft-blog.html', context)


def updateDraftBlog(request):
    postId = request.POST.get('postId')
    action = request.POST.get('action')
    mark = request.POST.get('mark').capitalize()
    blog = BlogPost.objects.get(id = postId)
    if(action == "save"):
        blog.is_draft = not mark
        blog.save()
        
    return JsonResponse("Blog Updated!!", safe = False)


def BlogView(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    blog = BlogPost.objects.filter(is_draft = False)
    if q:
        blog = BlogPost.objects.filter(category__icontains = q)
    context = {
        'blog': blog
    }

    return render(request,'blog/blog.html', context)