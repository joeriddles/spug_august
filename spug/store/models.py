from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


# register models with auditlog
# auditlog.register(MyModel)


class Brand(HandyHelperBaseModel):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name

    def disable(self):
        """disable this brand and all of its products"""
        self.enabled = False
        self.product_set.update(enabled=False)
        self.save()

    def get_absolute_url(self) -> str:
        return reverse("store:detail_brand", kwargs={"pk": self.pk})

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-solid fa-language"></i>"""

    def get_products(self):
        return self.product_set.all()
    
    # def get_orders(self):
    #     return Order.objects.filter(products__brand=self).select_related("status")

    # def get_orders_by_product(self):
    #     order_qs = self.get_orders().values('products__sku').annotate(qty=models.Count('products__sku'))
    #     return dict(
    #         id="orders_by_product",
    #         type="bar",
    #         label_list=[i['products__sku'] for i in order_qs],
    #         value_list=[i['qty'] for i in order_qs],
    #         list_view=f"/store/list_orders?products__brand__name={self.name}&products__sku=",
    #         color_list=get_colors(order_qs.count()),
    #     )

    # def get_orders_by_status(self):
    #     order_qs = self.get_orders().values('status__name').annotate(qty=models.Count('status__name'))
    #     return dict(
    #         id="orders_by_status",
    #         type="bar",
    #         label_list=[i['status__name'] for i in order_qs],
    #         value_list=[i['qty'] for i in order_qs],
    #         list_view=f"/store/list_orders?products__brand__name={self.name}&status__name=",
    #         color_list=get_colors(order_qs.count()),
    #     )


class Manufacturer(HandyHelperBaseModel):
    name = models.CharField(max_length=32, unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return ""
        # return reverse("store:detail_manufacturer", kwargs={"pk": self.pk})

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-solid fa-industry"></i>"""

    def disable(self):
        """disable this manufacturer and all of its brands and products"""
        self.enabled = False
        self.brand_set.update(enabled=False)
        for brand in self.brand_set.all():
            brand.product_set.update(enabled=False)
        self.save()

    def get_brands(self):
        return self.brand_set.all()

    # def get_orders(self):
    #     return Order.objects.filter(products__brand__manufacturer=self).select_related("status")

    # def get_orders_by_product(self):
    #     order_qs = self.get_orders().values('products__sku').annotate(qty=models.Count('products__sku'))
    #     print('TEST: ', order_qs)
    #     return dict(
    #         id="orders_by_product",
    #         type="bar",
    #         label_list=[i['products__sku'] for i in order_qs],
    #         value_list=[i['qty'] for i in order_qs],
    #         list_view=f"/store/list_orders?products__brand__manufacturer__name={self.name}&products__sku=",
    #         color_list=get_colors(order_qs.count()),
    #     )

    def get_products(self):
        return Product.objects.filter(brand__manufacturer=self)


class Product(HandyHelperBaseModel):
    sku = models.CharField(max_length=16, unique=True, blank=True, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, null=True)
    # attributes = models.ManyToManyField("ProductAttribute", blank=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.sku

    def get_absolute_url(self) -> str:
        return reverse("store:detail_product", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            if Product.objects.count() < 1:
                self.sku = "SKU-" + "1".zfill(8)
            else:
                self.sku = "SKU-" + str(Product.objects.count() + 1).zfill(8)
        super(Product, self).save(*args, **kwargs)

    @staticmethod
    def get_icon() -> str:
        return """<i class="fa-brands fa-product-hunt"></i>"""
    
