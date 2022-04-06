
// variables and constants
const cartContainer = document.querySelector('.cart-container');
const productList = document.querySelector('#product-list');
const cartList = document.querySelector('.cart-list');
const cartTotalValue = document.getElementById('cart-total-value');
const cartCountInfo = document.getElementById('cart-count-info');
const cartCountInfoValue = document.getElementById('cart-count-info');
const payBtn = document.getElementById("pay-btn");
let cartItemID = 1;


eventListeners();

// all event listeners
function eventListeners(){
    window.addEventListener('DOMContentLoaded', () => {
        loadJSON();
        loadCart();
    });

    // show/hide cart container
    document.getElementById('cart-btn').addEventListener('click', () => {
        cartContainer.classList.toggle('show-cart-container');
        $(document.getElementById("overlay")).toggle($(".show-cart-container").is(':visible'));

    });

    // add to cart
    productList.addEventListener('click', purchaseProduct);

    // delete from cart
    cartList.addEventListener('click', deleteProduct);

    // user clicks on PAY NOW button
    payBtn.addEventListener('click', callMicroservices);
}

function callMicroservices() {
    let products = getProductFromStorage();
    let custId = 1;
    let itemId;
    let itemName;
    let itemQuantity;

    getCustId()
    postToCart();
    placeAnOrder();

}

// function getCustId(params) {
//     name
// }


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
            console.log(custID)

            }

        else if (response.status == 404) {
            console.log("Response status is 404.")
            // console.log(createResponse.json().custID)
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


function placeAnOrder() {

}

// function postToCart() {
//     let products = getProductFromStorage();
//     let custId = 1;
//     let itemId;
//     let itemName;
//     let itemQuantity;

//     for (const product of products) { //try FOR IN if cannot
//         itemId = product.id;
//         // console.log("id:",typeof(product.id));
//         itemName = product.name;
//         // console.log("name:",itemName);
//         itemQuantity = parseInt(product.userQuantity);
//         // console.log("userquantity:",typeof(itemQuantity));

//         var myHeaders = new Headers();
//         myHeaders.append("Content-Type", "application/json");

//         var raw = JSON.stringify({
//         "custId": 2,
//         "itemId": 2,
//         "itemName": "AI WEI",
//         "itemQuantity": 3
//         });

//         var requestOptions = {
//         method: 'POST',
//         headers: myHeaders,
//         body: raw,
//         redirect: 'follow',
//         mode: 'no-cors'
//         };

//         console.log('b')
//         fetch("http://127.0.0.1:9393/addCartItem", requestOptions)
//         .then(response => response.text())
//         .then(result => console.log(result))
//         .catch(error => console.log('error', error));
//         console.log('a')
//         console.log(requestOptions)
//     }
//     console.log("c")


// }

// display the PAY NOW button if cart has items
function updatePayNowDisplay() {
    var numOfItemsInCart = JSON.parse(localStorage.getItem('products')).length
    if (numOfItemsInCart > 0) {
        payBtn.style.display='inline';
    } else {
        payBtn.style.display='none';
    }
}


// update cart info
function updateCartInfo(){
    let cartInfo = findCartInfo();
    cartCountInfo.textContent = cartInfo.productCount;
    cartTotalValue.textContent = cartInfo.total;
    updatePayNowDisplay()
}

// load product items content form JSON file
function loadJSON(){
    $(async () => {
                // Change serviceURL to your own
                var serviceURL = "http://127.0.0.1:9090/items";
                try {
                    const response =
                        await fetch(
                            serviceURL, { method: 'GET' }
                        );
                    const result = await response.json();
                    if (response.status === 200) {
                        // success case
                        var items = result;

                        let html = '';
                        items.forEach(item => {
                            var imgFileName = "static/images/" + item.id + "-1.jpeg";
                            html += `<div class="col">
                                    <div class="card shadow-sm">
                                        <img class="card-img-top bg-dark cover" id="shop-item-image" alt="${item.productName}" src=${imgFileName}>
                                        <div class="card-body">
                                            <h5 class="card-title text-center" id="shop-item-title">${item.productName}</h5>
                                            <p class="card-text text-center text-muted" id="shop-item-price">$${item.itemPrice}</p>
                                            <p class="card-text text-center text-muted" id="shop-item-quantity">Available Stocks: ${item.quantity}</p>
                                            <div class="d-grid gap-2">
                                                Quantity: <input type="number" min="1" max="${item.quantity}" id="user-quantity" value="1">
                                                <button class="btn add-to-cart-btn" type="button" id="add-to-cart-btn">Add to Cart</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>`;
                        });
                        productList.innerHTML = html;

                    } else if (response.status == 404) {
                        // No books
                        console.log(result.message);
                    } else {
                        // unexpected outcome, throw the error
                        throw response.status;
                    }
                } catch (error) {
                    // Errors when calling the service; such as network error,
                    // service offline, etc
                    console.log('There is a problem retrieving product data, please try again later.<br />' + error);
                } // error
            });
}

// check quantity
function checkQty(product) {
    let userQty = parseInt(product.userQuantity);
    let allowedQty = parseInt(product.quantity.split(":")[1])

    // validation of quantity selected
    if (userQty >= 1 && userQty <= allowedQty) {
        cartItemID++;
        addToCartList(product);
        saveProductInStorage(product);

    } else {
        document.querySelector(".modal-body").textContent = "Please enter a quantity between 1 and " + allowedQty + " :)";
        $('#exampleModal').modal('show');
    }

}

// purchase product
function purchaseProduct(e){
    if(e.target.classList.contains('add-to-cart-btn')){
        let product = e.target.parentElement.parentElement.parentElement;
        getProductInfo(product);
    }
}

// get product info after add to cart button click
function getProductInfo(product){
    let productInfo = {
        id: cartItemID,
        imgSrc: product.querySelector('img').src,
        name: product.querySelector('#shop-item-title').textContent,
        price: product.querySelector('#shop-item-price').textContent,
        quantity: product.querySelector('#shop-item-quantity').textContent,
        userQuantity: product.querySelector('#user-quantity').value,
    }

    checkQty(productInfo)

    // cartItemID++;
    // addToCartList(productInfo);
    // saveProductInStorage(productInfo);
}

// add the selected product to the cart list
function addToCartList(product){
    const cartItem = document.createElement('div');
    cartItem.classList.add('cart-item');
    cartItem.setAttribute('data-id', `${product.id}`);
    cartItem.innerHTML = `
        <img src = "${product.imgSrc}" alt = "product image">
        <div class = "cart-item-info">
            <h5 class = "cart-item-name">${product.name}</h5>
            <h5 class = "cart-item-price">${product.price}</h5>
            <h5 class = "cart-item-quantity">Quantity: ${product.userQuantity}</h5>
        </div>

        <button type = "button" class = "cart-item-del-btn">
            <i class = "fas fa-times"></i>
        </button>
    `;
    cartList.appendChild(cartItem);

}

// save the product in the local storage
function saveProductInStorage(item){
    let products = getProductFromStorage();
    products.push(item);
    localStorage.setItem('products', JSON.stringify(products));
    updateCartInfo();
}

// get all the products info if there is any in the local storage
function getProductFromStorage(){
    return localStorage.getItem('products') ? JSON.parse(localStorage.getItem('products')) : [];
    // returns empty array if there isn't any product info
}

// load carts product
function loadCart(){
    let products = getProductFromStorage();
    if(products.length < 1){
        cartItemID = 1; // if there is no any product in the local storage
    } else {
        cartItemID = products[products.length - 1].id;
        cartItemID++;
        // else get the id of the last product and increase it by 1
    }
    products.forEach(product => addToCartList(product));

    // calculate and update UI of cart info 
    updateCartInfo();
}

// calculate total price of the cart and other info
function findCartInfo(){
    let products = getProductFromStorage();
    let total = products.reduce((acc, product) => {
        let price = parseFloat(product.price.substr(1)); // removing dollar sign
        return acc += price;
    }, 0); // adding all the prices
    return{
        total: total.toFixed(2),
        productCount: products.length
    }
}

// delete product from cart list and local storage
function deleteProduct(e){
    let cartItem;
    if(e.target.className === "cart-item-del-btn"){
        cartItem = e.target.parentElement;
        cartItem.remove(); // this removes from the DOM only
    } else if(e.target.tagName === "I"){
        cartItem = e.target.parentElement.parentElement;
        cartItem.remove(); // this removes from the DOM only
    }

    let products = getProductFromStorage();
    let updatedProducts = products.filter(product => {
        return product.id !== parseInt(cartItem.dataset.id);
    });
    localStorage.setItem('products', JSON.stringify(updatedProducts)); // updating the product list after the deletion
    updateCartInfo();
}