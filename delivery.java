

public class delivery {
    private postalAddress recipient;

    //requested delivery period
    private int deliveryStartDate;
    private int deliveryEndDate;
    private int deliveryStartTime;
    private int deliveryEndTime;

    //delivery terms
    private String deliveryTerms;

    //constructor
    public delivery(postalAddress recipient, int deliveryStartDate, int deliveryEndDate, 
    int deliveryStartTime, int deliveryEndTime, String deliveryTerms){
        
        this.recipient = recipient;
        this.deliveryStartDate = deliveryStartDate;
        this.deliveryStartTime = deliveryStartTime;
        this.deliveryEndDate = deliveryEndDate;
        this.deliveryEndTime = deliveryEndTime;
        this.deliveryTerms = deliveryTerms;
    }

    //getters
    public postalAddress getRecipient(){
        return recipient;
    }

    public int getDeliveryStartDate(){
        return deliveryStartDate;
    }

    public int getDeliveryEndDate(){
        return deliveryEndDate;
    }

    public int getDeliveryStartTime(){
        return deliveryStartTime;
    }

    public int getDeliveryEndTime(){
        return deliveryEndTime;
    }

    public String getDeliveryTerms(){
        return deliveryTerms;
    }

    //setters

}

//functions

