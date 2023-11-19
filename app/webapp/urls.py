from django.urls import path

from app.webapp.views import IndexView

urlpatterns = [
    # Urls de inicio
    path('', IndexView.as_view(), name="index"),
]
