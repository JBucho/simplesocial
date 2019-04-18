from .models import Post
from django.db.models import Count

def get_latest_posts(request):
    context={}
    context["latest_posts"] = Post.objects.all().order_by('-created_at')[:3]
    return context

def get_popular_posts(request):
    context={}
    context['popular_posts'] = Post.objects.all() \
                                   .annotate(comments_count=Count('comments')) \
                                   .order_by('-comments_count')[:3]
    return context
