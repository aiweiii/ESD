////package com.example.inventory;
////        import org.springframework.beans.factory.annotation.Autowired;
////        import org.springframework.boot.ApplicationArguments;
////        import org.springframework.boot.ApplicationRunner;
////        import org.springframework.stereotype.Component;
////
////@Component
////public class LoadDataRunner implements ApplicationRunner {
////    @Autowired
////    private ItemRepository repo;
////
////    @Override
////    public void run(ApplicationArguments args) throws Exception {
//////        int ID, String productName, int quantity, int itemPrice,  int sellerId
////        Item i = new Item( 120, "FRUIT", 20, 10, 1);
////        Item j = new Item( 2, "PINEAPPLE", 50, 4, 1);
////        Item k = new Item( 3, "APPLE", 30, 6, 2);
////
//////        Cart cart1 = new Cart();
//////        cart1.setCustId("1111");
//////        cart1.setItemId("120");
//////        cart1.setItemName("Apple");
//////        cart1.setItemQuantity(3);
//////
//////        Cart cart2 = new Cart();
//////        cart2.setCustId("2222");
//////        cart2.setItemId("120") ;
//////        cart2.setItemName("Apple");
//////        cart2.setItemQuantity(1);
//////
//////        Cart cart3 = new Cart();
//////        cart3.setCustId("2222");
//////        cart3.setItemId("121");
//////        cart3.setItemName("Banana");
//////        cart3.setItemQuantity(3);
//////
//////        Cart cart4 = new Cart();
//////        cart4.setCustId("3333");
//////        cart4.setItemId("122");
//////        cart4.setItemName("Pear");
//////        cart4.setItemQuantity(3);
////
//////
////        repo.save(i);
////        repo.save(j);
////        repo.save(k);
////
////
////    }
////}
//
//
//package com.example.inventory;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.ApplicationArguments;
//import org.springframework.boot.ApplicationRunner;
//import org.springframework.stereotype.Component;
//
//@Component
//public class LoadDataRunner implements ApplicationRunner {
//    @Autowired
//    private ItemRepository repo;
//
//    @Override
//    public void run(ApplicationArguments args) throws Exception {
////        int ID, String productName, int quantity, int itemPrice,  int sellerId
//        Item i = new Item( 120, "FRUIT", 20, 10, 1);
//        Item j = new Item( 2, "PINEAPPLE", 50, 4, 1);
//        Item k = new Item( 3, "APPLE", 30, 6, 2);
//
//        Item a = new Item( 4, "WOMEN Pocketable UV Protection Parka", 53, 49, 1);
//        Item b = new Item( 5, "MEN Smooth Jersey AIRISM Lined Parka", 52, 59, 1);
//        Item c = new Item( 6, "Pocketable UV Protection Anorak Parka", 49, 62, 1);
//        Item d = new Item( 7, "Face Towel", 7, 38, 2);
//        Item e = new Item( 8, "Ottoman", 71, 129, 2);
//        Item f = new Item( 9, "Jersey Slippers", 7, 41, 2);
//        Item g = new Item( 10, "Beats Fit Pro", 36, 299, 3);
//        Item h = new Item( 11, "Beats Solo3 Wireless Headphones", 43, 279, 3);
//        Item l = new Item( 12, "Beats Studio Buds", 13, 219, 3);
//
//
//        repo.save(i);
//        repo.save(j);
//        repo.save(k);
//        repo.save(a);
//        repo.save(b);
//        repo.save(c);
//        repo.save(d);
//        repo.save(e);
//        repo.save(f);
//        repo.save(g);
//        repo.save(h);
//        repo.save(l);
//
//
//    }
//}



package com.example.inventory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class LoadDataRunner implements ApplicationRunner {
    @Autowired
    private ItemRepository repo;

    @Override
    public void run(ApplicationArguments args) throws Exception {
//        int ID, String productName, int quantity, int itemPrice,  int sellerId
        Item a = new Item( 1, "WOMEN Pocketable UV Protection Parka", 53, 49, 1);
        Item b = new Item( 2, "MEN Smooth Jersey AIRISM Lined Parka", 52, 59, 1);
        Item c = new Item( 3, "Pocketable UV Protection Anorak Parka", 49, 62, 1);
        Item d = new Item( 4, "Face Towel", 7, 38, 2);
        Item e = new Item( 5, "Ottoman", 71, 129, 2);
        Item f = new Item( 6, "Jersey Slippers", 7, 41, 2);
        Item g = new Item( 7, "Beats Fit Pro", 36, 299, 3);
        Item h = new Item( 8, "Beats Solo3 Wireless Headphones", 43, 279, 3);
        Item i = new Item( 9, "Beats Studio Buds", 13, 219, 3);
        repo.save(a);
        repo.save(b);
        repo.save(c);
        repo.save(d);
        repo.save(e);
        repo.save(f);
        repo.save(g);
        repo.save(h);
        repo.save(i);


    }
}
