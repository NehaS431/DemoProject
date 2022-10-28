from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('base.api.urls')),
    path('academics/',include('academics.urls'))
]
