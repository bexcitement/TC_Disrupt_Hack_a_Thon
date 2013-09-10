import requests

url = "http://api.shopstyle.com/api/v2/products?pid=uid8249-23662443-26"

def which_products(person, avgTemp):
	if person == 'Women':
		if avgTemp > 75:
			tank_args = {
			'fts': "tank tops",
			'cat': "womens-tops"
			}

			tops = requests.get(url, params=tank_args)

			print tops

			short_args = {
			'fts': "shorts",
			'cat': "shorts"
			}

			bottoms = requests.get(url, params=short_args)	

			sandal_args = {
			'fts': "sandals",
			'cat': "sandals"
			}

			frosting = requests.get(url, params=sandal_args)

		elif avgTemp > 50:
			long_args = {
			'fts': "long sleeve shirt",
			'cat': "longsleeve-tops"
			}

			tops = requests.get(url, params=long_args)

			pant_args = {
			'fts': "long pants",
			'cat': "casual-pants"
			}

			bottoms = requests.get(url, params=pant_args)	

			sneaker_args = {
			'fts': "tennis shoes",
			'cat': "womens-sneakers"
			}

			frosting = requests.get(url, params=sneaker_args)

		else:
			sweater_args = {
			'fts': "sweaters",
			'cat': "sweaters"
			}

			tops = requests.get(url, params=sweater_args)

			wool_args = {
			'fts': "woll pants",
			'cat': "womens-pants"
			}

			bottoms = requests.get(url, params=wool_args)	

			boot_args = {
			'fts': "leather boots",
			'cat': "boots"
			}

			frosting = requests.get(url, params=boot_args)

	if person == 'Men':	
		if avgTemp > 75:
			tank_args = {
			'fts': "tank tops",
			'cat': "mens-shirts"
			}

			tops = requests.get(url, params=tank_args)

			print tops

			short_args = {
			'fts': "shorts",
			'cat': "mens-shorts"
			}

			bottoms = requests.get(url, params=short_args)	

			sandal_args = {
			'fts': "sandals",
			'cat': "mens-sandals"
			}

			frosting = requests.get(url, params=sandal_args)

		elif avgTemp > 50:
			long_args = {
			'fts': "long sleeve shirt",
			'cat': "mens-longsleeve-shirts"
			}

			tops = requests.get(url, params=long_args)

			pant_args = {
			'fts': "long pants",
			'cat': "mens-chinos-and-khakis"
			}

			bottoms = requests.get(url, params=pant_args)	

			sneaker_args = {
			'fts': "tennis shoes",
			'ccat': "mens-sneakers"
			}

			frosting = requests.get(url, params=sneaker_args)

		else:
			sweater_args = {
			'fts': "sweaters",
			'cat': "mens-sweaters"
			}

			tops = requests.get(url, params=sweater_args)

			wool_args = {
			'fts': "woll pants",
			'cat': "mens-pants"
			}

			bottoms = requests.get(url, params=wool_args)	

			boot_args = {
			'fts': "leather boots",
			'cat': "mens-boots"
			}

			frosting = requests.get(url, params=boot_args)

	if person == 'Kids':	
		if avgTemp > 75:
			tank_args = {
			'fts': "tank tops",
			'cat': "girls-tops"
			}

			tops = requests.get(url, params=tank_args)

			short_args = {
			'fts': "shorts",
			'cat': "girls-shorts"
			}

			bottoms = requests.get(url, params=short_args)	

			sandal_args = {
			'fts': "sandals",
			'cat': "girls-shoes"
			}

			frosting = requests.get(url, params=sandal_args)

		elif avgTemp > 50:
			long_args = {
			'fts': "long sleeve shirt",
			'cat': "girls-tops"
			}

			tops = requests.get(url, params=long_args)

			pant_args = {
			'fts': "long pants",
			'cat': "girls-jeans"
			}

			bottoms = requests.get(url, params=pant_args)	

			sneaker_args = {
			'fts': "tennis shoes",
			'cat': "girls-shoes"
			}

			frosting = requests.get(url, params=sneaker_args)

		else:
			sweater_args = {
			'fts': "sweaters",
			'cat': "girls-sweaters"
			}

			tops = requests.get(url, params=sweater_args)

			wool_args = {
			'fts': "woll pants",
			'cat': "girls-jeans"
			}

			bottoms = requests.get(url, params=wool_args)	

			boot_args = {
			'fts': "leather boots",
			'cat': "girls-shoes"
			}

			frosting = requests.get(url, params=boot_args)

	return [tops.json(), bottoms.json(), frosting.json()]

