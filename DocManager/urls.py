from django.contrib import admin
from django.urls import path, include
from doc_manager_app.urls import doc_manager

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc_manager/', include((doc_manager.urls, 'doc_manager_app'), namespace='doc_manager_app'))
]
