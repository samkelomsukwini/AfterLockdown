import random
import string

from django.contrib import messages

from django.http import Http404, HttpResponse, JsonResponse

from django.shortcuts import redirect, render 

from .forms import PostSubmitForm
from .models import Post


def get_posts(request):
    '''
    Gets and returns all `Post` objects
    '''
    submissions = Post.objects.all().order_by('-created')
    
    return submissions

def view_post(request, call_id):
    '''
    Gets and redirects user to `Post` object associated
    with `call_id`
    '''
    submission = Post.objects.get(call_id=call_id)

    if request.method == 'POST':
        form = PostSubmitForm(request.POST)

        # Send `form` to create_post view in aferlockdown app.
        call_id = create_submission(request, form)

        # redirect user to the post detail view after
        # the creation of new Submission object
        return redirect(f'/s/{call_id}')

    # form to be passed to template if request.method is GET
    submission_form = PostSubmitForm() 

    context = {
        'submission_form': submission_form,
        'post': submission
    }

    return render(request, 'posts/view/post_detailed.html', context)


def post_call_id_generator(size=10, chars=string.ascii_letters + string.digits):
    '''
    Generates and returns `Submission` base64 call id
    '''
    return ''.join(random.choice(chars) for _ in range(size))


def check_call_id_exists(call_id):
    '''
    Checks if call id exists. Generates and returns new call id if exists
    '''
    # Try/Catch checks to see if a Submission with call_id == call_id
    # already exists. This will not throw an error if True. And if
    # that's the case, the function becomes recursive until a unique
    # call_id is generated
    try:
        Post.objects.get(call_id=call_id)

        # New call_id generated
        new_call_id = post_call_id_generator()

        # New call_id checked against all Submission objects
        check_call_id_exists(new_call_id)
    
    except:
        # This means there has been an error which means
        # that there's no Submission object with call_id == call_id
        return call_id


def create_submission(request, form):
    '''
    Creates and returns new `Post` object
    '''
    if request.method == 'POST':
        # form passed from POST accepting views
        form = form

        # Form validation:
        # 1. Sanitise user input
        # 2. Check if all fields are filled
        if not form.is_valid():
            # Form contained errors
            messages.error(request, 'Couldn\'t save your submission. Please try again.')
            return redirect('index')
        
        else:
            # Don't save yet
            submission = form.save(commit=False)
            
            # Submission text
            body = request.POST['body'].lower()
            post_prefix = 'After lockdown I want to '

            # if/else appends pos_prefix to user text
            if post_prefix in body:
                # user already added the prefix
                pass

            else:
                # concatenate user sub with prefix then insert 
                # new string into DB as the body
                new_submission_body = post_prefix+body
                submission.body = new_submission_body
            
            # generate call_id
            _call_id = post_call_id_generator()

            # Check to see if generated call_id exists in DB
            call_id = check_call_id_exists(_call_id)

            # Assign call_id to Post object
            submission.call_id = call_id

            # Insert the Submission object into DB
            form.save()

            messages.success(request, 'Success, you submission has been saved')
            return call_id
