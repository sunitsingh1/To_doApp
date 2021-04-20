from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import ToDo
from todo.forms import ToDoForm


# Create your views here.
def home(request):
    # return HttpResponse("Hello Home View")
    template_name = 'home.html'
    todo_list = ToDo.objects.all() #return queryset
    form = ToDoForm()
    # print(todo_list)
    context = {'todo_list':todo_list,"form":form}
    return render(request, template_name, context=context)

def add_todo(request):
    if request.method == 'POST':
        # todo_text= request.POST.get('todo_text')
        # ToDo.objects.create(todo_text=todo_text)
        # print(todo_text)

        form = ToDoForm(request.POST) #using form validation
        if form.is_valid():
            todo_text = form.cleaned_data.get('todo_text')
            ToDo.objects.create(todo_text=todo_text)
    return redirect('home')

def delete_todo(request,todo_id):
    if request.method == 'POST':
        todo_obj=ToDo.objects.get(pk=todo_id)
        todo_obj.delete()
    return redirect('home')

def edit_todo(request,todo_id):
    todo_object = ToDo.objects.get(pk=todo_id)

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
           todo_object.todo_text = form.cleaned_data.get('todo_text')
           todo_object.save()
           return redirect('home')

    template_name = 'edit.html'
    form = ToDoForm(initial = {'todo_text' : todo_object.todo_text})
    
    context = {'form':form,'todo_object':todo_object}
    return render(request,template_name,context)

