# colaboradores_management/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Colaborador
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404



class ColaboradorListView(LoginRequiredMixin, ListView):
    model = Colaborador
    template_name = 'colaboradores/list.html'
    context_object_name = 'colaboradores'

class ColaboradorCreateView(LoginRequiredMixin, CreateView):
    model = Colaborador
    fields = '__all__'
    template_name = 'colaboradores/form.html'
    success_url = reverse_lazy('colaboradores:list')

class ColaboradorUpdateView(LoginRequiredMixin, UpdateView):
    model = Colaborador
    fields = '__all__'
    template_name = 'colaboradores/form.html'
    success_url = reverse_lazy('colaboradores:list')

class ColaboradorDeleteView(LoginRequiredMixin, DeleteView):
    model = Colaborador
    template_name = 'colaboradores/confirm_delete.html'
    success_url = reverse_lazy('colaboradores:list')

# colaboradores_management/views.py

@login_required(login_url='dp_ses:login')
def dashboard_view(request):
    total = Colaborador.objects.count()
    ativos = Colaborador.objects.filter(status=True).count()
    return render(request, 'dashboard.html', {
        'total_colaboradores': total,
        'colaboradores_ativos': ativos,
    })
