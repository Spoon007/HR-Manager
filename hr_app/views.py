from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employe, Departement, Contrat
from .forms import EmployeForm
from django.db.models import Sum, Q
from datetime import timedelta
from django.utils import timezone

@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    total_employes = Employe.objects.filter(est_archive=False).count()
    masse_salariale_totale = Employe.objects.filter(est_archive=False).aggregate(Sum('salaire'))['salaire__sum'] or 0
    departements = Departement.objects.count()
    
    # Recrutements proches (ex: 30 derniers jours)
    trente_jours_ago = timezone.now().date() - timedelta(days=30)
    recrutements_proches = Employe.objects.filter(date_embauche__gte=trente_jours_ago, est_archive=False).order_by('-date_embauche')
    
    context = {
        'total_employes': total_employes,
        'masse_salariale_totale': masse_salariale_totale,
        'departements': departements,
        'recrutements_proches': recrutements_proches,
    }
    return render(request, 'hr_app/dashboard.html', context)

@login_required
def profil(request):
    # Un employé est lié à un utilisateur Django
    # Pour simplifier, on cherche un employé dont le nom/prénom correspond
    employe = Employe.objects.filter(nom=request.user.last_name, prenom=request.user.first_name).first()
    return render(request, 'hr_app/profil.html', {'employe': employe})

@login_required
def employe_list(request):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    query = request.GET.get('q')
    poste = request.GET.get('poste')
    diplome = request.GET.get('diplome')
    
    employes = Employe.objects.filter(est_archive=False)
    
    if query:
        employes = employes.filter(
            Q(nom__icontains=query) | 
            Q(prenom__icontains=query) |
            Q(departement__nom_service__icontains=query)
        )
    if poste:
        employes = employes.filter(type_poste=poste)
    if diplome:
        employes = employes.filter(dernier_diplome=diplome)
        
    diplomes = Employe.objects.filter(est_archive=False).values_list('dernier_diplome', flat=True).distinct().order_by('dernier_diplome')
    return render(request, 'hr_app/employe_list.html', {
        'employes': employes, 
        'diplomes': diplomes
    })

@login_required
def employe_detail(request, pk):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    employe = get_object_or_404(Employe, pk=pk)
    return render(request, 'hr_app/employe_detail.html', {'employe': employe})

@login_required
def employe_create(request):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employe_list')
    else:
        form = EmployeForm()
    return render(request, 'hr_app/employe_form.html', {'form': form, 'title': 'Nouvel Employé'})

@login_required
def employe_update(request, pk):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('employe_list')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'hr_app/employe_form.html', {'form': form, 'title': 'Modifier l\'Employé'})

@login_required
def employe_archive(request, pk):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    employe = get_object_or_404(Employe, pk=pk)
    employe.est_archive = True
    employe.save()
    return redirect('employe_list')

@login_required
def masse_salariale(request):
    if not request.user.is_staff:
        return redirect('employe_dashboard')
    
    stats_dept = Employe.objects.filter(est_archive=False).values('departement__nom_service').annotate(total=Sum('salaire'))
    stats_poste = Employe.objects.filter(est_archive=False).values('type_poste').annotate(total=Sum('salaire'))
    
    return render(request, 'hr_app/masse_salariale.html', {
        'stats': stats_dept,
        'stats_poste': stats_poste
    })

@login_required
def employe_dashboard(request):
    if request.user.is_staff:
        return redirect('dashboard')
    
    employe = Employe.objects.filter(nom=request.user.last_name, prenom=request.user.first_name).first()
    
    if employe:
        collegues = Employe.objects.filter(departement=employe.departement).exclude(pk=employe.pk)[:5]
    else:
        collegues = []
        
    context = {
        'employe': employe,
        'collegues': collegues,
    }
    return render(request, 'hr_app/employe_dashboard.html', context)
