
from django.urls import path,include
from .views import article_list,GenericApiView,ArticleViewSet,article_detail,ArticleApiView,ArticleDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet,basename = 'article')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    path('article/' ,article_list, name='article_list' ),
    path('article/apiview/' ,ArticleApiView.as_view(), name='article_apiview_list' ),
    path('article/apidetail/<int:id>' ,ArticleDetails.as_view(), name='article_apiview_details' ),
    path('generic/article/<int:id>/' ,GenericApiView.as_view(), name='GenericApiView' ),
    
    path('detail/<int:pk>/' ,article_detail, name='article_detail' )
]
