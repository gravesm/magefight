from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fight import views


urlpatterns = [
    path("mages/", views.MageList.as_view()),
    path("mages/<int:pk>/", views.MageDetail.as_view()),
    path("spells/", views.SpellList.as_view()),
    path("spells/<int:pk>/", views.SpellList.as_view()),
    path("fights/", views.FightList.as_view()),
    path("fights/<int:pk>/", views.FightDetail.as_view()),
]

urlpatters = format_suffix_patterns(urlpatterns)
