from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from .models import Review
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
# Create your views here.


class ReviewView(CreateView):
    model = Review
    template_name = 'reviews/reviews.html'
    form_class = ReviewForm  # Only needed bc of customizations
    success_url = '/submit/'

    # FormView
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # View
    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, 'reviews/reviews.html', {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/submit/')
    #     else:
    #         return render(request, 'reviews/reviews.html', {
    #             "form": form
    #         })


class SubmissionView(TemplateView):
    template_name = 'reviews/submission.html'

    # Possible but not reccomended
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     entered_username = self.request.GET.get('username')
    #     context['username'] = entered_username
    #     return context


class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'  # defaults to object_list

    # def get_queryset(self):
    #     base_query = super().get_queryset()

    #     data = base_query.filter(rating__gt=3)

    #     return data

    # TemplateView
    # template_name = 'reviews/review_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    context_object_name = 'review'

    # TemplateView
    # template_name = 'reviews/single_review.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context
