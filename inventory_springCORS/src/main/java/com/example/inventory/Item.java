package com.example.inventory;


import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Item {

    @Id
//    @GeneratedValue(strategy = GenerationType.AUTO)
    private int ID;
    private String productName;
    private int quantity;
    private int sellerId;
    private int itemPrice;

    Item(int ID, String productName, int quantity, int itemPrice,  int sellerId){
        this.ID = ID;
        this.productName = productName;
        this.quantity = quantity;
        this.itemPrice = itemPrice;
        this.sellerId = sellerId;

    }

    Item(){}

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


    public int getSellerId() {
        return sellerId;
    }

    public void setSellerId(int sellerId) {
        this.sellerId = sellerId;
    }


    public int getItemPrice() {
        return itemPrice;
    }

    public void setItemPrice(int itemPrice) {
        this.itemPrice = itemPrice;
    }







}
