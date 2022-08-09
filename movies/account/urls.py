from django.urls import path


from movies.account.views import RegisterView, ActivationView, LoginView, ChangePasswordView, LogOutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('active/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('logout/', LogOutView.as_view())]

