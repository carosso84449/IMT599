from django.urls import path
from . import views
from .views import SearchPageView, SearchResultsView, SpoiledSearchPageView, SpoiledSearchResultsView

app_name = 'app'
urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", SearchPageView.as_view(), name="search_page"),
    path("search_results_spoiled/", SpoiledSearchResultsView.as_view(), name="search_results_spoiled"),
    path("search_spoiled/", SpoiledSearchPageView.as_view(), name="search_page_spoiled"),
]
