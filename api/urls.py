from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AnimalList
swagger_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]

urlpatterns = [
       path('dogs/', AnimalList.as_view())
] + swagger_urlpatterns
