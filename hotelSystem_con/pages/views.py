from django.shortcuts import render
from django.views.generic import TemplateView
from hotels.models import Hotel,Room,User


#def index(request):
#    return render(request, 'index.html',{'title':'main'})
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()[:3]
        context['total_hotels'] = Hotel.objects.all().count()
        context['total_owner'] = User.objects.all().count()
        context['total_cities'] = Hotel.objects.values('city').distinct().count()
        context['title'] = 'main'

        return context


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')