import json

print("")
print("*************************************************************************")
print("*****************  Starting the application  ****************************")
#Input files which should be read to extract json objects from them.
products_file = open('./input/products.txt')
listings_file = open('./input/listings.txt')

#Create one output file in write mode, this will be required to dump Result objects once they are created.
output = open('./output/Result.txt','w')

# Create separete dictionaries for handling all products and listings respectively.
products = {}
listings = {}

i = 1

print("Extracting products information...")
# Extract all the products in one single dictionary so as to create nested JSON structure for better understanding.
for line in products_file:
    j = json.loads(line)
    products[i] = j
    i = i+1

i = 1

print("Extracting listings information...")
#Extract all the listings as dictionaries into one dictionary
for line in listings_file:
    j = json.loads(line)
    listings[i] = j
    i = i+1

#Closing these files, because we have extracted information from them.
products_file.close()
listings_file.close()

#A dictionary to hold Manufacturer Based classification of Products. 
organized_products = {}

# The following loop will fill the above created dictionary. 
# It will create a Classification in products on the base of Brand name.
# This organized dictionary will look like this:
#   { {"Brand_1":{"model1":"product_name1", "model2":"product_name2", ...},
#     {"Brand_2":{"model1":"product_name1", "model2":"product_name2", ...},
#     ...
#   }
print("Visualizing products under a brand name...")
for key in range(1,len(products)):
    if products[key]['manufacturer'] not in organized_products:
        organized_products[products[key]['manufacturer']] = {}

    organized_products[products[key]['manufacturer']][products[key]['model']] = products[key]['product_name']

# A dictionary to hold Manufacturer or Brand based classifications of listings.
organized_listings = {}

# Following loop serves as a filter in listings dictionary. 
# It extracts all the listings into organized_listings wherever the title has a brand name in it.
# This listing will organize every listing present in listings under a brand name.
#
print("Visualizing listings under respective brand names and filtering unnecessary listings...")
for brand in organized_products:
    if brand not in organized_listings:
        organized_listings[brand] = []
    
    for list in listings:
        if brand in listings[list]['title']:
            organized_listings[brand].append(listings[list])

# Sort the keys of listings because it will be required to iterate over both dictionaries.
sorted_keys = sorted(organized_listings.keys())

# Following loop further compares the 2 equally sized organized_products and organized_listings dictionaries and extracts 
# the required listings under one product_name and sends it to result structure.
print("Filtering all the listings on the basis of products...")
for brand in sorted_keys:
    for model in organized_products[brand]:
	    # Create a result object against every 'product_name'
        result = {'product_name':organized_products[brand][model], 'listings':[] }

        for listing in range(len(organized_listings[brand])):
		    # This if condition serves as the best filter, which selects listings by matching both 'model' and 'manufacturer' which is important.
            if model in organized_listings[brand][listing]['title'] and brand in organized_listings[brand][listing]['manufacturer']:
                #Populate the result object according to above filter.
                result['listings'].append(organized_listings[brand][listing])
                output.write(json.dumps(result)+"\n")
				
output.close()
print("Job Completed !")
