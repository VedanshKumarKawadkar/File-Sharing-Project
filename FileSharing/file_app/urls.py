from file_app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("test/", view=views.test, name="test"),
    path("", view=views.home, name="home"),
    path("login/", view=views.loginUser, name="login"),
    path("register/", view=views.registerUser, name="register"),
    path("user/", view=views.userHome, name="userhome"),
    path("user/send/", view=views.sendFiles, name="send files"),
    path("user/received_files/", view=views.receivedFiles, name="received files")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)