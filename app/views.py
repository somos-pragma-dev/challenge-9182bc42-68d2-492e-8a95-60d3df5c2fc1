def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_panel')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, corrige los errores abajo.')
    return render(request, 'app/login.html', {'form': UserLoginForm()})


@login_required
def admin_panel(request):
    profiles = UserProfile.objects.all()
    return render(request, 'app/admin_panel.html', {'profiles': profiles})


from django.urls import path
from. import views