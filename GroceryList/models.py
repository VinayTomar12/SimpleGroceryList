from django.contrib import admin
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db import models
from django.conf import settings

#   Grocery User
User = settings.AUTH_USER_MODEL


#   Item Category
class ItemCategory(models.Model):
    name             = models.CharField(max_length=50)
    description      = models.TextField(null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item Category"
        verbose_name_plural = "Item Categories"

    def __str__(self):
        return self.name


#   Item Quantity
class ItemQuantity(models.Model):
    name         = models.CharField(max_length=10)
    description  = models.TextField()

    class Meta:
        verbose_name = "Item Quantity"
        verbose_name_plural = "Item Quantities"

    def __str__(self) -> str:
        return self.name

#   Item
class Item(models.Model):
    user         = models.ForeignKey(User, related_name="created_by", on_delete=SET_NULL, null=True)
    category     = models.ForeignKey(ItemCategory, on_delete=SET_NULL, null=True, blank=True)
    name         = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


#   Buying List Category
class ListCategory(models.Model):
    name             = models.CharField(max_length=50)
    description      = models.TextField(null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "List Category"
        verbose_name_plural = "List Categories"

    def __str__(self):
        return self.name


#   Buying List
def default_buyinglist_name():
    from django.utils import timezone
    today = timezone.now()
    date_str = today.strftime("%Y%m%d_%H%M%S")
    return "List_"+str(date_str)

class BuyingList(models.Model):
    user         = models.ForeignKey(User, on_delete=CASCADE)
    category     = models.ForeignKey(ListCategory, on_delete=SET_NULL, null=True, blank=True)
    name         = models.CharField(max_length=50, default=default_buyinglist_name)
    is_completed = models.BooleanField(default=False)
    is_deleted   = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)    

    class Meta:
        verbose_name = "Buying List"
        verbose_name_plural = "Buying Lists"

    def list_user(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.name


#   Buying List Item
def set_default_quantity():
    quantity_objs = ItemQuantity.objects.filter(name="unit")
    if quantity_objs.count() == 0:
        return ItemQuantity.objects.create(name="unit")
    else:
        return quantity_objs[0]

class BuyingListItem(models.Model):
    buying_list      = models.ForeignKey(BuyingList, on_delete=CASCADE, null=True)
    # item_category    = models.ForeignKey(ItemCategory, on_delete=SET_NULL, null=True, blank=True)
    # item_name        = models.CharField(max_length=200)
    item             = models.ForeignKey(Item, on_delete=CASCADE)
    quantity         = models.FloatField(default=1)
    quantity_name    = models.ForeignKey(ItemQuantity, on_delete=SET_DEFAULT, default=set_default_quantity)
    is_purchased     = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)    

    class Meta:
        verbose_name = "Buying List Item"
        verbose_name_plural = "Buying List Items"

    def display_list_name(self):
        return self.buying_list.name

    def display_item_quantity(self):
        from fractions import Fraction
        return str(Fraction(self.quantity))

    def display_list_item(self):
        return self.item.name + " " +  str(self.display_item_quantity()) + " " + str(self.quantity_name)        

    def __str__(self):
        return self.item.name + " " +  str(self.display_item_quantity()) + " " + str(self.quantity_name)