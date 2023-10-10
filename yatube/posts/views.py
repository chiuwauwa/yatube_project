from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Самая главная страница!'
                        ' Главнее не будет, но будут другие')

def group_posts(request, sl):
    return HttpResponse(f'А это невьебенный пост от нашего блогера {sl}')
