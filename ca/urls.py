from django.conf.urls import patterns, url
from ca import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        url(r'^articles/$', views.articles, name = 'articles'),
        url(r'^search/$', views.search, name = 'search'),
        url(r'^register/$', views.register, name = 'register'),
        url(r'^login/$', views.user_login, name = 'login'),
        url(r'^logout/$', views.user_logout, name = 'logout'),
        url(r'^profile/$', views.profile, name = 'profile'),
        url(r'^edit_profile/$', views.edit_profile, name = 'edit_profile'),
        url(r'^program_search/$', views.program_search, name = 'program_search'),
        url(r'^program_detail/(?P<program_id>\d+)/$', views.program_detail, name = 'program_detail'),
        # url(r'^program_detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name = "program_detail"),
        )
