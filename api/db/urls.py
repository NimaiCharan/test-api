
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('^$', views.index),
    path('data/', views.test),
    path('data/<int:pk>', views.getdata),
    # path('api/v1/', include(api_urlpatterns)),
]