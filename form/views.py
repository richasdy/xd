from django.shortcuts import render

# Create your views here.

def update(request):
    context = {}
    if request.method == 'POST':
        form = profilForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        if form.is_valid():
            form.save()
            return redirect('auth/system-login.html')
    else:
        form = profilForm(instance=request.user)
    context['form'] = form
    return render(request, 'auth/form.html', {'form': form})



#def remove_log(request):
    #form = UserCreationForm(request.POST or None)
    #context['log'] = False
   # form = logging(data=request.POST, )
    #if request.method(logger) == "POST":
    #    if form.is_valid():
    #        DeleteView.get_object(logger)
    #        print("Succesfully deleted")
    #        return redirect('login')
