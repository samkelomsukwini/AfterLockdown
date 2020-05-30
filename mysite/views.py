from django.shortcuts import render

from afterlockdown.views import get_posts
from logistics.models import OperatingSystem


def index(request):
    '''
    App entrypoint. Presents user with all `Post` objects
    '''
    # Gets all post objects in DB
    posts = get_posts(request)
    
    # Get divice operating system from meta data
    os = request.META['OS']

    # Try/Catch checks if Operating System is in DB
    # raises exception if not. It assumes OS is desktop
    # if it is not in the DB
    try:
        OperatingSystem.objects.filter(name__icontains=os).first()
        is_mobile = True
    
    except:
        is_mobile = False

    context = {
        'is_mobile': is_mobile,
        'posts': posts
    }
    return render(request, 'index.html', context)