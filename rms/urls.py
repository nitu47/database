from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category',CategoryViewset)
router.register('food',Foodviewset)
urlpatterns = [
    #path("category/",CategoryViewset.as_view({'get':'list','post':'create','delete':'destroy'}))
    #path('category/',category.as_view()),
    #path('category/<id>/',category_detail.as_view()),
] + router.urls
