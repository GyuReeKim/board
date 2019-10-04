from django.shortcuts import render, redirect
from .models import Todo # '.models' 대신 'todos.models'를 사용해도 된다.

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    content = request.POST.get('content')
    due_date = request.POST.get('due-date')

    # todo = Todo()
    # todo.author = author
    # todo.title = title
    # todo.content = content
    # todo.due_date = due_date
    # todo.save() # 바로 저장하지 않고 쓰일때 사용

    # create는 안에 인스턴스를 만들고 생성까지 해준다.
    todo = Todo.objects.create(
        author=author,
        title=title,
        content=content,
        due_date=due_date,
    )
    return redirect('/todos/')