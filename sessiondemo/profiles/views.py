from urllib import request

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from .forms import CreateProfileForm
from .models import Profile

# Create your views here.


class CreateProfileView(CreateView):
    model = Profile
    fields = ['name', 'image']
    template_name = 'profiles/create_profile.html'
    success_url = '/success'

    # def get(self, request):
    #     form = CreateProfileForm()
    #     profiles = Profile.objects.all()
    #     return render(request, 'profiles/create_profile.html', {"form": form, "profiles": profiles})

    # def post(self, request):
    #     submitted_form = CreateProfileForm(request.POST, request.FILES)
    #     if submitted_form.is_valid():
    #         profile = Profile(
    #             image=submitted_form.cleaned_data['image'], name=submitted_form.cleaned_data['name'])
    #         profile.save()
    #         return redirect('create-profile')
    #     return render(request, 'profiles/create_profile.html', {"form": submitted_form})


class SuccessView(TemplateView):
    template_name = 'profiles/success.html'

class UserProfilesView(ListView):
    model = Profile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'