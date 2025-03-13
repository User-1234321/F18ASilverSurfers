public class orderReference {
    private int orderID;
    private int issueDate;

    //constructor
    public orderReference(int orderID, int issueDate){
        this.orderID = orderID;
        this.issueDate = issueDate;
    }


    //getters
    public int getOrderID(){
        return orderID;
    }

    public int getIssueDate(){
        return issueDate;
    }

    //setters
}
