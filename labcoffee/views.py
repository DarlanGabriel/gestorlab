from django.shortcuts import render

from labcoffee.models import Presentation, Author


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_presentations = Presentation.objects.all().count()
    presentations = Presentation.objects.all()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_presentations': num_presentations,
        'presentations': presentations,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def list(request):
    presentations = Presentation.objects.all()
    context = {
        'presentations': presentations,
    }
    return render(request, 'list.html', context=context)
