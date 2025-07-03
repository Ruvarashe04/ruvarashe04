/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.mybank;


import java.io.Serializable;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;

/**
 *
 * @author hp
 */
class bank {

    static void addCustomer(Customer customer) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    static void removeCustomer(Customer customer) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    public class Bank implements Serializable{
    private ArrayList<Customer> customers = new ArrayList<Customer>();
    
    void addCustomer(Customer customer) {
        if(accountExists(customer.getAccount().getAccountNumber())){
            customer.getAccount().setAccountNumber(findValidAccountNumber());
        }
        customers.add(customer);
    }
    
    private int findValidAccountNumber(){
        int accountNumber;
        do {
            accountNumber = Account.getNextAccountNumber();
        } while(accountExists(accountNumber));      
        return accountNumber;
    }
    
    private boolean accountExists(int accountNumber){
        for(Customer c : customers){
            if(c.getAccount().getAccountNumber() == accountNumber){
                return true;
            }
        }
        return false;
    }

    Customer getCustomer(int account) {
        return customers.get(account);
    }
    
    ArrayList<Customer> getCustomers(){
        return customers;
    }

    Customer getCustomerByAccountNumber(int accountNumber) {
        Customer customer = null;
        for(Customer c : customers){
            if(c.getAccount().getAccountNumber() == accountNumber){
                customer = c;
                break;
            }
        }
        return customer;
    }

    void removeCustomer(Customer customer) {
        customers.remove(customer);
    }
    
    public static double round(double value, int places) {
        if (places < 0) {
            throw new IllegalArgumentException();
        }
        BigDecimal bd = new BigDecimal(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
    
    
    }
    
}
