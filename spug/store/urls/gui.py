from django.urls import path
from store.views import gui
from store.views import report


urlpatterns = [
    # GUI views
    path("", gui.Index.as_view(), name=""),
    path("index", gui.Index.as_view(), name="index"),
    path("default", gui.Index.as_view(), name="default"),
    path("home", gui.Index.as_view(), name="home"),
    # list views
    # path("list_mymodels/", gui.ListMymodels.as_view(), name="list_mymodels"),
    path("brands/", gui.ListBrands.as_view(), name="list_brands"),
    # detail views
    # path("detail_mymodel/<int:pk>", gui.DetailMymodel.as_view(), name="detail_mymodel"),
    path("brand/<int:pk>", gui.DetailBrand.as_view(), name="detail_brand"),
    # report views
    path("dashboard/", report.storeDashboard.as_view(), name="dashboard"),
    path("annual_progress/", report.storeAnnualProgressView.as_view(), name="annual_progress"),
    path("annual_stats/", report.storeAnnualStatView.as_view(), name="annual_stats"),
    path("annual_trends/", report.storeAnnualTrendView.as_view(), name="annual_trends"),
]
