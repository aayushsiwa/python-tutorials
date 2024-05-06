from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages, admin
from .forms import NewUserCreationForm


# Create your views here.
def error_page(request, code, error):
    return render(request, "main/error.html", {"code": code, "error": error})


def account(request):
    user = request.user
    if not user.is_authenticated:
        error = "No user is logged in"
        return error_page(request, 404, str(error))
    username = request.user.username
    return render(request, "main/account.html", {"username": username})


def single_slug(request, single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(category__slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(series__series=m.series).earliest(
                "published"
            )
            series_urls[m] = part_one.slug
        return render(request, "main/category.html", {"part_ones": series_urls})
    tutorials = [t.slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tut = Tutorial.objects.get(slug=single_slug)
        tuts_from_series = Tutorial.objects.filter(
            series__series=this_tut.series
        ).order_by("published")
        this_tut_index = list(tuts_from_series).index(this_tut)
        return render(
            request,
            "main/tutorial.html",
            {
                "tutorial": this_tut,
                "sidebar": tuts_from_series,
                "this_tut_index": this_tut_index,
            },
        )
    error = f"{single_slug} does not correspond to anything."
    return error_page(request, 404, str(error))


def homepage(request):
    return render(
        request=request,
        template_name="main/categories.html",
        context={"categories": TutorialCategory.objects.all()},
    )


def register(request):
    if request.method == "POST":
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserCreationForm()
    return render(request, "main/register.html", context={"form": form})


def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_req(request):
    error = "Please enter a correct username and password. Note that both fields may be case-sensitive."
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")
        else:
            for msg in form.error_messages:
                messages.error(request, error)
    form = AuthenticationForm()
    return render(request, "main/login.html", context={"form": form})
