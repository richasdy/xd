from tabel.form import editForm
from .models import tabel
#from django.views.generic import UpdateView, DeleteView
from django.shortcuts import redirect, render

# Create your views here.
#class UpdateTabelView(UpdateView):
#    model = tabel
#    template_name = 'auth/form.html'
#    fields = ['waktu', 'nama', 'level', 'pesan']

def update(request, req_id):
    up_tabel = tabel.objects.get(id=req_id)
    print(tabel.t_id)

    data = {
        'waktu' : up_tabel.waktu,
        'nama' : up_tabel.nama,
        'level' : up_tabel.level,
        'pesan' : up_tabel.pesan,
    }
    up_form = editForm(request.POST or None, initial=data, instance=up_tabel)
    
    if request.method == 'POST':
        if up_form.is_valid():
            up_form.save()

        return redirect('tabel/')

    context = {
        
    }    
