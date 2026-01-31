from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from authentication.views import UserView, account, CustomTokenObtainPairView, approve_user, pending_user, reject_user

urlpatterns = [
    path('signup/', UserView.as_view(), name="signup"),
    path('account/', account),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Processo de solicitação
    path("pending/", pending_user),
    path("<int:pk>/approve/", approve_user),
    path("<int:pk>/reject/", reject_user)
]