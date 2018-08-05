from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
  # the index function is called when root is visite
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def index(request):
    if request.method=="POST":
      return redirect('all_users') 
    else:
      return render(request,'user_dashboard/registration.html')
def all_users(request):
    context={
        'all_users':User.objects.all(),
        'all_jobs':Job.objects.all(),
    }
    return render(request,'user_dashboard/dashboard.html', context)
def all_jobs(request):
    context={
        'all_jobs':User.objects.all(),
    }
    return render(request,'user_dashboard/dashboard.html', context)
def new(request,id):
  context={
    'user': User.objects.get(id=id),
    'jobs': Job.objects.all()
  }
  return render(request,'user_dashboard/dashboard.html', context)
def new_registration(request):
   
  pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
  print("PASSWORD:",pw_hash)

  password_hash=pw_hash.decode('utf8')
  errors = User.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
  if len(errors):
      # if the errors object contains anything, loop through each key-value pair and make a flash message
      for key, value in errors.items():
          messages.error(request, value)
      # redirect the user back to the form to fix the errors
      return redirect('/')
  else:
      user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password_hash)
      user.save()
      messages.success(request, "User successfully updated")
            # redirect to a success route
      return redirect('/go_dashboard/'+str(user.id))
def go_dashboard(request,id):
    context={
        'user': User.objects.get(id=id)
    }
    return render(request,'user_dashboard/dashboard.html',context)
def add(request,id):
    context={
        'user': User.objects.get(id=id)
    }
    return render(request,'user_dashboard/addjob.html',context)
def add_job(request,id):
    if request.method == "POST":
        errors = Job.objects.basic_validator(request.POST)
            # check if the errors object has anything in it
        if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            user=User.objects.get(id=id)
            job = Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'], uploaded_by_id=user)
            job.save()
            messages.success(request, "Job successfully created")
    #         # redirect to a success route
    return redirect('/add/'+str(id))


def validate_login(request):
  user = User.objects.get(email=request.POST['email'])
  
  request.session['id']=user.id
  if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
      print("password match")
      return redirect('/new/'+str(user.id))
  else:
      print("failed password") 
      return render(request,"user_dashboard/registration.html")
def logout(request):
    if request.method=="POST":
      return render(request,'user_dashboard/registration.html')
    else:
      return redirect('/')
    
def show_jobs(request,id):
 
    all_jobs = Job.objects.all()
    user_jobs=all_jobs.get(uploaded_by_id=id)
    context={
        
        'all_jobs': user_jobs
    }
    return render(request,'user_dashboard/dashboard.html',context)
def post_quote(request,id):
    user=User.objects.get(id=id)
    Quote.objects.create(quote=request.POST['quote_from_post'], uploaded_by_id=user)
    
    return redirect('/show_post/'+str(user.id))

def edit(request,id):
  context={
        'user':User.objects.get(id=id)
  }
  return render(request,'user_dashboard/edit_job.html',context)

def update(request,id):
  if request.method=="POST":
        job=Job.objects.all().get(uploaded_by_id_id=id)
        if job:
            job.title = request.POST['title']
            job.description = request.POST['description']
            job.location = request.POST['location']
            job.save()
            url_string = '/edit/'+str(user.id)
            return redirect(url_string)
        else:
            response=HttpResponse()
            response.write=("<p> Couldn't find any message for this user</p>")
            return render('user_dashboard/edit_job.html',response)
        return redirect(url_string)
  else:
        return redirect('/')
  # messages.success(request, "User's data were successfully updated")
  # redirect to a success route
    
def show(request,id):
    user=User.objects.get(id=id)
    context={
        'jobs':Job.objects.get(id=id),
        'user':user
    }
    return render(request,'user_dashboard/show.html',context)
def destroy(request,id):
    job=Job.objects.get(id=id)
    job.delete()
    return redirect('/all_users')
  
