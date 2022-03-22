package com.example.inventory;
// public class ItemService { 
// }
import java.util.ArrayList;  
import java.util.List;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;

import java.util.Optional;
//defining the business logic  
@Service  
public class ItemService   
{  
@Autowired  
ItemRepository itemRepository;
//getting all items record by using the method findaAll() of CrudRepository
public List<Item> getAllItems()
{  
List<Item> items = new ArrayList<Item>();
    itemRepository.findAll().forEach(item1 -> items.add(item1));
return items;
}  
//getting a specific record by using the method findById() of CrudRepository  
public Optional<Item> getItemsById(int id)
{  
//return booksRepository.findById(id);
    Optional<Item> user = itemRepository.findById(id);
//    Optional<User> opt = Optional.ofNullable(user);
    return user;
}  
//saving a specific record by using the method save() of CrudRepository  
public void saveOrUpdate(Item item)   
{
    itemRepository.save(item);
}  
//deleting a specific record by using the method deleteById() of CrudRepository  
public void delete(int id)   
{
    itemRepository.deleteById(id);
}
//updating a record  
public void update(Item item, int itemid)
{
    itemRepository.save(item);
}  
}  

// https://www.javatpoint.com/spring-boot-crud-operations