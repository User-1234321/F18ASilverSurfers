

public class transactionConditions {
    private String requiredAction;
    private String transactionMethod;

    //constructor
    public transactionConditions(String requiredAction, String transactionMethod){
        this.requiredAction = requiredAction;
        this.transactionMethod = transactionMethod;
    }

    //getters
    public String getRequiredAction(){
        return requiredAction;
    }

    public String getTransactionMethod(){
        return transactionMethod;
    }

    //setters
    public void setRequiredAction(String requiredAction){
        this.requiredAction = requiredAction;
        return;
    }

    public void setTranactionMethod(String transactionMethod){
        this.transactionMethod = transactionMethod;
        return;
    }
}

//functions
