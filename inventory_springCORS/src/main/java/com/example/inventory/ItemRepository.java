package com.example.inventory;
import org.springframework.data.repository.CrudRepository;
public interface ItemRepository extends CrudRepository<Item, Integer> {
//    Item findById(long id); //https://www.baeldung.com/spring-data-partial-update
 }
