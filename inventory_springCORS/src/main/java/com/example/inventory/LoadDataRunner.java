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
        Item i = new Item( 1, "FRUIT", 20, 10, 1);
        Item j = new Item( 2, "PINEAPPLE", 50, 4, 1);
        Item k = new Item( 3, "APPLE", 30, 6, 2);
        repo.save(i);
        repo.save(j);
        repo.save(k);


    }
}
