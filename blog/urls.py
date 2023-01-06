

from django.urls import path,include

from.views import CategoryView, BlogView #views den class ları import ediyoruz.

from rest_framework import routers 

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('blog', BlogView)

from.views import logout

urlpatterns = [

    path('', include(router.urls)),
    path('logout/', logout)
]
