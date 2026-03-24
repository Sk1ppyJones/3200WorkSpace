from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class SessionHomeView(TemplateView):
    template_name = 'colordo/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['bg_color'] = self.request.session.get('bg-color', '#FFFFFF')
        return context


class CHangeColorView(TemplateView):
    template_name = 'colordo/change_color.html'

    def post(self, request, *args, **kwargs):
        color = request.POST.get('color', '#FFFFFF')
        request.session['bg-color'] = color
        return redirect('home')
# Process
# 1- Django gens a session ID and sends it to the client as a cookie
# 2- Client sends the session ID back to the server with each request

# Why sessions?
# - Store user-specific data across requests
# - Implement user authentication
# - Personalize user experience
# Session data is stored on the server, and the client only has the session ID
