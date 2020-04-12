from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Dr Mak.")

def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return 