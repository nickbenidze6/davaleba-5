from django.shortcuts import render, redirect
from .forms import StudentForm, BookModelForm
from .models import Student, Book


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            course = form.cleaned_data['course']
            
            Student.objects.create(firstname=firstname, lastname=lastname, age=age, course=course)
            
            return redirect("student")
    else:
        form = StudentForm()
        
    students = Student.objects.all()
    context = {
        "form": form,
        "students": students
    }
    
    return render(request, "forms_app/student.html", context)





def book(request):
    if request.method == "POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("book")
    elif request.method == "GET":
        form = BookModelForm()
        books = Book.objects.all()
        context = {
            "form": form,
            "book": books
        }
        return render(request, "forms_app/book.html", context)
