from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, template_name='compiler/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_fom = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_fom.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_fom.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES['profile_pic']:
                profile.save()
                registered = True
            else:
                print(user_form.errors)
        else:
            user_form = UserForm()
            profile_fom = UserProfileInfoForm()
        return render(request, template_name='compiler/registration.html', context={
            'user_fom': user_form,
            'profile_fom': profile_fom,
            'registered': registered
        })

# Create your views here.
