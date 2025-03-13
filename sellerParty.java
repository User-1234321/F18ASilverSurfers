
public class sellerParty{
    private int ID;
    private postalAddress seller;
    private contact sellerContact;
    private tax sellerTax;

    public sellerParty(int ID, postalAddress seller, contact sellerContact, tax sellerTax){
        this.ID = ID;
        this.seller = seller;
        this.sellerContact = sellerContact;
        this.sellerTax = sellerTax;
    }

    public int getID(){
        return ID;
    }

    public postalAddress getPostalAddress(){
        return seller;
    }

    public contact getSellerContact(){
        return sellerContact;
    }

    public tax getSellerTax(){
        return sellerTax;
    }

    //setters
    public void setID(int ID){
        this.ID = ID;
        return;
    }

    public void setPostalAddress(postalAddress seller){
        this.seller = seller;
        return;
    }

    public void setSellerContact(contact sellerContact){
       this.sellerContact = sellerContact;
       return;
    }

    public void setSellerTax(tax sellerTax){
       this.sellerTax = sellerTax;
       return;
    }

}

//functions