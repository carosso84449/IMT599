from django.urls import path
from . import views
from .views import SearchPageView, SearchResultsView, SpoiledSearchPageView, SpoiledSearchResultsView

app_name = 'legacy'
urlpatterns = [
    path('spoiled/', views.index, name='spoiled'),
    path('submitted/', views.index2, name='submitted'),
    path("search_results/", SearchResultsView.as_view(), name="search_results"),
    path("", SearchPageView.as_view(), name="search_page"),
    path("search_results_spoiled/", SpoiledSearchResultsView.as_view(), name="search_results_spoiled"),
    path("", SpoiledSearchPageView.as_view(), name="search_page_spoiled"),
]
