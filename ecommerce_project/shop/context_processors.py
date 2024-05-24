from .models import CATEGORY


def menu_link(request):
    links = CATEGORY.objects.all()
    return dict(links=links)
