"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView, ListView
from .models import Spoiled, Submitted

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def faq(request):
    """Renders the FAQ page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/faq.html',
    )

def search_spoiled(request):
    """Renders the spoiled ballot search page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/search_spoiled.html',
    )

class SpoiledSearchPageView(TemplateView):
    template_name = 'app/search_spoiled.html'

class SpoiledSearchResultsView(ListView):
    model = Spoiled
    template_name = 'app/search_results_spoiled.html'

class SearchPageView(TemplateView):
    template_name = 'app/search.html'

class SearchResultsView(ListView):
    model = Spoiled
    template_name = 'app/search_results.html'
