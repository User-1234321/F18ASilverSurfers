

public class buyerParty{
    private int ID;
    private postalAddress buyer;
    private contact buyerContact;
    private tax buyerTax;

    //contructor
    public buyerParty(int ID, postalAddress buyer, contact buyerContact, tax buyerTax){
        this.ID = ID;
        this.buyer = buyer;
        this.buyerContact = buyerContact;
        this.buyerTax = buyerTax;
    }

    //getters
    public int getID(){
        return ID;
    }

    public postalAddress getAddress(){
        return buyer;
    }

    public contact geContact(){
        return buyerContact;
    }

    public tax getTax(){
        return buyerTax;
    }

    //setters

}

//functions


