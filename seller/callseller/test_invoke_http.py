from invokes import invoke_http
from os import environ

seller_URL = environ.get('sellerURL') or input("Enter Seller service URL: ")  

# invoke seller microservice to get all seller
results = invoke_http(seller_URL, method='GET')

print( type(results) )
print()
print( results )