""" filtersets for applicable store models """

from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

from store.models import Brand


class BrandFilterSet(FilterSet):
    """filterset class for Brand"""

    # product = RelatedFilter("ProductFilterSet", field_name="product", queryset=Product.objects.all())
    has_product = BooleanFilter(field_name="product", lookup_expr="isnull", exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""

        model = Brand
        fields = {
            "created_at": "__all__",
            "enabled": "__all__",
            "id": "__all__",
            "name": "__all__",
            "updated_at": "__all__",
        }
