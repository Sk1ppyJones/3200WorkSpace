from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.


def index(request):
    if request.method == 'POST':
        # # Retrieve Data from form
        # entered_username = request.POST['username']

        # if entered_username == '':
        #     return render(request, 'reviews/reviews.html', {
        #         "has_error": True,
        #         "error_message": "Username cannot be empty."
        #     })

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save
            return HttpResponseRedirect('/submit/')
    else:
        form = ReviewForm()

    return render(request, 'reviews/reviews.html', {
        "form": form
    })


def submission(request):
    entered_username = request.GET.get('username')
    print(entered_username)
    return render(request, 'reviews/submission.html', {'username': entered_username})
