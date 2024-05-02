from django.shortcuts import render

# Create your views here.
def index(request):
    studenci = [
        {
            'imie': 'Jan',
            'nazwisko': 'Kowalski',
            'nr_albumu': '12345'
        },
        {
            'imie': 'Aleksandra',
            'nazwisko': 'Nowak',
            'nr_albumu': '678910'
        }
    ]
    return render(request, 'www/index.html', {'studenci': studenci})