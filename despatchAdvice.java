

public class despatchAdvice {
    private int despatchType; 
    private int fulfillment;
    private buyerParty buyer;
    private sellerParty seller;
    private shipment goods;
    private deliveryCustomer recipient;
    private despatchSupplier supplier;
    private despatchLine despatchLine;

    //constuctor
    public despatchAdvice(int despatchType, int fulfillment, buyerParty buyer, 
    sellerParty seller, shipment goods, deliveryCustomer recipient, 
    despatchSupplier supplier, despatchLine despatchLine){

        this.despatchType = despatchType;
        this.fulfillment = fulfillment;
        this.buyer = buyer;
        this.seller = seller;
        this.goods = goods;
        this.recipient =recipient;
        this.supplier = supplier;
        this.despatchLine =  despatchLine;
    }

    //getters
    public int getDespatchType(){
        return despatchType;
    }

    public int getFulfillment(){
        return fulfillment;
    }

    public buyerParty getBuyerParty(){
        return buyer;
    }

    public sellerParty getSellerParty(){
        return seller;
    }

    public shipment getShipment(){
        return goods;
    }

    public deliveryCustomer getRecipient(){
        return recipient;
    }

    public despatchSupplier getSupplier(){
        return supplier;
    }

    public despatchLine getDespatchLine(){
        return despatchLine;
    }

    //setters
    

    
}
//functions