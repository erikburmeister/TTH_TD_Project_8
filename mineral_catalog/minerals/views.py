import random

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Mineral

# Create your views here.
def search_page(request):
    """Seach all fields in the Mineral Model."""
    term = request.GET.get('search')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term) |
        Q(image_filename__icontains=term) |
        Q(image_caption__icontains=term) |
        Q(category__icontains=term) |
        Q(formula__icontains=term) |
        Q(strunz_classification__icontains=term) |
        Q(color__icontains=term) |
        Q(crystal_system__icontains=term) |
        Q(unit_cell__icontains=term) |
        Q(crystal_symmetry__icontains=term) |
        Q(cleavage__icontains=term) |
        Q(mohs_scale_hardness__icontains=term) |
        Q(luster__icontains=term) |
        Q(streak__icontains=term) |
        Q(diaphaneity__icontains=term) |
        Q(optical_properties__icontains=term) |
        Q(refractive_index__icontains=term) |
        Q(crystal_habit__icontains=term) |
        Q(specific_gravity__icontains=term) |
        Q(group__icontains=term))
    return render(request, 'minerals/minerals_home.html',
                  {'minerals': minerals})


def search_by_letter(request):
    """Search by the first letter of the Mineral Model."""
    letter = request.GET.get('letter')
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/minerals_home.html',
                  {'minerals': minerals,
                   'search_letter': letter.upper()})


def search_by_group(request):
    """Search by the group field of the Mineral Model."""
    group = request.GET.get('group')
    minerals = Mineral.objects.filter(group__icontains=group)
    return render(request, 'minerals/minerals_home.html',
                  {'minerals': minerals, 'search_group': group})


def search_by_diaphaneity(request):
    """Search by the diaphaneity field of the Mineral Model."""
    diaphaneity = request.GET.get('diaphaneity')
    minerals = Mineral.objects.filter(
        diaphaneity__icontains=diaphaneity)
    return render(request, 'minerals/minerals_home.html',
                  {'minerals': minerals,
                   'search_diaphaneity': diaphaneity})


def minerals_home(request):
    """Shows each individual Mineral Model."""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/minerals_home.html',
                  {'title': 'Home', 'minerals': minerals})


def mineral_detail(request, pk):
    """Shows the fields the Mineral Model has."""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/minerals_detail.html',
                  {'title': mineral, 'mineral': mineral})


def mineral_random(request):
    """Pick a random Mineral Model and give it's details."""
    minerals = Mineral.objects.all()
    mineral = random.choice(minerals)
    return render(request, 'minerals/minerals_detail.html',
                  {'title': mineral, 'mineral': mineral})
