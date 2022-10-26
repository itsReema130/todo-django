from django.shortcuts import render,redirect
from .models import todo
from .forms import todoform
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.
def index(request):
    todo_list=todo.objects.order_by('id')
    form=todoform()
    context={'todo_list':todo_list,'form':form}
    
    return render(request,'todo/index.html',context)

@require_POST
def addToDo(request):
    form=todoform(request.POST)

    
    if form.is_valid():
     new_todo=todo(text=request.POST['text'])
     new_todo.save()
    
    return redirect('index')


def completed(request,todo_id):
    stodo=todo.objects.get(pk=todo_id)
    stodo.complete=True
    stodo.save()
    return redirect('index')

def deletecomtodo(request):
   todo.objects.filter(complete=True).delete()
   return redirect('index')    


def deleteall(request):
    todo.objects.get().delete()
    return redirect('index')  
    

