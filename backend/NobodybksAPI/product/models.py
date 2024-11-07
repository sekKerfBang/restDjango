from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(name__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            qs = qs.filter(user=user).filter(lookup) 
            # qs = (qs | qs_2 ).distinct()
        return qs
    

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_query_set().is_public().search(query, user)
class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    public = models.BooleanField(default=True)
    
    objects = ProductManager()
    
    @property
    def get_discount(self):
        return "%.2f"%(float(self.price) * 0.5)
    
    def __str__(self):
        return self.name