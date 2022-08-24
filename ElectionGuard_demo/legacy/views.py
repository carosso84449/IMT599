# Pulls from model classes and directs pages to HTML templates
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Spoiled, Submitted

def index(request):
    data = Spoiled.objects.all()
    spoiled = {
        "spoiled_list": data
    }
    return render(request, "legacy/profile.html", spoiled)

def index2(request):
    data = Submitted.objects.all()
    submitted = {
        "submitted_list": data
    }
    return render(request, "legacy/profile2.html", submitted)

class SpoiledSearchPageView(TemplateView):
    template_name = 'legacy/search_spoiled.html'

class SpoiledSearchResultsView(ListView):
    model = Spoiled
    template_name = 'legacy/search_results_spoiled.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Spoiled.objects.filter(
            Q(ballot_id__icontains=query)
        )
        object_list = object_list.filter(
            Q(tally__icontains=1)
        )
        return object_list

class SearchPageView(TemplateView):
    template_name = 'legacy/search.html'

class SearchResultsView(ListView):
    model = Submitted
    template_name = 'legacy/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Submitted.objects.filter(
            Q(ballot_id__icontains=query)
        )
        return object_list