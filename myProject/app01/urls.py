from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('chgpwd/', views.chgpwd_view),
    path('destroy/', views.destroy_view),
    # path('population_bar/', views.population_bar_options_view),
    # path('china/', views.china_view),
    # path('hebei/', views.hebei_view),
    # path('henan/', views.henan_view),
    # path('shandong/', views.shandong_view),
    # path('shanxi/', views.shanxi_view),
]