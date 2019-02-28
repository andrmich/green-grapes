from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    SkillListView,
    )

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name ='home'),
    path('skill/', SkillListView.as_view(), name ='skill'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
