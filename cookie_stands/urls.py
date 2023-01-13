from django.urls import path
from .views import CookieStandList, CookieStandDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="CookieStand_detail"),
    # path("<slug:slug>/", CookieStandDetail.as_view(), name="CookieStand_detail"),
]
