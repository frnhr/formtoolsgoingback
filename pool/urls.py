from django.urls import path
from . import views

wizard = views.WizardView.as_view(
    views.FORMS,
    url_name='wizard',
    done_step_name='done'
)

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'wizard/<step>/', wizard, name='wizard'),
    path(r'done/<pk>/', views.DoneView.as_view(), name='done'),
]

