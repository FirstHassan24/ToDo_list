from django.urls import path
from . import views
urlpatterns = [
    path("",views.board_categorys,name="board"),
    path("new/",views.create_list,name="create")
]