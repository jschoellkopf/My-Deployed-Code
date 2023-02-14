from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('time_display', views.time)
    # path('blogs', views.index),
    # path('blogs/new', views.new),
    # path('blogs/create', views.create),
    # path('blogs/<int:id>', views.show),
    # path('blogs/<int:id>/edit', views.edit),
    # path('blogs/<int:id>/delete', views.destroy),
    # path('blogs/json', views.jsonrsps),
]