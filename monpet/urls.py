from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('', include('store.urls')),
]
