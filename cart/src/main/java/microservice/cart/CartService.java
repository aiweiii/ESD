package microservice.cart;


import java.util.ArrayList;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.NoSuchElementException;
import java.util.Optional;

//defining the business logic

@Service
public class CartService
{
@Autowired
CartRepository cartRepository;
//getting all items record by using the method findaAll() of CrudRepository
public List<Cart> getAllCartRows()
{
    List<Cart> cartRows = new ArrayList<Cart>();
    cartRepository.findAll().forEach(item1 -> cartRows.add(item1));
    return cartRows;
}

//getting items in a cart by using the method findByCustId()
public List<Cart> getCartByCustId(int custId)
{
    List<Cart> cartRow = cartRepository.findByCustId(custId);
    return cartRow;
}

//getting a specific record by using the method findById() of CrudRepository
public Optional<Cart> getAnItemByCartId(int custId, int itemId)
{
    Optional <Cart> cartRow = cartRepository.findByCustIdAndItemId(custId, itemId);
    return cartRow;
}

//saving a specific record by using the method save() of CrudRepository
public void saveOrUpdate(Cart cartItem)
{
    cartRepository.save(cartItem);
}

//deleting a specific record by using the method deleteById() of CrudRepository
public void deleteCartItem(int custId, int itemId)
{
    Optional <Cart> cartItem = cartRepository.findByCustIdAndItemId(custId, itemId);
    try{
        Cart cartRow = cartItem.get();
        cartRepository.delete(cartRow);}
    catch (NoSuchElementException e){
        System.out.println("No such item in cart");
    }
}

//deleting record of the specified custId
public void deleteCart(int custId) {

    List<Cart> cartRows = cartRepository.findByCustId(custId);
    cartRepository.deleteAll(cartRows);
}

//updating a record
public void update(Cart cart)
{
    cartRepository.save(cart);
}
}


