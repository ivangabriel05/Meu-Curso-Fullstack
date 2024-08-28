from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Item, clients
from .forms import ClientesForm
from datetime import datetime
from django.contrib import messages
from django.db.models import F

class ItemListView(ListView):
   model = Item
   template_name = 'item/item_list.html'

class ItemDetailView(DetailView):
   model = Item
   template_name = 'item/item_detail.html'

class ItemCreateView(CreateView):
   model = Item
   fields = ['nome', 'descricao', 'preco']
   success_url = '/'
   template_name = 'item/item_form.html'
   

class ItemUpdateView(UpdateView):
   model = Item
   fields = ['nome', 'descricao', 'preco']
   success_url = '/'
   template_name = 'item/item_form.html'

class ItemDeleteView(DeleteView):
   model = Item
   success_url = '/'
   template_name = 'item/item_confirm_delet.html'

def FormularioView(request):
   if request.method == "POST":
      form = ClientesForm(request.POST or None)
      if form.is_valid():
         cd = form.cleaned_data
         pd = clients(
            name = cd['name'],
            cpf_cnpj = cd['cpf_cnpj'],
            rg_ie = cd['rg_ie'],
            zip_code = cd['zip_code'],
            address = cd['address'],
            neighborhood = cd['neighborhood'],
            number = cd['number'],
            city = cd['city'],
            state = cd['state'],
            ddd = "",
            created_at = datetime.now(), 
         )
         pd.save()

         messages.success(request, "Dados adcionados com sucesso no Formulario")

         return redirect('formulario')
      else: 
         print(form.errors)
   else:
      form = ClientesForm()


   return render(request, 'forms/form_template.html', {'form': form})


def FormListView(request):
   clientes = clients.objects.all()
   return render(request, 'forms/form_list.html', {'cliente': clientes})

def FormDetailView(request, pk):
   id = pk 
   clientes = clients.objects.get(pk=id)
   return render(request, 'forms/form_detail.html', {'cliente': clientes})

def FormDeleteView(request, pk):
   id = pk
   clientes = clients.objects.get(pk=id)

   if request.method == 'POST':
      clientes.delete()
      messages.success(request, "Cliente Deletado Com Sucesso!!")
      return redirect('form_list')
   return render(request, 'forms/form_confirme_delete.html', {'cliente': clientes})