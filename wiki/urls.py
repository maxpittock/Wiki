from django.urls import path, include

from . import views
app_name = 'wiki'


urlpatterns = [
    #navigatin for all pages
    path('', views.IndexView.as_view(), name='index'), 
    path('error', views.error_test, name='error_test'),
    path('upload/', views.upload_file, name='upload_page' ), 
    path('<str:pk>/edit', views.edit_page, name='edit_page'),
    path('<str:pk>/save', views.save_page, name='save_page'),
    path('<str:pk>/', views.view_page, name='detail'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]