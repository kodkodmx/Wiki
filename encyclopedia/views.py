from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, title):
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
    
