
public class postalAddress {
    private  String streetName;
    private int buildingNumber;
    private String cityName;
    private String subEntity;
    private int addressLine; //assuming that this is for apartments
    private String country;

    //constructor
    public postalAddress(String streetName, int buildingNumber, String cityName, 
    String subEntity, int addressLine, String country){
        
        this.streetName = streetName;
        this.buildingNumber = buildingNumber;
        this.cityName = cityName;
        this.subEntity = subEntity;
        this.addressLine = addressLine;
        this.country = country;
    }

    //getters
    public String getStreetName(){
        return streetName;
    }

    public int getBuildingNumber(){
        return buildingNumber;
    }

    public String getCityName(){
        return cityName;
    }

    public String getSubEntity(){
        return subEntity;
    }

    public int getAddressLine(){
        return addressLine;
    }

    public String getCountry(){
        return country;
    }


    //setters
}

