from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from .forms import StudentRegisteration

# Create your views here.
def home(request):
    form = StudentRegisteration()
    students = User.objects.all()
    return render(request,'myapp/index.html',{'form':form,'stu':students})

def save_data(request):
    if request.method == "POST":
        form= StudentRegisteration(request.POST)
        if form.is_valid():
            sid= request.POST['sid']
            name= request.POST['name']
            email= request.POST['email']
            password= request.POST['password']

            if(sid!=""):
                usr=User.objects.filter(pk=sid).update(name=name,email=email,password=password)

            else:
                usr = User.objects.create(name=name, email=email, password=password)

            return JsonResponse({'status':'1', 'student_data':getStudentData()})
        else:
            return JsonResponse({'status':'0'})

def delete_record(request):
    if request.method == "POST":
        id=request.POST['id']
        User.objects.filter(pk=id).delete()
        # Use fiter instead of get because it won't genetate exception incase id is not available
        return JsonResponse({'status':'1', 'student_data':getStudentData()})
    else:
        return JsonResponse({'status':'0'})

def edit_record(request):
    if request.method == "POST":
        id=request.POST['id']
        stu = User.objects.get(pk=id)
        student_data={"id":stu.id,"name":stu.name,"email":stu.email,"password":stu.password}
        return JsonResponse(student_data)

def getStudentData():
    students = User.objects.values()
    student_data= list(students)
    return student_data



    