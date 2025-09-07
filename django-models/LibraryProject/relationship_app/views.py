from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import BookForm


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_book')
    return render(request, 'relationship_app/book_book_confirm_delete.html', {'book': book})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.sace()
            return redirect('list_books')
        else:
            form = BookForm(instance=book)
        return render(request, 'relationship_app/book_form.html', {'form: form'})
    


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect("login")  
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  
            messages.success(request, "Login successful!")
            return redirect("relationship_app/login.html")  
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("relationship_app/logout.html")

def role_redirect(request):
    role = request.user.userprofile.role
    if role == 'Admin':
        return redirect('/admin/')
    elif role == 'Librarian':
        return redirect('/librarian/')
    else:
        return redirect('/member/')
#Roles

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
def is_librarian(user):
    return hasattr(user, 'userprofile' and user.userprofile.role == 'Librarian')
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

#user views

@user_passes_test(is_admin)

def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



