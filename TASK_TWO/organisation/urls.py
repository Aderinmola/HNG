from django.urls import path
from .views import OrganisationCreateView, SingleOrganisationView


urlpatterns = [
    path('', OrganisationCreateView.as_view(), name='organisation-create-get-all'),
    path('<str:pk>/', SingleOrganisationView.as_view(), name='get_organisation'),

]