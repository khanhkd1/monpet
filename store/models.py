from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    price = models.IntegerField()
    avaiable = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.image_url

    class Meta:
        db_table = 'image'
