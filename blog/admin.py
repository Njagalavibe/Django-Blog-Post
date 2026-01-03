from django.contrib import admin

from .models import Post, Like, Comment, Project


# Register Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'published_date']
    list_filter = ['status', 'published_date', 'author']
    search_fields = ['title', 'body', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_date']
    list_filter = ['created_date', 'user']
    search_fields = ['content', 'user__username'] 

    
# Register Like model with custom admin
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'reaction_type', 'created_at']
    list_filter = ['reaction_type', 'created_at']
    search_fields = ['post__title', 'user__username']

# Register Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']