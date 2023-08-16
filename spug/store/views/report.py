""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView

# from handyhelpers.views.report import get_colors

# import models
# from store.models import ()


class storeDashboard(View):
    """store dashboard"""

    template_name = "store/custom/dashboard.html"

    def get(self, request):
        """render dashboard for store specific data"""
        context = {"title": "store Dashboard"}
        return render(request, self.template_name, context=context)


class storeAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/store/list_models",
        # ),
    ]


class storeAnnualStatView(AnnualStatView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/store/list_models",
        # ),
    ]


class storeAnnualTrendView(AnnualTrendView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/store/list_models",
        # ),
    ]
