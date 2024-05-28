from django.shortcuts import render

finches = [
    {'name': 'Larry', 'type':'canary', 'from': 'Yorkshire', 'color': 'yellow'},
    {'name': 'Cheryl', 'type':'house-finch', 'from': 'North America', 'color': 'gray'},
    {'name': 'Toffee', 'type':'towhee', 'from': 'North America', 'color': 'dark-brown'},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')