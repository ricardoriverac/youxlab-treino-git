package introducao.poo.composition.exercicios.entities;


import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;


public class Order {
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

    private Date moment;
    private OrderStatus status;

    private  Client client;

    private List<OrdemItem> Items = new ArrayList<>();

    public Order(){

    }

    public Order(Date moment, OrderStatus status , Client client) {
        this.moment = moment;
        this.status = status;
        this.client = client;
    }

    public Date getMoment() {
        return moment;
    }

    public void setMoment(Date moment) {
        this.moment = moment;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public void setStatus(OrderStatus status) {
        this.status = status;
    }



    public void addItem(OrdemItem ordemItem){
        Items.add(ordemItem);
    }

    public void removeItem(OrdemItem ordemItem){
        Items.remove(ordemItem);
    }

    public double total(){
        double sum = 0.0;
        for (OrdemItem ordemItem : Items){
            sum = ordemItem.subtotal();
        }
        return sum;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("ORDER SUMMARY");
        sb.append("\n");
        sb.append("Order Moment: ");
        sb.append(sdf.format(moment));
        sb.append("\n");
        sb.append("Order Status: ");
        sb.append(status);
        sb.append("\n");
        sb.append("Cliente: ");
        sb.append(client).append("\n");
        sb.append("Order Items: \n");
        for (OrdemItem item : Items){
            sb.append(item).append("\n");
        }
        sb.append("Total price: $");
        sb.append(String.format("%.2f" , total()));
        return sb.toString();
    }
}
