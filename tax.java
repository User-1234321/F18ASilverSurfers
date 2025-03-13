
public class tax {
    private String regName;
    private int taxNumber; //vat, gst, etc
    private String exemption;
    private String taxScheme;

    //constructor
    public tax(String regName, int taxNumber, String exmeption, String taxScheme){
        this.regName = regName;
        this.taxNumber = taxNumber;
        this.exemption = exmeption;
        this.taxScheme = taxScheme;
    }

    //getters
    public String getRegName(){
        return regName;
    }

    public int getTaxNumber(){
        return taxNumber;
    }

    public String getExemption(){
        return exemption;
    }

    public String getTaxScheme(){
        return taxScheme;
    }

    //setters
}


