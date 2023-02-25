import openai
from decouple import config
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Code


def index(request):
    lang_list = [
        "bash",
        "c",
        "clike",
        "cpp",
        "css",
        "dart",
        "django",
        "docker",
        "git",
        "http",
        "javascript",
        "jsx",
        "markup",
        "markup-templating",
        "mermaid",
        "mongodb",
        "nginx",
        "perl",
        "php",
        "powershell",
        "python",
        "regex",
        "ruby",
        "rust",
        "scss",
        "sql",
        "tsx",
        "typescript",
        "yaml",
    ]
    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]
        # Check to make sure there is a language selected
        if lang == "Select Programming Language":
            messages.error(request, "You forgot to select a programming language.")
            return render(
                request,
                "website/index.html",
                {"lang_list": lang_list, "code": code, "lang": lang},
            )
        else:
            openai.api_key = config("OPENAI_API_KEY")
            openai.Model.list()
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. Fix this {lang} code {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                response = (response["choices"][0]["text"]).strip()
                record = Code(
                    question=code,
                    code_answer=response,
                    language=lang,
                    user=request.user,
                )
                record.save()
                return render(
                    request,
                    "website/index.html",
                    {"lang_list": lang_list, "response": response, "lang": lang},
                )
            except Exception as e:
                return render(
                    request,
                    "website/index.html",
                    {"lang_list": lang_list, "response": e, "lang": lang},
                )

    context = {"lang_list": lang_list}
    return render(request, "website/index.html", context)


def suggest(request):
    lang_list = [
        "bash",
        "c",
        "clike",
        "cpp",
        "css",
        "dart",
        "django",
        "docker",
        "git",
        "http",
        "javascript",
        "jsx",
        "markup",
        "markup-templating",
        "mermaid",
        "mongodb",
        "nginx",
        "perl",
        "php",
        "powershell",
        "python",
        "regex",
        "ruby",
        "rust",
        "scss",
        "sql",
        "tsx",
        "typescript",
        "yaml",
    ]
    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]
        # Check to make sure there is a language selected
        if lang == "Select Programming Language":
            messages.error(request, "You forgot to select a programming language.")
            return render(
                request,
                "website/suggest.html",
                {"lang_list": lang_list, "code": code, "lang": lang},
            )
        else:
            openai.api_key = config("OPENAI_API_KEY")
            openai.Model.list()
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                response = (response["choices"][0]["text"]).strip()
                record = Code(
                    question=code,
                    code_answer=response,
                    language=lang,
                    user=request.user,
                )
                record.save()
                return render(
                    request,
                    "website/suggest.html",
                    {"lang_list": lang_list, "response": response, "lang": lang},
                )
            except Exception as e:
                return render(
                    request,
                    "website/suggest.html",
                    {"lang_list": lang_list, "response": e, "lang": lang},
                )

    context = {"lang_list": lang_list}
    return render(request, "website/suggest.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("index")
        else:
            messages.error(
                request, "There was an error trying to login, please try again."
            )
            return redirect("index")
    else:
        context = {}
        return render(request, "website/login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("index")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You have successfully registered. Enjoy the experience."
            )
            return redirect("index")

    else:
        form = SignUpForm()
        context = {"form": form}
        return render(request, "website/register.html", context)

    context = {"form": form}
    return render(request, "website/register.html", context)


def past_code(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user)
        context = {'code': code}
        return render(request, "website/past_code.html", context)
    else:
        messages.success(request, 'You must be logged in to view this page.')
        return redirect("index")


def delete_past_code(request, past_id):
    past = Code.objects.get(pk=past_id)
    past.delete()
    messages.success(request, 'Your code snippet has been deleted.')
    return redirect('index')
