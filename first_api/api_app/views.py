from django.shortcuts import render
from api_app.models import Monitor


# Create your views here.
def index(request):
    value_list = Monitor.objects.all()
    content = {'data':value_list}
    return render(request, 'api_app/index.html', context=content)
    