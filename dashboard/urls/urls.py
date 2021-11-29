from django.contrib import admin
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static 
from core.views import index_view, favorites_view, experiences_view, avatar_view, courses_view

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),
    
    # Index
    path('', index_view.index),

    # Avatar
    path('signin_page/', avatar_view.signin_page),
    path('signin', avatar_view.signin),
    path('signout/', avatar_view.signout),

    # Favorites
    path('dashboard/favorites/', favorites_view.favorites),
    path('dashboard/favorites/add', favorites_view.add_favorites),

    # Experiences
    path('dashboard/experiences/', experiences_view.experiences),
    path('dashboard/experiences/add', experiences_view.experiences_add),

    # Courses
    path('dashboard/courses/', courses_view.courses),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
