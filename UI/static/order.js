
const failedBtn = document.getElementById('failedBtn');
const successBtn = document.getElementById('successBtn');


successBtn.addEventListener('click', function onClick() {
    document.querySelector(".modal-body").textContent = "Your order has been successfully cancelled";
    $('#exampleModal').modal('show');

    successBtn.style.backgroundColor = 'grey';
    successBtn.style.color = 'black';
    successBtn.style.borderColor ='black';
    successBtn.innerText ="Cancelled"

});

failedBtn.addEventListener('click', function onClick() {
    document.querySelector(".modal-body").textContent = "Order cancellation failure as order has been shipped or already cancelled and cannot be cancelled";
    $('#exampleModal').modal('show');
});


async function getCust(user) {           
    // Change serviceURL to your own
    var customerURL = "http://localhost:9292/customers";
    var findCustomer = customerURL + '/' + user ;
    
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
            // console.log( result.data.custAddress)
            // getOrders(custID);
            
            } 
        
        else if (response.status === 404) {
            const createResponse = await createCustomer('', user);
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

async function cancelOrders(orderID) {
    var cancelURL = "http://localhost:9696/cancelOrder";
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
    "id": orderID
    });

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    const cancelResponse = await fetch(cancelURL, requestOptions)
    // .then(response => response.text())
    // .then(result => console.log(result))
    // .catch(error => console.log('error', error));
    
    const cancelled = await cancelResponse.json();
    
    if (cancelResponse.status === 200) {
        alert(cancelled.message);
        document.getElementById("orderstatus").innerText = 'Cancelled';
        // window.location.href = "http://localhost:3000/orderhistory";
    } else {
        alert(cancelled.message);
        window.location.href = "http://localhost:3000/orderhistory";

    }

};


// async function getOrders(custID) {
    
//     // var customerOrderURL = "http://localhost:9494/orderByCustomer/" + custID;
//     var customerOrderURL = "http://localhost:9494/orderByCustomer/1";
//     const orderResponse = await fetch(customerOrderURL);
//     const orders = await orderResponse.json();
    
//     if (orderResponse.status === 200) {

//         for (i in orders.data) {
//             var order = orders.data[i];
//             order_details = order.order_item;
            
//             var orders_length = order_details.length
//             var rows = "<tr><td rowspan=" + orders_length +">" + order_details[0].order_id + "</td>";
//             var button = "";

//             if (order.status !== 'Shipped') {
//                 button = " <button class='btn btn-primary btn-sm' onclick='cancelOrders(" +
//                 order_details[0].order_id + ")'> Cancel order </button>";
//             } else {
//                 button = " <button class='btn btn-primary btn-sm disabled'> Cancel order </button>";
//             }

//             for (j in order_details) {
//                 sellername = await getSeller(order_details[0].sellerID)
//                 var imgFileName = "static/images/" + order_details[j].order_item_id + "-1.jpeg";

//                 eachRow = "<td> <img style='height: 100px' src=" + imgFileName +"> " +
//                             order_details[j].productName + "</td>" +
//                             "<td>" + order_details[j].quantity + "</td>" +
//                             "<td>" + sellername + "</td>";

//                 if (j == 0) {
//                     eachRow += "<td id='orderstatus' rowspan=" + orders_length +">" + order.status  + "</td>"+
//                                 "<td rowspan=" + orders_length +">" + button + "</td>";
//                 }

//                 rows += eachRow + "</tr>";

//             }
        
//             $('#orderTable').append(rows);

//         }
//     } else if (orderResponse.status == 404) {

//         showError(orders.message);

//     } else {

//         message = "Something went wrong while retrieving orders, please try again later."
//         showError(message);

//     }
// }

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