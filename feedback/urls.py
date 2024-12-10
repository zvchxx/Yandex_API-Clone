from rest_framework.routers import DefaultRouter
from feedback.views import FeedbackViewSet

router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')

urlpatterns = [
    
]

urlpatterns += router.urls