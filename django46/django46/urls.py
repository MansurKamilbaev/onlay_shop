from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import home_page, get_product_category_page, MyLoginView, logout_view, search_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('shop/<int:pk>', get_product_category_page, name='category_page'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('search', search_product, name='search-product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)