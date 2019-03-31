from django.views.generic import TemplateView
from posts.models import Post

class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["latest_posts"] = Post.objects.all().order_by('-created_at')[:3]
        return context


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
