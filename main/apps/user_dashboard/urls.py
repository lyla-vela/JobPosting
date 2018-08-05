from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^new_registration$', views.new_registration),
    url(r'^new/(?P<id>\d+)$', views.new),
    url(r'^go_dashboard$', views.go_dashboard),
    url(r'^all_users$', views.all_users),
    url(r'^validate_login$', views.validate_login),
    url(r'^logout$', views.logout),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^add_job/(?P<id>\d+)$', views.add_job),
    url(r'^(?P<id>\d+)/edit$', views.edit),
     url(r'^users/(?P<id>\d+)/add$',views.add),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^show_jobs/(?P<id>\d+)$',views.show_jobs),
    url(r'^update/(?P<id>\d+)$',views.update),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^all_users/(?P<id>\d+)/edit$',views.edit),
    url(r'^all_users/(?P<id>\d+)/add$',views.add_job),
    url(r'^new/(?P<id>\d+)/add$',views.add_job),
    url(r'^post_quote/(?P<id>\d+)$',views.post_quote),
    url(r'^all_users/(?P<id>\d+)/show$',views.show),
    url(r'^users/(?P<id>\d+)$',views.go_dashboard),
    url(r'^all_users/(?P<id>\d+)/destroy$',views.destroy),
 
] 