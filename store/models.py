from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    price = models.IntegerField()
    avaiable = models.BooleanField(default=True)
    describe = models.TextField()

    class Meta:
        db_table = 'product'


class Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.image_url

    class Meta:
        db_table = 'image'
