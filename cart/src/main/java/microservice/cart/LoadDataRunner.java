package microservice.cart;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class LoadDataRunner implements ApplicationRunner {

    @Autowired
    private CartRepository cartRepository;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        Cart cart1 = new Cart();
        cart1.setCustId("1111");
        cart1.setItemId("120");
        cart1.setItemName("Apple");
        cart1.setItemQuantity(3);

        Cart cart2 = new Cart();
        cart2.setCustId("2222");
        cart2.setItemId("120");
        cart2.setItemName("Apple");
        cart2.setItemQuantity(1);

        Cart cart3 = new Cart();
        cart3.setCustId("2222");
        cart3.setItemId("121");
        cart3.setItemName("Banana");
        cart3.setItemQuantity(3);

        Cart cart4 = new Cart();
        cart4.setCustId("3333");
        cart4.setItemId("122");
        cart4.setItemName("Pear");
        cart4.setItemQuantity(3);

        cartRepository.save(cart1);
        cartRepository.save(cart2);
        cartRepository.save(cart3);
        cartRepository.save(cart4);
    }
}
