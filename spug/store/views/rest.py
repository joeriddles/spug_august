""" DRF viewsets for applicable app models """

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from handyhelpers.drf_permissions import InAnyGroup

from store.models import Brand
from store.serializers import BrandSerializer
from store.filtersets import BrandFilterSet


class BrandViewSet(viewsets.ModelViewSet):
# class BrandViewSet(viewsets.ModelViewSet, InAnyGroup):
    """API endpoint that allows Brands to be viewed"""
    # permission_classes = (InAnyGroup,)
    # permission_dict = {'GET': ['blah'],
    #                    'POST': ['admin', 'orderers']}

    model = Brand
    queryset = model.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilterSet
