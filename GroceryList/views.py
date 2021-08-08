from django.shortcuts import render, HttpResponse

from .utils import *
from .models import *


# Create your views here.

def home(request):
    logger.info("home request method:  %s", str(request.method))
    logger.info("home request user:  %s", str((request.user)))
    if not request.user.is_anonymous:
        logger.info("home request:  %s", str(request.POST))
        user = User.objects.get(email=str(request.user))
        items = []
        active_lists = []
        list_categories = ListCategory.objects.all()
        context = {
            'user':user,
            'products':items,
            'active_lists':active_lists,
            'list_categories':list_categories
        }
        return render(request, 'GroceryList/index.html', context=context)
    else:
        return HttpResponse("You need to login first.", status=401)


def products(request, category=None):
    if not request.user.is_anonymous:
        user = User.objects.get(email=str(request.user))
        logger.info("products category:  %s", str(category))

        item_categories = ItemCategory.objects.all()


        list_categories = ListCategory.objects.all()
        active_lists = []
        context = {
            'user':user,
            'product_categories':item_categories,
            'active_lists':active_lists,
            'list_categories':list_categories
        }
        return render(request, 'GroceryList/products.html', context=context)
    else:
        return HttpResponse("You need to login first.", status=401)


def products_under_category(request, category_id=None):
    if not request.user.is_anonymous:
        user = User.objects.get(email=str(request.user))
        logger.info("products category id:  %s", str(category_id))

        if category_id != None:
            item_category = ItemCategory.objects.get(pk=category_id)
            items = Item.objects.filter(user=user, category=item_category)
        logger.info("products:  %s", str(items))

        list_categories = ListCategory.objects.all()
        active_lists = []
        context = {
            'user':user,
            'product_category':item_category,
            'products':items,
            'active_lists':active_lists,
            'list_categories':list_categories
        }
        return render(request, 'GroceryList/products_under_category.html', context=context)
    else:
        return HttpResponse("You need to login first.", status=401)
