from django.shortcuts import render
from django.views.generic import DetailView, View

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView

from store.models import Brand


class Index(HandyHelperIndexView):
    """render the store index page"""

    title = """store"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/store/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for store ",
        },
        {
            "url": "/store/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for store",
        },
    ]
    protected_item_list = []
    protected_group_name = "admin"


class ListBrands(HandyHelperListPlusCreateAndFilterView):
    """list available Brand entries"""
    queryset = Brand.objects.all().select_related("manufacturer")
    title = "Brands"
    table = "store/table/brands.htm"


class DetailBrand(DetailView):
    model = Brand
    template_name = 'storemgr/detail/brand.html'


# class ListMyModels(HandyHelperListPlusCreateAndFilterView):
#     """list available MyModel entries"""
#     queryset = MyModel.objects.all()
#     title = "MyModel"
#     table = "myapp/table/mymodels.htm"


# class DetailMyModel(DetailView):
#     model = MyModel
#     template_name = 'myapp/detail/mymodel.html'
