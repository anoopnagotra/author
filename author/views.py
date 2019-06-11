from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm


# Create your views here.
def home(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        # return render(request, "base.html", {"title": "home"})
        return redirect('/authors/')
    else:
        return redirect("/logout/")


def author(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        if request.method == "POST":
            author = Author()
            form = AuthorForm(request.POST, request.FILES, instance=author)
            if form.is_valid():
                form.save()
            authors = Author.objects.all()
            return render(request, "authors.html", {"title": "Author", "records": authors})
        else:
            form = AuthorForm()
            return render(request, "create_author.html", {"form": form})
    else:
        return redirect("/logout/")


def author_details(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        print(request.user)
        authors = Author.objects.all()
        return render(request, "authors.html", {"title": "Event", "records": authors})
    else:
        return redirect("/logout/")


def author_display(request, id):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        print(request.user)
        author = Author.objects.filter(pk=id).first()
        return render(request, "display_author.html", {"title": "Event", "record": author})
    else:
        return redirect("/logout/")