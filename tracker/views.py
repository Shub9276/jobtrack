from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html",{"form":form})

@login_required
def application_list(request):
    all_applications = Application.objects.filter(user = request.user)
    applications = all_applications

    query = request.GET.get("q","")
    selected_status = request.GET.get("status","")

    if query:
        applications = applications.filter(Q(company__icontains=query) | Q(role__icontains=query))

    if selected_status:
        applications = applications.filter(status = selected_status)

    paginator = Paginator(applications, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    params = request.GET.copy()
    params.pop("page", None)
    querystring = params.urlencode()

    stats = {
        "total" : all_applications.count(),
        "applied" : all_applications.filter(status="applied").count(),
        "interview": all_applications.filter(status = "interview").count(),
        "offer":all_applications.filter(status="offer").count(),
        "rejected":all_applications.filter(status="rejected").count(),
    }

    context = {
        "applications" : page_obj,
        "querystring":querystring,
        "stats":stats,
        "query":query,
        "selected_status":selected_status,
        "status_choices":Application.STATUS_CHOICES,
    }

    return render(request, "tracker/application_list.html",context)

@login_required
def application_add(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit = False)
            application.user = request.user
            application.save()
            return redirect("application_list")

    else:
        form = ApplicationForm()
    
    return render(request, "tracker/application_form.html", {"form":form})


@login_required
def application_edit(request, pk):
    application = get_object_or_404(Application, pk = pk , user = request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance = application)
        if form.is_valid():
            form.save()
            return redirect("application_list")

    else:
        form = ApplicationForm(instance = application)
    return render(request, "tracker/application_form.html",{"form": form, "editing":True})


@login_required
def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk, user = request.user)
    if request.method == "POST":
        application.delete()
        return redirect("application_list")
    
    return render(request,"tracker/application_confirm_delete.html",{"application":application})
