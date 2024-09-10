from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Course

# View para a página inicial
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# Views para a gestão de usuários
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        photo = request.FILES.get('photo')  # Pega o arquivo da foto
        User.objects.create(name=name, email=email, phone=phone, course=course, photo=photo)
        return redirect('user_list')
    return render(request, 'users/user_create.html')

def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
        return redirect('user_list')
    return render(request, 'users/user_edit.html', {'user': user})

def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list') 
    return render(request, 'users/user_delete.html', {'user': user})

# View para a lista de cursos


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'cursos/courses_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        duration = request.POST['duration']
        Course.objects.create(name=name, description=description, duration=duration)
        return redirect('course_list')
    return render(request, 'cursos/course_create.html')

def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.name = request.POST['name']
        course.description = request.POST['description']
        course.duration = request.POST['duration']
        course.save()
        return redirect('course_list')
    return render(request, 'cursos/course_edit.html', {'course': course})

def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'cursos/course_delete.html', {'course': course})

