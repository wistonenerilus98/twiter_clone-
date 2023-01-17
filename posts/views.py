from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    form = PostForm(request.POST, request.FILES)
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            
            # Redirect to Home
            return HttpResponseRedirect('/')
        
        else:   
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())
                         
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    
    # Show
    return render(request, 'posts.html',{'posts': posts, 'form': form})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    #to select or choose post
    like=Post.objects.get(id=post_id)
    like.likes +=1
    like.save()
    return HttpResponseRedirect('/')
    
def edit(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method=="GET":
        return render(request, "edit.html", {"post":post})
    if request.method=="POST":
        editposts=Post.objects.get(id=post_id)
        form=PostForm(request.POST,request.FILES,instance=editposts)
        if form.save():
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    
        
        
    