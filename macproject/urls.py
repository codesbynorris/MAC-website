"""
URL configuration for macproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from macapp.views import about, inventory_list, master_page, product_detail, product_list, shop_list, shopping_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('macapp.urls')),
    path('about/', about, name='about'),
    path('homepage/', product_list, name='homepage'),
    path('products_list/', shop_list, name='shopping_list' ),
    path('master', master_page),
    path('inventory/', inventory_list, name='inventory_list'),
    path('shopping/', shopping_list, name='shopping'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

