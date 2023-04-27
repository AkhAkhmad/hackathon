from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from . import forms, models


@login_required
def func(request):
    try:
        user_profile = models.UserProfile.objects.get(user=request.user)
    except BaseException as e:
        print('--------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------')
        print(e)
    else:
        print(user_profile)
    context = {
        'choice': user_profile.choice,
    }
    return render(request, 'main/base.html', context)


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        user = form.save()
        profile = models.UserProfile.objects.create(user=user, choice=form.cleaned_data['choice'])
        print(
            '------------------------------------------------------------------------------------------------------------------------------')
        from pprint import pprint
        pprint(form.cleaned_data)
        print(profile.choice)
        messages.success(self.request, 'Регистрация прошла успешно')
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
