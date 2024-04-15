from django.urls import path
from habits.apps import HabitsConfig
from habits.views import CreateHabitsAPIView, ListHabitsAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', CreateHabitsAPIView.as_view(), name='create'),
    path('habits/list/', ListHabitsAPIView.as_view(), name='list'),
    path('habits/detail/<int:pk>/', DetailHabitsAPIView.as_view(), name='detail'),
    path('habits/update/<int:pk>/', UpdateHabitsAPIView.as_view(), name='update'),
    path('habits/delete/<int:pk>/', DeleteHabitsAPIView.as_view(), name='delete'),
    path('habits/user_list/', UserListHabitsAPIView.as_view(), name='user_list'),
    path('habits/public_list/', PublicListHabitsAPIView.as_view(), name='public_list'),
]
