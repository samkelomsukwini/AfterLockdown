from django.contrib import messages

from django.shortcuts import redirect, render

from afterlockdown.views import create_submission, get_posts
from afterlockdown.forms import PostSubmitForm

from logistics.models import OperatingSystem


def index(request):
    '''
    App entrypoint. Presents user with all `Post` objects
    '''
    if request.method == 'POST':
        submission_form = PostSubmitForm(request.POST)

        # Pass form and request to create_submission in afterlockdown app
        call_id = create_submission(request, submission_form)

        # Redirect user to detailed view of post
        return redirect(f'/s/{call_id}')
    
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


    # Gets all post objects in DB
    posts = get_posts(request)

    # Post creation form
    submission_form = PostSubmitForm()

    context = {
        'submission_form': submission_form,
        'is_mobile': is_mobile,
        'posts': posts
    }
    return render(request, 'index.html', context)