from .models import Post

def get_latest_posts(request):
    context={}
    context["latest_posts"] = Post.objects.all().order_by('-created_at')[:3]
    return context
