from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Title(models.Model):
    title = models.CharField(max_length=200)
    context = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    context = models.TextField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Products1(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    context = models.TextField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Goods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
