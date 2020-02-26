from django.shortcuts import render, redirect
from .models import Friend, ClassYear
from .forms import *

# Create your views here.
def index(request):

    if request.method == "POST":
        form = FriendForm(request.POST)
        if (form.is_valid()):
            new_friend = Friend()
            new_friend.name = form.cleaned_data['name']
            new_friend.ClassYear = ClassYear.objects.get(classYear = form.cleaned_data['ClassYear'])
            new_friend.hobby = form.cleaned_data['hobby']
            new_friend.food = form.cleaned_data['food']
            new_friend.drink = form.cleaned_data['drink']
            new_friend.save()
        return redirect('/#friends')
    else:
        form = FriendForm()
    friends = Friend.objects.all()
    classyear = ClassYear.objects.all()
    response = {'friends' : friends, 'classyear' : classyear}
    return render(request, 'index.html', response)

def deleteItem(request, name):
    item = Friend.objects.get(name=name)
    item.delete()
    return redirect('/#friends/')
