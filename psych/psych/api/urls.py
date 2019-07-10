from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userView.as_view()),
    path('title/', views.title.as_view()),
    path('title_c/', views.title_c.as_view()),
    path('title/<int:pk>/', views.detailtitle.as_view()),
    path('users/', views.user_reg.as_view()),
    path('users/update/<int:pk>/', views.updateUser.as_view()),
    path('users/<int:pk>/', views.user_detail.as_view()),
    path('users_c/<int:pk>/', views.user_detail_c.as_view()),
    path('profile/', views.profile.as_view()),
    path('profile/<int:pk>/', views.profiledetail.as_view()),
    path('answers/', views.answer),
    path('okanswer/<int:pk>/', views.okanswer.as_view()),
    path('question/<int:pk>/', views.question.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('user_result/', views.results.as_view()),
    path('user_result_f/', views.results_fbv),
    path('users_f/', views.user_reg_f),
    path('user/<int:pk>/result/', views.userresult.as_view())

]