from myapp.models import Category, Products
import requests


"""
code working for this url :
url = https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes/1.json

"""
def get_product(category, url):
	
	final_list = []

	nutrition_grade_list = ["a", "b", "c", "d", "e"]
	response = requests.get(url)
	my_products = response.json()["products"]
	# i = 0
	for product in my_products:
		if 'product_name_fr' in product and product["product_name_fr"] != "":
			new_entry = {}
			new_entry["name"] = product["product_name_fr"]
			new_entry["category"] = category
			if "nutrition_grades" in product:
				new_entry["nutriscore"] = nutrition_grade_list.index(product["nutrition_grades"])
			else:
				new_entry["nutriscore"] = 4
			if "image_front_url" in product:
				new_entry["image_url"] = product["image_front_url"]
			else:
				new_entry["image_url"] = "{% static 'myapp/assets/img/image_not_found.png' %}"
			# i += 1
			# new_entry["compte"] = i
			final_list.append(new_entry)
	return final_list


# def printme(stuffs):
# 	print(stuffs)


# printme(get_product("pates-a-tartiner-aux-noisettes", "https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes/1.json"))


def add_products_to_db(product_list):
	for element in product_list:
		new_product = Products.objects.create(name=element["name"], nutriscore=element["nutriscore"], image_url=element["image_url"])
		category_check = Category.objects.filter(name=element["category"])
		if not category_check.exists():
			category = Category.objects.create(name=element["category"])
		else:
			category = category_check[0]
		new_product.categories.add(category)


add_products_to_db(get_product("pates-a-tartiner-aux-noisettes", "https://fr.openfoodfacts.org/categorie/pates-a-tartiner-aux-noisettes/1.json"))
