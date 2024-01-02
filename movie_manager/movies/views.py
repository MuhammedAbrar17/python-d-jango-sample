from django.shortcuts import render
from .models import MovieInfo
# Create your views here.
from .forms import MovieForm
def create(requset):
    frm = MovieForm()
    if requset.POST:
        frm = MovieForm(requset.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = MovieForm()        
         
      
      
    return render(requset,'create.html',{'frm':frm})




def list(request):
    
    movie_data=MovieInfo.objects.all()
    print(movie_data)
    return render(request,'list.html',{'movies':movie_data})




def edit(request):
    return render(request,'edit.html',)