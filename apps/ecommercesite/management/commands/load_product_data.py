from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from apps.ecommercesite.models import Category
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

Category_NAMES = {
    "name": 'Men\'s Dresses',    "is_subcategory":True   ,  "is_active" :True,
    "name": 'Women\'s Dresses',    "is_subcategory":True   ,  "is_active" :True,
    "name": 'Baby\'s Dresses',     "is_subcategory":True   ,  "is_active" :True,
    "name": 'Shirts',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Jeans',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Swimwear',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Sleepwear',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Sportswear',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Jumpsuits',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Blazers',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Jackets',    "is_subcategory":False  ,  "is_active" :False,
    "name": 'Shoes',    "is_subcategory":False  ,  "is_active" :False,
}




ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from product_data.csv into our Product model"

    def handle(self, *args, **options):
        #  if Category.objects.exists() :
        #      print('Product data already loaded...exiting.')
        #      print(ALREDY_LOADED_ERROR_MESSAGE)                        
                 
        #      print("Creating category data")
             for category_name, in Category_NAMES.items():
                print(category_name[1])
                # cat = Category(name=category_name['name'],
                #                issubclass=category_name['is_subcategory'],
                #                is_active=category_name['is_active'])
                # cat.save()
        # print("Loading product data for pets available for adoption")
        # for row in DictReader(open('./product_data.csv')):
        #     prod = Product()
        #     prod.name  = row['name']
        #     prod.price = row['price']
        #     prod.digital = row['digital']
        #     prod.image = row['image']          
        #     prod.description = row['description']                     
        #     prod.save()
        #     raw_category_names = row['category']
        #     category_names = [name for name in raw_category_names.split('| ') if name]
        #     print(category_names)
        #     for c_name in category_names:
        #         cat_Name = Category.objects.get(name=c_name)
        #         prod.category.add(cat_Name)
        #     prod.save()
