from django.shortcuts import render
from markdown2 import Markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
        if title in util.list_entries():
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.lower() in util.list_entries():
            title=title.lower()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.upper() in util.list_entries():
            title=title.upper()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.capitalize() in util.list_entries():
            title=title.capitalize()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "title": title , "message": "The requested page was not found."
        })
    
def search(request):
    if request.method == "POST":
        title = request.POST.get('q')
        if title in util.list_entries():
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.lower() in util.list_entries():
            title=title.lower()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.upper() in util.list_entries():
            title=title.upper()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        elif title.capitalize() in util.list_entries():
            title=title.capitalize()
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        else:
            title = request.POST.get('q')
            entries = []
            for entry in util.list_entries():
                if title in entry:
                    entries.append(entry)
                elif title.lower() in entry:
                    entries.append(entry)
                elif title.upper() in entry:
                    entries.append(entry)
                elif title.capitalize() in entry:
                    entries.append(entry)
            if entries:
                    return render(request, "encyclopedia/result.html", {
                        "entries": entries , "title": title
                            })
            else:
                return render(request, "encyclopedia/error.html", {
                    "title": title , "message": "The requested page was not found."
                        })
    else:
        return render(request, "encyclopedia/search.html")
    
def new(request):
    if request.method == "POST":
        title = request.POST.get('title').capitalize()
        content = request.POST.get('content')
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "title": title , "message": "The entry you are trying to save already exists."
            })
        else:
            filename = f"entries/{title}.md"
            if default_storage.exists(filename):
                default_storage.delete(filename)
            default_storage.save(filename, ContentFile("#" + " " + title.capitalize() + "\n\n" + content.capitalize()))
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
    else:
        return render(request, "encyclopedia/new.html")
    
def save(request):
    if request.method == "POST":
        title = request.POST.get('title').capitalize()
        content = request.POST.get('content')
        if title in util.list_entries():
            util.save_entry(title, content)
            markdowner = Markdown()
            content = markdowner.convert(util.get_entry(title))
            return render(request, "encyclopedia/content.html", {
                "content": content , "title": title
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "title": title , "message": "The requested page was not found."
            })
    
def edit(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        title = request.POST.get('title')
        util.save_entry(title, content)
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/content.html", {
            "content": content , "title": title
        })
    else:
        return render(request, "encyclopedia/edit.html", {
            "content": util.get_entry(title) , "title": title
        })

def delete(request, title):
    try:
        default_storage.delete(f"entries/{title}.md")
    except FileNotFoundError:
        return None
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def random(request):
    import random
    title = random.choice(util.list_entries())
    markdowner = Markdown()
    content = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/content.html", {
        "content": content , "title": title
    })

def error(request, title):
    return render(request, "encyclopedia/error.html", {
                "title": title , "message": "The requested page was not found."
            })