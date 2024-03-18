from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required
def context_handler(request):
    user = request.user
    user_groups = Group.objects.filter(user=user)
    return render(request, 'main.html', {'user': user, 'user_groups': user_groups})

