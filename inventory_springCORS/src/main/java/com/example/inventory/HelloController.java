//package com.example.inventory;
//
//public class HelloController {
//}
package com.example.inventory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/")
    public String index() {
        return "Hello Trainers!";
    } }