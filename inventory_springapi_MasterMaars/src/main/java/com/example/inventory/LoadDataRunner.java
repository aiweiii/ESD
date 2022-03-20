package com.example.inventory;
//
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.ApplicationArguments;
//import org.springframework.boot.ApplicationRunner;
//import org.springframework.stereotype.Component;
//
//public class LoadDataRunner {
//}



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

        Item i = new Item( 1, "FRUIT", 20, 1);
        Item j = new Item( 2, "PINEAPPLE", 50, 1);
        Item k = new Item( 3, "APPLE", 30, 1);
        repo.save(i);
        repo.save(j);
        repo.save(k);


//        Trainer ash = new Trainer();
//        ash.setName("Ash");
//        Pokemon pikachu = new Pokemon("Pikachu","Electric", 10,10, 9);
//        Pokemon squirtle = new Pokemon("Squirtle","Water", 8,10, 8);
//        ash.getPokemons().add(pikachu);
//        ash.getPokemons().add(squirtle);
//        Trainer misty = new Trainer();
//        misty.setName("Misty");
//        Pokemon charmander = new Pokemon("Charmander","Fire", 9,10, 7);
//        misty.getPokemons().add(charmander);
//        trainerRepository.save(ash);
//        trainerRepository.save(misty);

    }
}
