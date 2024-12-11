from django.urls import path

from user import views  


urlpatterns = [
    path('login/', views.LoginView.as_view()),  
    path('verify-email/', views.VerifiyViews.as_view()),  
    path('resend-code/', views.ResendCodeView.as_view()),
]