from uuid import uuid4
from argon2 import PasswordHasher
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails, FileDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
    return render(request, "test.html", context={"msg":"Hey!"})


def home(request):
    return render(request, "home.html")


def registerUser(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        print(name, email, username, pass1, pass2)

        check_email = (UserDetails.objects.filter(email=email))
        print(check_email)
        print(len(check_email))
        
        check_un = (UserDetails.objects.filter(username=username))
        print(check_un==None)
        if (check_un is None and check_email is None) or (len(check_email)==0 and len(check_un)==0): 
            if pass1 != pass2:
                messages.error(request, "Passwords are not same")
                return render(request, "register.html")
            if pass1==pass2:
                newuser = UserDetails(name=name, email=email, username=username, password=pass1)
                #newuser.set_password(pass1)
                newuser.save()
                messages.success(request, "New User Created. Please Login again.")
                return redirect("/login")
        if (check_email is not None and check_un is not None) or (len(check_email)>0 and len(check_un)>0):
            messages.warning(request, "Credentials Already present.")
            return redirect("/register/")
    else:
        return render(request, "register.html")


def loginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass1")

        try:
            user = UserDetails.objects.get(email=email)
            s = authenticate(request, email=email, password=password)
            print(s)
        except:
            messages.error(request, "Email not found.")
            return redirect("/login/")
        print(user == None)

        if user is not None:
            if user.password==password:
                print(56456)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                x = authenticate(request, email=email, password=password)
                print(x)
                print(password, user.password)
                request.session["email"] =  email
                request.session["username"] = user.username
                request.session["name"] = user.name
                userdet = [{"email":email, "name":user.name, "username":user.username}]
                return redirect("/user")
            else:
                print(123123)
                print(password, user.password)
                messages.warning(request, "Incorrect Password.")
                return redirect("/login/")
    else:
        return render(request, "login.html")

#@login_required
def userHome(request):
    username = request.session["username"]
    email = request.session["email"]
    name = request.session["name"]
    user_details = [{"username":username, "email":email, "name":name}]
    return render(request, "userhome.html", context={"user_details":user_details})


def logoutUser(request):
    ...

def sendFiles(request):
    username = request.session["username"]
    email = request.session["email"]
    name = request.session["name"]
    user_details = [{"username":username, "email":email, "name":name}]

    r = UserDetails.objects.all()
    all_receivers = []
    for i in r:
        all_receivers.append(i.username)
    print(all_receivers)
    context = {"user_details":user_details, "all_receivers":all_receivers}

    if request.method == "POST":
        receivers = request.POST.getlist('receivers')
        files = request.FILES.get('file_in')
        filename = request.POST['filename']
        print(f"receivers={receivers}\nfilename={filename}\nfiles={files}\n")

        file_key = str(uuid4())
        print(f"file_key={file_key}")
        

        file_obj = FileDetails(files=files, filename=filename, uploaded_by=username, file_key=file_key)
        file_obj.save()
        #print(file_obj.file_key)
        #print(type(file_key), type(file_obj.file_key))
        for u in receivers:
            user = UserDetails.objects.get(username=u)
            file_key_obj = user.received_files_keys
            user.received_files_keys = file_key_obj+file_key+","
            user.save()

        return HttpResponse("working")
    
    return render(request, "send_files.html", context=context)


def receivedFiles(request):
    username = request.session["username"]
    email = request.session["email"]
    name = request.session["name"]
    user_details = [{"username":username, "email":email, "name":name}]

    user = UserDetails.objects.get(username=username)
    files_keys = user.received_files_keys
    file_keys = files_keys.split(",")
    file_keys = file_keys[:-1]
    print(file_keys)
    all_files = []

    for key in file_keys:
        f = FileDetails.objects.get(file_key=key)
        all_files.append({"file":f.files, "filename":f.filename, "upload_date":f.uploaded_date, "uploaded_by":f.uploaded_by})
    print(f"files_keys={files_keys}\nfiles={all_files}")
    context = {"user_details":user_details, "all_files":all_files}
    return render(request, "received_files.html", context=context)