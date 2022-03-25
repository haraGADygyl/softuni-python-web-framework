from django.urls import path

from tests_demo.web.views import ProfileCreateView, ProfilesListView, ProfileDetailsView

urlpatterns = (
    path('', ProfilesListView.as_view(), name='list profiles'),
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='details profile'),
)
