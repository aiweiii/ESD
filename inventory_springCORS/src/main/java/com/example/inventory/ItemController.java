package com.example.inventory;
// public class ItemController {
    
// }

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;  
import org.springframework.web.bind.annotation.GetMapping;  
import org.springframework.web.bind.annotation.PathVariable;  
import org.springframework.web.bind.annotation.PostMapping;  
import org.springframework.web.bind.annotation.PutMapping;  
import org.springframework.web.bind.annotation.RequestBody;  
import org.springframework.web.bind.annotation.RestController;  
// import com.javatpoint.model.Books;  
// import com.javatpoint.service.BooksService;  
//mark class as Controller  
@RestController  
public class ItemController   
{

//    String frontendLink = "http://localhost:3000";

//autowire the BooksService class  
@Autowired  
ItemService itemService;
//creating a get mapping that retrieves all the books detail from the database



//    this didnt work for cors:
//@CrossOrigin(origins = "http://localhost:8080")
@CrossOrigin(origins = "http://localhost:3000")
@GetMapping("/items")
private List<Item> getAllItems()
{  
return itemService.getAllItems();
}  

//creating a get mapping that retrieves the detail of a specific book
@CrossOrigin(origins = "http://localhost:3000")
@GetMapping("/item/{itemid}")
private Optional<Item> getBooks(@PathVariable("itemid") int itemId)
{  
return itemService.getItemsById(itemId);
}  
//creating a delete mapping that deletes a specified book
@CrossOrigin(origins = "http://localhost:3000", maxAge = 3600)
@DeleteMapping("/deleteItem/{itemid}")
private int deleteBook(@PathVariable("itemid") int itemId)
{
    itemService.delete(itemId);
return itemId;
}  
//creating post mapping that post the book detail in the database
@CrossOrigin(origins = "http://localhost:3000")
@PostMapping("/addItem")
private int saveBook(@RequestBody Item item)
{
    itemService.saveOrUpdate(item);
return item.getID();
}  
//creating put mapping that updates the book detail
@CrossOrigin(origins = "http://localhost:3000")
@PutMapping("/updateItem")
private Item update(@RequestBody Item item)
{
    itemService.saveOrUpdate(item);
return item;
}  

}  