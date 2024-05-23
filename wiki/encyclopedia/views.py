from django.shortcuts import render
from markdown import Markdown
from random import choice

from . import util




def ConverterToHtml(name):
    inf = util.get_entry(name)
    markdowner = Markdown()
    if inf == None:
        return None
    else:
        return markdowner.convert(inf)

def entry(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html")
    else:
        entry_page = ConverterToHtml(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page": entry_page
        })

def index(request):
    if request.method == 'POST':
        inf = util.get_entry(request.POST['q'])
        if inf is not None:
            entry = ConverterToHtml(request.POST['q'])
            return render(request, "encyclopedia/entry.html", {
                "title": request.POST['q'],
                'page': entry
            })
        else:
            results = []
            for i in util.list_entries():
                if request.POST['q'].lower() in i.lower():
                    results.append(i)
            return render(request, "encyclopedia/search_results.html", {
                'results': results
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == 'POST':
        for i in util.list_entries():
            if request.POST['title'].lower() == i.lower():
                return render(request, "encyclopedia/error2.html")
        util.save_entry(request.POST['title'], request.POST['content'])
        return entry(request, request.POST['title'])
    return render(request, "encyclopedia/create.html")

def edit(request):
    if request.method == 'POST':
        return render(request, "encyclopedia/edit.html", {
            'title': request.POST['title'],
            'content': util.get_entry(request.POST['title'])
        })
def edited(request):
    if request.method == 'POST':
        util.save_entry(request.POST['title'], request.POST['content'])
        return entry(request, request.POST['title'])
def Random(request):
    rand_title = choice(util.list_entries())
    entry_page = ConverterToHtml(rand_title)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_title,
        "page": entry_page
    })
