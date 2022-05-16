from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Car_Project_Childish.api.urls')),
    path('base/', include('Car_Project_Childish.base.urls'))
]
