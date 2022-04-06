//package microservice.cart;
//
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.web.bind.annotation.*;
//
//import java.util.List;
//import java.util.Optional;
//
//public class CartController {
//}


package microservice.cart;

        import java.util.Optional;
        import java.util.List;
        import org.springframework.web.bind.annotation.GetMapping;
        import org.springframework.web.bind.annotation.PostMapping;
        import org.springframework.web.bind.annotation.RestController;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.web.bind.annotation.DeleteMapping;
        import org.springframework.web.bind.annotation.PathVariable;
        import org.springframework.web.bind.annotation.PutMapping;
        import org.springframework.web.bind.annotation.RequestBody;


@RestController
public class CartController {
    private CartRepository cartRepository;

    @Autowired
    CartService cartService;

    public CartController(CartRepository cartRepository) {
        this.cartRepository = cartRepository;
    }

    @GetMapping("/all")
    public Iterable<Cart> getAll() {
        return cartRepository.findAll();
    }

    //creating a get mapping that retrieves the detail of a specific book
    @GetMapping("/cart/{custId}/{itemId}")
    private Optional<Cart> getACartItem(@PathVariable("custId") int custId, @PathVariable("itemId") int itemId)
    {
        return cartService.getAnItemByCartId(custId, itemId);
    }

    @GetMapping("/cart/{custId}")
    private List<Cart> getACart(@PathVariable("custId") int custId)
    {
        return cartService.getCartByCustId(custId);
    }

    //creating a delete mapping that deletes a specified item in cart
    @DeleteMapping("/deleteCartItem/{custId}/{itemId}")
    private String deleteCartItem(@PathVariable("custId") int custId, @PathVariable("itemId") int itemId)
    {
        cartService.deleteCartItem(custId, itemId);
        return "Deleted item: custId-" + custId + "; itemId-" + itemId;
    }

    //creating a delete mapping that deletes a specified cart
    @DeleteMapping("/deleteCart/{custId}")
    private int deleteCart(@PathVariable("custId") int custId)
    {
        cartService.deleteCart(custId);
        return custId;
    }

    //creating post mapping that post the cart detail in the database
    @PostMapping("/addCartItem")
    private String saveCartItem(@RequestBody Cart cart)
    {
        cartService.saveOrUpdate(cart);
        return "Added: custId-" + cart.getCustId() + "; itemId-" +  cart.getItemId();
    }
    //creating put mapping that updates the cart item detail
    @PutMapping("/updateCart")
    private Cart update(@RequestBody Cart cart)
    {
        cartService.saveOrUpdate(cart);
        return cart;
    }
}
