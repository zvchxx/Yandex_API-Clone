from django.urls import path
from basket import views

app_name = 'basket'

urlpatterns = [
    path('', views.BasketView.as_view(), name='basket'),
    path('submit/', views.ChangeBasketStatusView.as_view(), name='basket_submit'),
]
