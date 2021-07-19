from tabel.form import tabelForm
from .models import tabel
from django.shortcuts import redirect, render


def update(request, id):
    up_tabel = tabel.objects.get(id=id)
    form = tabelForm(instance=up_tabel)
    if request.method == 'POST':
        form = tabelForm(request.POST or None,  instance=up_tabel)   
        if form.is_valid():
            form.save()
            return redirect('/')
    print("data berhasil diperbarui")        
    context = {'form' : form}
    return render(request, 'auth/form.html', context)

def delete(request, id):
    del_tabel = tabel.objects.get(id=id)
    del_tabel.delete()
    print("data berhasil dihapus")
    return redirect('/')
  
