from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import FormView, View, ListView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, ProfileUpdateForm, PostForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

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

# def posts_view(request):
#     return HttpResponse("Post here!")

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

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(ListView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def test_func(self):
       post = self.get_object()
       return self.request.user == post.author

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')



