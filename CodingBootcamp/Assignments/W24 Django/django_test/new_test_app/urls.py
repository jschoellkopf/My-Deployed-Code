from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:id>', views.show),
    path('blogs/<int:id>/edit', views.edit),
    path('blogs/<int:id>/delete', views.destroy),
    path('blogs/json', views.jsonrsps),

    # path('bears', views.one_method),                        # would only match localhost:8000/bears
    # path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
    # path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    # path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
    # path('', views.root_method),
    # path('another_route', views.another_method),
    # path('redirected_route', views.redirected_method)
]
