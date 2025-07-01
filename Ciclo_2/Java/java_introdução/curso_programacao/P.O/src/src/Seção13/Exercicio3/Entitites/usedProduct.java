package Seção13.Exercicio3.Entitites;

import java.util.Date;

public class usedProduct extends Product {
    public Date date;

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getPriceTag() {
        return priceTag;
    }

    public void setPriceTag(String priceTag) {
        this.priceTag = priceTag;
    }

    public String priceTag;
}
