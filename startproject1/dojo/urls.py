from django.urls import path, re_path
from . import views
from . import views_cbv


app_name = 'dojo'
# urlpatterns = {
#     path('sum/<int:x>/', views.mysum),
#     path('sum/<int:x>/<int:y>/', views.mysum),
#     path('sum/<int:x>/<int:y>/<int:z>/', views.mysum),
# }

#
# urlpatterns = {
#     re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
# }


# urlpatterns = {
#     path('list1/', views.post_list1),
#     path('list2/', views.post_list2),

#     path('excel/', views.excel_download)
# }

urlpatterns = [
    path('cbv/list1/', views_cbv.post_list1, name="dojo"),
    path('list3/', views.post_list3),
    path('cbv/list2/', views_cbv.post_list2),
    path('new/', views.post_new),
    path('<int:id>/edit/', views.post_edit),
    # path('cbv/list2/', views_cbv.post_list2),
    # path('cbv/list3/', views_cbv.post_list3),
    # path('cbv/excel/', views_cbv.excel_download),
]

