from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.

def main(request):
    title = "CRUD"  
    crud_post = Post.objects.get(title=title)
    
def create():
    Post.objects.create(title="Заголовок нового поста", text="Текст нового поста")
    post = Post.objects.get(title="Заголовок нового поста")
    print(post.title)
def edit(): 
    post = Post.objects.get(title="Заголовок нового поста")
    post.title = "От чего вымерли динозавры?"
    post.save()
    
def delete():
    post = Post.objects.get(title="Новый заголовок")
    post.delete() 

    all_posts = Post.objects.all()
    all_posts.delete()  
    
def home (request):
    return HttpResponse('Home page')
            