#首先是配置应用层面的路由
from django.urls import path, include
import blog.views

urlpatterns = [
    path('index', blog.views.get_index_page),
    path('detail/<int:article_id>', blog.views.get_detail_page)

]