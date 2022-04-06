async function getCust(user) {           
    // Change serviceURL to your own
    var customerURL = "http://localhost:9292/customers";
    var findCustomer = customerURL + '/' + user ;
    console.log(findCustomer)
    
    try {
        const response =
        await fetch(
            findCustomer, 
            { method: 'GET' }
        );
        
        const result = await response.json();
        console.log(result)

        if (response.status === 200) {
        
            var custID = result.data.custID;
            console.log( result.data.custAddress)
            getOrders(custID);
            
            } 
        
        else if (response.status == 404) {
            const createResponse = await createCustomer('', '{{user}}');

            console.log(createResponse.json().custID)

        }

        else {
            throw response.status;
        }

    } catch (error) {
        showError(error);
    }
};

function showError(message) {
// Hide the table and button in the event of error
$('#orderTable').hide();

// Display an error under the main container
$('#main-container')
    .append(
        "<div class='container-sm pt-3'>" +
        message + 
        "</div>"
        );
}

async function createCustomer(address, name){
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "custAddress": address,
    "custName": name
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    const response_ = await fetch("http://localhost:9292/customers/createCustomers", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
        return response_;
};

async function getOrders(custID) {
    
    // var customerOrderURL = "http://localhost:9494/orderByCustomer/" + custID;
    var customerOrderURL = "http://localhost:9494/orderByCustomer/1";
    const orderResponse = await fetch(customerOrderURL);
    const orders = await orderResponse.json();
    
    if (orderResponse.status === 200) {

        for (i in orders.data) {
            var order = orders.data[i];
            order_details = order.order_item;
            
            var rows = "";

            for (j in order_details) {
                sellername = await getSeller(order_details[0].sellerID)
                eachRow = "<td>" + order_details[j].order_id + "</td>" +
                            "<td>" + order_details[j].productName + "</td>" +
                            "<td>" + sellername + "</td>" +
                            "<td>" + order.status + "</td>";
                rows += "<tr>" + eachRow + "</tr>";

            } $('#orderTable').append(rows);
            console.log(rows)
        } 
    } else if (orderResponse.status == 404) {

        showError(orders.message);

    } else {

        message = "Something went wrong while retrieving orders, please try again later."
        showError(message);

    }
}

async function getSeller(sellerID) {
    
    var sellerURL = "http://localhost:9191/sellers/" + sellerID;
    const sellerResponse = await fetch(sellerURL);
    const seller = await sellerResponse.json();
    
    if (sellerResponse.status === 200) {

        return seller.data.sellerName;
    } else {
        return seller.message;
    }
}