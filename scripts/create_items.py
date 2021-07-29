from GroceryList.models import *
from django.contrib.auth import get_user_model
import requests
import json

User = get_user_model()
admin = User.objects.get(pk=1)

# Adding Fruits
category_name = "Fruits & Vegetables"
category_obj = ItemCategory.objects.filter(name=category_name)[0]

fruit_api = requests.get("https://www.fruityvice.com/api/fruit/all")
fruit_api_content = json.loads(fruit_api.text)
fruit_name_list = []
for fruit in fruit_api_content:
    fruit_name_list.append(fruit["name"].strip().capitalize())
    print(fruit)
    fruit_name =fruit["name"].strip().capitalize()
    items = Item.objects.filter(category=category_obj, name=fruit_name)
    print(items , end="\n")
    if items.count() == 0:
        item = Item.objects.create(user=admin, category=category_obj, name=fruit_name)
    else:
        item = items[0]
        item.user = admin
        item.save()
