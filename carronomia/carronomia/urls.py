from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include


# Serializers define the API representation.
from . import views, settings

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<str:busqueda>/', views.scrape, name='scrape'),
    path('<str:busqueda>/<int:year>/stats/', views.stats, name='promedio'),

]
