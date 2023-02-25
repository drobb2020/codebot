import openai
from decouple import config
from django.contrib import messages
from django.shortcuts import render


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
            openai.api_key = config('OPENAI_API_KEY')
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
                response = (response['choices'][0]["text"]).strip()
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
    context = {}
    return render(request, "website/suggest.html", context)
