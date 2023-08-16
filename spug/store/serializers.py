""" DRF serailizers for applicable store models """

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from store.models import Brand


class BrandSerializer(FlexFieldsModelSerializer):
    """serializer class for Brand"""

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = [
            "created_at",
            "enabled",
            "id",
            "name",
            "updated_at",
        ]
