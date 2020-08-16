from django.contrib import messages

from django.core.paginator import Paginator

from django.shortcuts import redirect, render

from afterlockdown.forms import PostSubmitForm
from afterlockdown.models import Post
from afterlockdown.views import create_submission, get_posts

from logistics.models import OperatingSystem


def index(request):
    '''
    App entrypoint. Presents user with all `Post` objects
    '''
    if request.method == 'POST':
        submission_form = PostSubmitForm(request.POST)

        # Pass form and request to create_submission in afterlockdown app
        call_id = create_submission(request, submission_form)

        return redirect('index')
        
    elif request.method == 'GET':
        # Get divice operating system from meta data
        os = request.GET

        print(os)

        # Try/Catch checks if Operating System is in DB
        # raises exception if not. It assumes OS is mobile
        # if it is not in the DB
        try:
            OperatingSystem.objects.filter(name__icontains=os).first()
            is_mobile = False
        
        except:
            is_mobile = True


        # Gets all post objects in DB
        posts = Post.objects.all().order_by('?')
        paginator = Paginator(posts, 6)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Post creation form
        submission_form = PostSubmitForm()

        context = {
            'page_obj': page_obj,
            'submission_form': submission_form,
            'is_mobile': is_mobile,
            'posts': posts
        }
        return render(request, 'index.html', context)