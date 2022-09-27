"""appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('logregc',views.logregc,name='logregc'),
    path('logregp',views.logregp,name='logregp'),
    path('cregs',views.cregs,name='cregs'),
    path('clogs',views.clogs,name='clogs'),
    path('pregs',views.pregs,name='pregs'),
    path('plogs',views.plogs,name='plogs'),
    path('req',views.req,name='req'),
    path('myappointments',views.myappointments,name='myappointments'),
    path('listsp',views.listsp,name='listsp'),
    path('approach/<id>',views.approach,name='approach'),
    path('apemail/<id>',views.apemail,name='apemail'),
    path('Logout',views.Logout,name='Logout'),
    path('admin/', admin.site.urls),
    path('accept/<id>',views.accept,name='accept'),
    path('decline/<id>',views.decline,name='decline'),
    path('upcomap',views.upcomap,name='upcomp'),
    path('complete/<id>',views.complete,name='complete'),
    path('ccomplete/<id>',views.ccomplete,name='ccomplete'),
    path('bookappointments',views.bookappointments,name='bookappointments'),
]
