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
        cart1.setCustId("1");
        cart1.setItemId("3");
        cart1.setItemName("APPLE");
        cart1.setItemQuantity(3);

        Cart cart2 = new Cart();
        cart2.setCustId("2");
        cart2.setItemId("3");
        cart2.setItemName("APPLE");
        cart2.setItemQuantity(1);

        Cart cart3 = new Cart();
        cart3.setCustId("2");
        cart3.setItemId("2");
        cart3.setItemName("PINEAPPLE");
        cart3.setItemQuantity(3);

        Cart cart4 = new Cart();
        cart4.setCustId("3");
        cart4.setItemId("1");
        cart4.setItemName("FRUIT");
        cart4.setItemQuantity(3);

        cartRepository.save(cart1);
        cartRepository.save(cart2);
        cartRepository.save(cart3);
        cartRepository.save(cart4);
    }
}
