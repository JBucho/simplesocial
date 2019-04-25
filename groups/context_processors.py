from .models import Group
from django.db.models import Count


def get_popular_groups(request):
    context = {}
    context["popular_groups"] = (
        Group.objects.all()
        .annotate(members_count=Count("members"))
        .order_by("-members_count")[:3]
    )
    return context
