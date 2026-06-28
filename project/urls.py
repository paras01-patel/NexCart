from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.populer,name='populer'),
    path('jewellery/',views.jewellery,name='jewellery'),
    path('mobile/',views.mobile,name='mobile'),
    path('buynow/',views.buynow,name='buynow'),
    path('payment/',views.payment,name='payment'),
    path('setting/',views.setting,name='setting'),
    path('help/',views.help,name='help'),
    path('report/',views.report,name='report'),
    path('report_is/',views.report_is,name='report_is'),
    path('help_is/',views.help_is,name='help_is'),
    path('delete-report/<int:id>/', views.delete_report, name='delete_report'),
    path('delete-help/<int:id>/', views.delete_help, name='delete_help'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('adminpanel/',views.adminpanel,name='adminpanel')
    
    
]