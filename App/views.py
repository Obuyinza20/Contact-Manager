from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def signUp(request):
    page = 'signup'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'error occurred during registration, check fields again.')

    return render(request, 'App/login_signup.html' , {'page':page, 'form':form})




def loginPage(request):
    page= 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User Does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Bad Credentials!, try again.')
        
            
    context = {
        'page':page

    }
    return render (request, 'App/login_signup.html' , context)

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def home(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains = search_input)
    else:
        contacts = Contact.objects.all()
        search_input =''
    context ={'contacts':contacts, 'search_input':search_input}
    return render(request, 'App/home.html', context)


def contact_profile(request , pk):

    contact = Contact.objects.get(id = pk)
    context={'contact':contact}
    return render(request, 'App/profile.html', context)

def create(request):

    contacts = Contact.objects.all()
 
    
    page ='create'

    if request.method == 'POST':
        new_contact = Contact(
        owner= request.user,
        full_name = request.POST['full_name'],
        relationship = request.POST['relationship'],
        email = request.POST['email'],
        phone = request.POST['phone_number'],
        address = request.POST['address']
       )
        new_contact.save()
        return redirect('home')
        
    context ={ 'page':page,'contacts':contacts}
    return render(request, 'App/create_update.html' , context)

def update(request , pk):
    contact = Contact.objects.get(id=pk)

    if request.method =='POST':
        contact.full_name = request.POST['full_name']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.address = request.POST['address']
        contact.phone = request.POST['phone_number']

        contact.save()

        return redirect('/contact-profile/' + str(contact.id))
       
    context = {'contact':contact}
    return render(request, 'App/create_update.html' , context)

def delete(request , pk):
    contact = Contact.objects.get(id = pk)

    if request.method =='POST':
        contact.delete()
        return redirect('home')
    
    context ={'contact':contact}
    return render (request, 'App/delete.html', context)


# def loginPage(request):
#     page = 'login'
#     # form = loginForm()

#     # if request.method =='POST':
#     #    UserName = request.POST['username']
#     #    Password = request.POST['pass1']
#     #    ConfirmP = request.POST['pass2']

#     #    if Password == ConfirmP:
#     #        user = User.objects.get(UserName= UserName)
#     #        if user is not None:
#     #         login(request, user)
#     #         return redirect('home')
#     #    else:
#     #        messages.error(request, 'Error Occured, Check credentials')
        
    
        

#     context={'page':page}

#     return render(request, 'App/login_signup.html', context)