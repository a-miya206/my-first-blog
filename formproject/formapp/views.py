from django.shortcuts import render, redirect
from formapp.forms import ContentsForm
from formapp.models import Contents

def home(request):
    model=Contents.objects.values()
    form=ContentsForm(request.POST)
    
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return redirect("home")
    else:
        form=ContentsForm()
    return render(request, 'formapp/index.html', {'form': form, 'model': model})