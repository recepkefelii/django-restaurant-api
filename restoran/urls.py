from django.urls import path
from restoran.views import RestoranAPIView,MenuanAPIView

urlpatterns = [
    path('create/restoran/',RestoranAPIView.as_view(),name='restoran_create'),
    path('create/menu/',MenuanAPIView.as_view(),name='menu_create')
]
