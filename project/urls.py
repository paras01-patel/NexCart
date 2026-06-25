from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.populer,name='populer'),
    path('jewellery/',views.jewellery,name='jewellery'),
    path('mobile/',views.mobile,name='mobile'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('adminpanel/',views.adminpanel,name='adminpanel')
    
    
]