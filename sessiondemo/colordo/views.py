from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View


class SessionHomeView(TemplateView):
    template_name = 'colordo/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bg_color'] = self.request.session.get('bg-color', '#FFFFFF')
        context['todo_list'] = self.request.session.get('todo_list', [])
        return context


class CHangeColorView(TemplateView):
    template_name = 'colordo/change_color.html'

    def post(self, request, *args, **kwargs):
        color = request.POST.get('color', '#FFFFFF')
        request.session['bg-color'] = color
        return redirect('home')


class AddTaskView(View):
    def post(self, request):
        new_task = request.POST.get('task_text', '').strip()

        if new_task:
            tasks = request.session.get('todo_list', [])
            tasks.append(new_task)
            request.session['todo_list'] = tasks
            request.session.modified = True

        return redirect('home')
    
class DeleteTaskView(View):
    def post(self, request, task_index):
        tasks = request.session.get('todo_list', [])
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            request.session['todo_list'] = tasks
            request.session.modified = True
        return redirect('home')

class ResetSessionView(View):
    def post(self, request):
        request.session.flush() # Wipes whole page
        # Alternative: request.session.clear() # Clears data but keeps session ID
        # request.session['todo_list'] = [] # Clear specific data
        return redirect('home')
# Process
# 1- Django gens a session ID and sends it to the client as a cookie
# 2- Client sends the session ID back to the server with each request

# Why sessions?
# - Store user-specific data across requests
# - Implement user authentication
# - Personalize user experience
# Session data is stored on the server, and the client only has the session ID
