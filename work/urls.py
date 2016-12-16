from django.conf.urls import url
from work import views

urlpatterns = [
    url(r'^$', views.work, name='view_project'),
    # url(r'^view/(?P<slug>[^\.]+)', views.work_detail, name='view_project_detail'),
]
