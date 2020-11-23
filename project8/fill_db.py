from myapp.models import Category, Products

sucrerie = Category.objects.create(name="sucrerie")
chocolat = Category.objects.create(name="chocolat")
condiments = Category.objects.create(name="condiments")
aperitif = Category.objects.create(name="aperitif")

nutella = Products.objects.create(name="nutella", palm_oil=True, gluten=True, stores="Leclerc", url="opfood/nutella.fr")
nustilabio = Products.objects.create(name="nustilabio", palm_oil=False, gluten=False, stores="Leclerc", url="opfood/nustilabio.fr")
dragibus = Products.objects.create(name="dragibus", palm_oil=False, gluten=False, stores="Intermarché", url="opfood/dragibus.fr")
ketchup = Products.objects.create(name="ketchup", palm_oil=False, gluten=True, stores="Leclerc", url="opfood/ketchup.fr")
tomate_grd = Products.objects.create(name="sauce tomate grand-mère", palm_oil=False, gluten=False, stores="Intermarché", url="opfood/tomate-grand-mere.fr")
duritos = Products.objects.create(name="duritos", palm_oil=True, gluten=True, stores="Leclerc", url="opfood/duritos.fr")
chips_bio = Products.objects.create(name="chips bio", palm_oil=False, gluten=False, stores="Intermarché", url="opfood/chips-bio.fr")

nutella.categories.add(sucrerie)
nutella.categories.add(chocolat)
nustilabio.categories.add(sucrerie)
nustilabio.categories.add(chocolat)
dragibus.categories.add(sucrerie)
ketchup.categories.add(condiments)
tomate_grd.categories.add(condiments)
duritos.categories.add(aperitif)
chips_bio.categories.add(aperitif)