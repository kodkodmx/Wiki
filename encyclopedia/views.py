from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, title):
    if title == "css" or title == "html":
        title = title.upper()
    else:
        title = title.capitalize() 
    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "title": title , "message": "The requested page was not found."
        })
    else:
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(title))
        return render(request, "encyclopedia/content.html", {
            "content": content , "title": title
    })
