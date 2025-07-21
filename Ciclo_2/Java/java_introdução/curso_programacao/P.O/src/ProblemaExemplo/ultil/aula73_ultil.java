package ProblemaExemplo.ultil;

public class aula73_ultil {

    public double dollarPrice;
    public double dollarqtd;
    public static final double decimal6 = 6;


    public double CurrencyConverter(){
        double iof = decimal6 /100;
        double multiplica = dollarqtd * dollarPrice;
        return multiplica + multiplica * iof;
    }


}
