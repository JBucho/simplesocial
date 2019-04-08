from django.views.generic import TemplateView
from django.shortcuts import render
from posts.models import Post

class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_user'] = "Visitor is able to sign up and create User \
                                  providing nick name (Display name), e-mail \
                                  address and password. There is no e-mail \
                                  veryfication (on purpose)."
        context['message_group'] = "Visitor is able to see groups list and posts in group. \
                            After logging in the user can create new group or \
                            join and leave existing one. Groups can be created \
                            due to content topic."
        context['message_posts'] = "Logged in user can create new post in specific group. \
                            Post will contain information about creation time and \
                            its author. The post author is able to delete it."
        return context

class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
