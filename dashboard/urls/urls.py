from django.contrib import admin
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static 
from core.views import index_view, favorites_view, experiences_view, avatar_view, course_view, tutorial_view, technology_view

urlpatterns = [
    # Admin URL's
    path('admin/', admin.site.urls),

    # Sigin
    path('login_page/', index_view.login_page),
    path('logout_page/', index_view.logout_page),
    path('signin', index_view.sigin_page),
    
    # Index
    path('', index_view.index),

    # Avatar
    # path('signin_page/', avatar_view.signin_page),
    # path('signin', avatar_view.signin),
    # path('signout/', avatar_view.signout),

    # Favorites
    path('dashboard/favorites/', favorites_view.favorites),
    path('dashboard/favorites/add', favorites_view.favorites_add),

    # Experiences
    path('dashboard/experiences/', experiences_view.experiences),
    path('dashboard/experiences/add', experiences_view.experiences_add),

    # Courses
    path('dashboard/courses/', course_view.courses),
    path('dashboard/courses/add', course_view.courses_add),

    # Technology
    path('dashboard/technologias/', technology_view.technology),
    path('dashboard/technologias/add', technology_view.technology_add),

    # Tutorials
    path('dashboard/tutorials/', tutorial_view.tutorial),
    path('dashboard/tutorials/add/', tutorial_view.tutorial_add),
    path('dashboard/tutorials/markdown', tutorial_view.tutorial_preview),
    path('dashboard/tutorials/record', tutorial_view.tutorial_record),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
