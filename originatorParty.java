

public class originatorParty {
    private int ID;
    private contact orginator;

    //constructor
    public originatorParty(int ID, contact originator){
        this.ID = ID;
        this.orginator = originator;
    }

    //getters
    public int getID(){
        return ID;
    }

    public contact getOriginator(){
        return orginator;
    }

    //setters
}
