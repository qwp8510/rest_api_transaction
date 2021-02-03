from django.urls import path, include


urlpatterns = [
    path('', include('fund.urls')),
    path('api/', include('djoser.urls.authtoken')),
]
