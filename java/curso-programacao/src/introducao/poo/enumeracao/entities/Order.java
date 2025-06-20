package introducao.poo.enumeracao.entities;

import introducao.poo.enumeracao.entitiesEnum.OrderStatus;

import java.util.Date;

public class Order {
    // Classe de pedido de quando foi feito
    private Integer id;
    private Date moment;
    private OrderStatus order;

    // Order Status a ordem que o pedido está
    public Order(Integer id, Date moment, OrderStatus order) {
        this.id = id;
        this.moment = moment;
        this.order = order;
    }

    @Override
    public String toString() {
        return "Order{" +
                "id= " + id +
                ", moment= " + moment +
                ", order= " + order +
                '}';
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Date getMoment() {
        return moment;
    }

    public void setMoment(Date moment) {
        this.moment = moment;
    }

    public OrderStatus getOrder() {
        return order;
    }

    public void setOrder(OrderStatus order) {
        this.order = order;
    }
}
