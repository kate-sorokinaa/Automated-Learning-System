from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная',
        'mainText': 'Освой новую сферу или улучши уровень уже имеющиехся знаний с помощью нашей онлайн-платформы '
                    'YourCourse. \nДесятки курсов самых разных направлений, находящихся под рукой в любое время. '
                    'Онлайн-обучение, которое будет удобно каждому. \n\nНе жди! Присоединяйся.\n',
        'coolThing1': '\nВ любой момент можно продолжить обучение\n\n',
        'coolThing2': '\nВыбирай из множества областей\n\n',
        'coolThing3': '\nНикогда не прекращай развиваться\n\n',
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Про проект',
        'mainText': 'Проект "Автоматизированная Система Обучения".'
                    '\n\nПодготовлен и выполнен студенткой Сорокиной Екатериной, группа 053504'
                    '\n\n\n БГУИР ФКСиС 2022'
    }
    return render(request, 'main/about.html', data)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return index(request)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "login/"

    template_name = "main/register.html"

    def form_valid(self, form):
        form.save()

        return user_login(self)
