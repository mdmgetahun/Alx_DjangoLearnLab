from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import FormView, View
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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

@method_decorator(login_required, name='dispatch') #ensure that the user is logged in to access profile
class ProfileView(View):
    template_name = 'blog/profile.html'

    def get(self, request, *args, **kwargs): #allows users to view their profile
        form = ProfileUpdateForm(
            instance=request.user.profile, 
            initial={'email': request.user.email}
        ) 
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs): #allows users to update their profile
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully") # success message
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

    

# def profile_view(request):
#     return render(request, 'blog/profile.html')
# # Create your views here.
