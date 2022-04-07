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

        import org.springframework.web.bind.annotation.*;
        import org.springframework.beans.factory.annotation.Autowired;

@RestController
public class CartController {
    private CartRepository cartRepository;

    @Autowired
    CartService cartService;

    public CartController(CartRepository cartRepository) {
        this.cartRepository = cartRepository;
    }

//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @GetMapping("/all")
    public Iterable<Cart> getAll() {
        return cartRepository.findAll();
    }

    //creating a get mapping that retrieves the detail of a specific book
    @CrossOrigin(origins = "http://localhost:8000")
    @GetMapping("/cart/{custId}/{itemId}")
    private Optional<Cart> getACartItem(@PathVariable("custId") int custId, @PathVariable("itemId") int itemId)
    {
        return cartService.getAnItemByCartId(custId, itemId);
    }

//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @GetMapping("/cart/{custId}")
    private List<Cart> getACart(@PathVariable("custId") int custId)
    {
        return cartService.getCartByCustId(custId);
    }

    //creating a delete mapping that deletes a specified item in cart
//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @DeleteMapping("/deleteCartItem/{custId}/{itemId}")
    private String deleteCartItem(@PathVariable("custId") int custId, @PathVariable("itemId") int itemId)
    {
        cartService.deleteCartItem(custId, itemId);
        return "Deleted item: custId-" + custId + "; itemId-" + itemId;
    }

    //creating a delete mapping that deletes a specified cart
//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @DeleteMapping("/deleteCart/{custId}")
    private int deleteCart(@PathVariable("custId") int custId)
    {
        cartService.deleteCart(custId);
        return custId;
    }

    //creating post mapping that post the cart detail in the database
//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @PostMapping("/addCartItem")
    private String saveCartItem(@RequestBody Cart cart)
    {
        cartService.saveOrUpdate(cart);
        return "Added: custId-" + cart.getCustId() + "; itemId-" +  cart.getItemId();
    }
    //creating put mapping that updates the cart item detail
//    @CrossOrigin(origins = "http://localhost:3000")
    @CrossOrigin(origins = "http://localhost:8000")
    @PutMapping("/updateCart")
    private Cart update(@RequestBody Cart cart)
    {
        cartService.saveOrUpdate(cart);
        return cart;
    }
}
