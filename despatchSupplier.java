public class despatchSupplier {
    private postalAddress supplierAddress;
    private String partyName;
    private tax partyTax;
    private contact supplier;

    //constuctor
    public despatchSupplier(postalAddress supplierAddress, String partyName, tax partyTax, contact supplier){
        this.supplierAddress = supplierAddress;
        this.partyName = partyName;
        this.partyTax = partyTax;
        this.supplier = supplier;
    }

    //getters
    public postalAddress getSupplierAddress(){
        return supplierAddress;
    }

    public String getPartyName(){
        return partyName;
    }

    public tax getPartyTax(){
        return partyTax;
    }

    public contact getSuppliercContact(){
        return supplier;
    }
    //setters

    
}

//funcitons
