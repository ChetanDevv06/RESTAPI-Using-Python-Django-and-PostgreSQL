from django.urls import path
from .views import SimpleHelloWorld,SimpleHelloPerson

urlpatterns = [
    path('hello1/', SimpleHelloWorld.as_view(), name='hello-view1'),
    path('hello2/<str:name>/', SimpleHelloPerson.as_view(), name='hello-view2'),
]