from django.urls import path, re_path
from . import views

# urlpatterns = {
#     path('sum/<int:x>/', views.mysum),
#     path('sum/<int:x>/<int:y>/', views.mysum),
#     path('sum/<int:x>/<int:y>/<int:z>/', views.mysum),
# }

#
# urlpatterns = {
#     re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
# }


urlpatterns = {
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download)
}
