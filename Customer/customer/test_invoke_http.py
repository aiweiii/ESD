from invokes import invoke_http
from os import environ

customer_URL = environ.get('customerURL') or input("Enter Customer service URL: ")  

# invoke book microservice to get all books
results = invoke_http(customer_URL, method='GET')

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
custID = 'A04'
cust_details = { "custCCNo": 978112947, "custAddress": 'Blk 145 Lorong 2 Toa Payoh Singapore 310145', "custName": "Tom Holland" }
create_results = invoke_http(
        customer_URL + "/" + custID, method='POST', 
        json=cust_details
    )

print()
print( create_results )
