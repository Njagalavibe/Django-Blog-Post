from urllib import request
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy 
from .models import Post, Like, Comment, Project
from .forms import CommentForm


# PUBLIC VIEWS
# Home page view
def home(request):
    """
    Home page with custom animations and unique menu design.
    No blog posts displayed - just artistic elements and navigation.
    """
    return render(request, 'home.html')

# Blogs views
def blogs_page(request):
    """Show all published blog posts with pagination"""
    # Get all published posts, ordered by most recent first
    posts_list = Post.objects.filter(status='published').order_by('-published_date')
    
    # Add pagination - 6 posts per page 
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        posts = paginator.page(paginator.num_pages)
    
    # Context dictionary with clear variable names
    context = {
        'posts': posts,           # Paginated posts
        'page_title': 'Blog',     # For <title> tag in template
        'current_page': 'blog',   # For navigation highlighting
    }
    
    return render(request, 'blogs_page.html', context)

# Single blog post view
def blog_detail(request, slug):
    """Show single blog post with navigation to next/previous posts"""
    
    # Get the current post - CRITICAL: Only published posts!
    post = get_object_or_404(
        Post, 
        slug=slug, 
        status='published'  # 👈 Security: prevents accessing unpublished posts
    )
    
    # Get next post (older than current)
    # Using .first() which returns None if no matches, so no try-except needed
    next_post = Post.objects.filter(
        status='published',
        published_date__lt=post.published_date  # Less than current date
    ).order_by('-published_date').first()  # Get the most recent one before current
    
    # Get previous post (newer than current)
    prev_post = Post.objects.filter(
        status='published',
        published_date__gt=post.published_date  # Greater than current date
    ).order_by('published_date').first()  # Get the oldest one after current
    
    # Note: i will implement Google Auth for likes/comments later
    # For now, i wil just pass the post data to the template
    # View counting, likes, and comments will be added after portfolio is populated
    
    # Context with all needed data for the template
    context = {
        'post': post,
        'next_post': next_post,  #  Next Post navigation
        'prev_post': prev_post,  # Previous Post navigation
        'page_title': post.title,  # Dynamic title based on post
        'current_page': 'blog',    # Keep blog navigation active
    }
    
    return render(request, 'blog_detail.html', context)


# Projects views
def projects_page(request):
    """Show all projects"""
    projects = Project.objects.all().order_by('-created_date')
    return render(request, 'projects_page.html', {'projects': projects})

# Single project view
def project_detail(request, slug):
    """Show single project"""
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

# About page view
def about(request):
    """About page"""
    return render(request, 'about.html')


#  INTERACTION VIEWS 
# TODO: Update these to use slug and user-based system
# Like/Dislike functionality
def like_blog_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Ensure session exists
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    # Check if user already reacted
    existing_like = Like.objects.filter(post=post, session_key=session_key).first()
    
    if existing_like:
        # If already liked, remove the like (toggle)
        if existing_like.reaction_type == 'like':
            existing_like.delete()
        else:
            # If was dislike, change to like
            existing_like.reaction_type = 'like'
            existing_like.save()
    else:
        # Create new like
        Like.objects.create(post=post, session_key=session_key, reaction_type='like')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def dislike_blog_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    existing_like = Like.objects.filter(post=post, session_key=session_key).first()
    
    if existing_like:
        if existing_like.reaction_type == 'dislike':
            existing_like.delete()
        else:
            existing_like.reaction_type = 'dislike'
            existing_like.save()
    else:
        Like.objects.create(post=post, session_key=session_key, reaction_type='dislike')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# ADMIN VIEWS
class BlogPostCreateView(CreateView):
    model = Post
    template_name = 'blog_post_new.html'
    fields = '__all__'

class BlogPostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_post_edit.html'
    fields = ['title', 'body']

class BlogPostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_post_delete.html'
    success_url = reverse_lazy('home')

