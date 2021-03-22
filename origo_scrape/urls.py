from django.urls import path
from .views import index, start_scrape, get_scraping_status

urlpatterns = [
    path('', index, name="home"),
    path('start_scrape/', start_scrape, name="start_scrape"),
    path('get_scraping_status/', get_scraping_status, name="get_scraping_status"),
    # path('stores/',stores_views.detail,{'location':'headquarters'})
    # path('start_scrape/<str:scrape_type>/<str:site>', start_scrape, name="start_scrape"),
    # path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout")
]
