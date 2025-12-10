from django.contrib import admin
from django.urls import include, path

import Beauty.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Beauty/', include('Beauty.urls'))

]
