from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Post model
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    body = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    # Like/Dislike methods
    def get_like_count(self):
        """Returns total number of likes for this post"""
        return self.likes.filter(reaction_type='like').count()
    
    def get_dislike_count(self):
        """Returns total number of dislikes for this post"""
        return self.likes.filter(reaction_type='dislike').count()
    
    def get_user_reaction(self, user):
        """Check if user has reacted to this post"""
        if not user or not user.is_authenticated:
            return None
        try:
            like = self.likes.get(user=user)
            return like.reaction_type
        except Like.DoesNotExist:
            return None
    def has_user_reacted(self, user):
        """Check if user has already reacted"""
        return self.get_user_reaction(user) is not None
    
    # Comment methods
    def get_comment_count(self):
        """Returns total number of comments"""
        return self.comments.count()
    
    
    def get_recent_comments(self, limit=5):
        """Get most recent comments"""
        return self.comments.all().order_by('-created_date')[:limit]
    
    # Properties for easy template access
    @property
    def like_count(self):
        return self.get_like_count()
    
    @property
    def dislike_count(self):
        return self.get_dislike_count()
    
    @property
    def comment_count(self):
        return self.get_comment_count()


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    # Verification field
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.post.slug})

    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
       

# Like model
class Like(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=7, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']  # Ensure one reaction per user per post

    def __str__(self):
        return f"{self.reaction_type} on {self.post.title} by {self.user.username}"
    
# Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})