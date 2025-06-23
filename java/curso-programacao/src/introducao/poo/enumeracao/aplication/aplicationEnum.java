package introducao.poo.enumeracao.aplication;

import introducao.poo.enumeracao.entities.Order;
import introducao.poo.enumeracao.entitiesEnum.OrderStatus;

import java.util.Date;

public class aplicationEnum {
    public static void main(String[] args) {
        Order order = new Order(2 , new Date() , OrderStatus.PENDING_PAYMENT);
        Order order1 = new Order(1098 , new Date() , OrderStatus.PENDING_PAYMENT);

        System.out.println(order);
        System.out.println(order1);

        // Conversão de String para enum

        OrderStatus os1 = OrderStatus.DELIVERED;

        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}
