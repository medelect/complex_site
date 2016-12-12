from django.conf.urls import url

from . import views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^color/(?P<clr>\w{3})$', views.color, name='color'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^posts2/$', views.posts2, name='posts2'),
    url(r'^psto/(?P<pid>\d{1,4})$',views.post_vs_comments, name='psto'),
    url(r'^input_post$',views.input_post, name='psto_in'),
    url(r'^start$',views.start, name='start'),
    url(r'^comments/(?P<pst_id>\d{1,3})$', views.ForumCommentView.as_view(),name='comments'),
    url(r'^user$', views.get_user ,name='user'),

]
