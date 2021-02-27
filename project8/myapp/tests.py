from django.test import TestCase
from django.urls import reverse
from .models import Category, Products, Product_saved
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your tests here.

testproduct = ""
testproduct2 = ""

def setting_up_db():
    testcategory = Category.objects.create(name="testcategory")
    testproduct = Products.objects.create(name="testproduct",
                                     nutriscore=4,
                                     image_url="/",
                                     url_offacts="/",
                                     energy_value=24.2,
                                     energy_unit="kcal",
                                     sugars_100g=12.1,
                                     fat_100g=2,
                                     saturated_fat_100g=1.2,
                                     proteins=4,
                                     nutriscore_complete_url="myapp/assets/img/nutriscore/nutricomplet_e.png",
                                     nutriscore_letter_url="myapp/assets/img/nutriscore/nutrilettre_e.png")
    testproduct2 = Products.objects.create(name="testproduct2",
                                     nutriscore=3,
                                     image_url="/",
                                     url_offacts="/",
                                     energy_value=24.2,
                                     energy_unit="kcal",
                                     sugars_100g=12.1,
                                     fat_100g=2,
                                     saturated_fat_100g=1.2,
                                     proteins=4,
                                     nutriscore_complete_url="myapp/assets/img/nutriscore/nutricomplet_d.png",
                                     nutriscore_letter_url="myapp/assets/img/nutriscore/nutrilettre_d.png")
    testproduct.categories.add(testcategory)
    testproduct2.categories.add(testcategory)
    user = User.objects.create(username="Bob", email="bob@gmail.com", password="bobby")
    
    # savedproduct = Product_saved.objects.create(product_selected=testproduct, substitution_product=testproduct2, user=user)


# Index page
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# Search page
class SearchPageTestCase(TestCase):
    def setUp(self): # create data before tests start
        setting_up_db()

    def test_search_page_product_found(self):
        response = self.client.get(reverse('search'), {'query': 'testproduct'})
        self.assertEqual(response.status_code, 200)

    def test_search_page_product_not_found(self):
        response = self.client.get(reverse('search'), {'query': 'huhuhuhu'})
        self.assertEqual(response.status_code, 404)

# Result page
class ResultPageTestCase(TestCase):
    def setUp(self): # create data before tests start
        setting_up_db()

    def test_result_page_product_found(self):
        myproduct = Products.objects.get(name="testproduct")
        product_id = myproduct.id
        response = self.client.get(reverse('results', args=(product_id,)))
        self.assertEqual(response.status_code, 200)


# Product detail
class DetailPageTestCase(TestCase):
    def setUp(self): # create data before tests start
        setting_up_db()

    def test_detail_page_product_found(self):
        myproduct = Products.objects.get(name="testproduct")
        product_id = myproduct.id
        response = self.client.get(reverse('product_detail', args=(product_id,)))
        self.assertEqual(response.status_code, 200)

# Save and delete a product
class SaveProductPageTestCase(TestCase):
    def setUp(self): # create data before tests start
        setting_up_db()

    def test_saveanddelete_product_page(self):
        self.client.force_login(user=User.objects.get(username='Bob'))
        saved_products = Product_saved.objects.all()
        products_number_before = len(saved_products)
        product_to_save_selected = Products.objects.get(name="testproduct")
        product_to_save_selected_id = Products.objects.get(name="testproduct").id
        product_to_save_substitution = Products.objects.get(name="testproduct2")
        product_to_save_substitution_id = Products.objects.get(name="testproduct2").id
        # Saving new product
        response = self.client.get(reverse('save_product', kwargs={'product_selected_id': product_to_save_selected_id, 'substitution_id': product_to_save_substitution_id}))
        self.assertEqual(response.status_code, 302)

        saved_products_after = Product_saved.objects.all()
        products_number_after = len(saved_products_after)
        self.assertEqual(products_number_after, (products_number_before + 1))

        # Deleting new product
        new_product_saved = Product_saved.objects.get(product_selected=product_to_save_selected, 
                                                      substitution_product=product_to_save_substitution,
                                                      user=User.objects.get(username='Bob'))
        response2 = self.client.get(reverse('delete_product', args=(new_product_saved.id,)))
        self.assertEqual(response2.status_code, 302)
        products_number_finally = len(Product_saved.objects.all())
        self.assertEqual(products_number_finally, products_number_before)

# Create an account


# Login


# Logout