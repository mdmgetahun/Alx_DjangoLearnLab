from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

class UserLoginView(LoginView): #custom login view
    template_name = 'blog/login.html'
    success_url = reverse_lazy('profile') # redirect to profile page after successful login

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home') # redirect to home page after logout

class RegisterView(FormView): #custom register view
    template_name = 'blog/register.html'
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') # redirect to login page after successful registration

    def form_valid(self, form): 
        form.save()
        messages.success(self.request, "Success")
        return super().form_valid(form)

def home_view(request):
    return HttpResponse("home")

def posts_view(request):
    return HttpResponse("Post here!")

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Successfully created account!")
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()  

#     return render(request, 'blog/register.html', {'form': form})

def profile_view(request):
    return render(request, 'blog/profile.html')
# Create your views here.
