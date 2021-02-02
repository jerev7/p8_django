from django.test import TestCase
from django.urls import reverse
from .models import Category, Products, Product_saved

# Create your tests here.



# Index page
class IndexPageTestCase(TestCase):
    def SetUp(self): # create data before tests start
        testcategory = Category.objects.create(name="testcategory")
        testproduct = Products.objects.create(name="testproduct",
                                         nutriscore=4,
                                         nutriscore_complete_url="myapp/assets/img/nutriscore/nutricomplet_e.png")



    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# Search page


# Result page


# Save product


# Delete product


# Create an account


# Login


# Logout