from django.shortcuts import render
from django.http import HttpResponse
from .models import Medicine

# Create your views here.


def homepage(request):

    medicines = Medicine.objects.all()
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        medicines = medicines.filter(medicine_name__icontains=search_term)
        print(medicines)

    context = {"medicines": medicines, 'search_term': search_term}

    return render(request,
                  'main/home.html',
                  context)


def details(request, medicine_id):
    return HttpResponse('You are looking for: {}'.format(medicine_id))

