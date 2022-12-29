from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from environs import Env
# env = Env()
# env.read_env()
def signin(request):
    # request.session['project_name'] = env("HOST_")
    try:
        if request.method == 'POST':
            res = authenticate(username=request.POST['username'], password=request.POST['password'])
            if res:
                login(request, res)
                request.session['user_id'] = res.id
                # request.session['ip'] = env("IP_")
                # request.session['access_token_gologin'] = env("access_token_gologin")
                messages.success(request, 'Login  Successfully')
                return redirect('dashboard/main/')
            else:
                messages.error(request, 'Invalid Credentials')
    except Exception as e:
        print("exception", e)
    return render(request, 'user_auth/signin.html')


def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(username=request.POST['username'],
                                            email=request.POST['email'],
                                            password=request.POST['password'])
            user.save()
            messages.success(request, "Congratulate!, User created successfully.")
            return redirect('/')
        except Exception as e:
            messages.success(request, "User already exist please try with different one")
            return redirect('/signup/')

    return render(request, 'user_auth/signup.html')


def logout_user(request):
    try:
        logout(request)
        return redirect("signin")
    except:
        return redirect("signin")


# decorator
def login_required(view_func):
    def func_wrapper(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            return redirect('signin')
        except Exception as e:
            print("Exception\t:\t", e)
            return redirect('signin')

    return func_wrapper


def page_not_found_view(request, exception):
    return render(request, 'user_auth/signin.html', status=404)