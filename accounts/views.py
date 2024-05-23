from django.shortcuts import render,redirect
from accounts.forms import *
from django.contrib.auth import authenticate ,login,logout
# Create your views here.
def login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Replace 'home' with your home view name
            else:
                form.add_error(None, 'Invalid username or password')
    context = {
        'form':form
    }
    return render(request, 'login_page.html',context)


def register_page(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        account_form = UserAccountForm(request.POST, request.FILES)

        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            account = account_form.save(commit=False)
            account.user = user
            account.save()

            login(request, user)
            return redirect('login')  # Replace 'home' with the URL name of your desired redirect view
    else:
        user_form = UserRegistrationForm()
        account_form = UserAccountForm()

    context = {
        'user_form': user_form,  # Corrected key
        'account_form': account_form
    }

    return render(request, 'register.html', context)
def logout_user(request):
    logout(request)
    return redirect('login')

