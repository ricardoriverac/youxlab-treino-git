package introducao.enumeracao.aplication;

import introducao.enumeracao.entities.Order;
import introducao.enumeracao.entitiesEnum.OrderStatus;

import java.util.Date;

public class aplicationEnum {
    public static void main(String[] args) {
        Order order = new Order(2 , new Date() , OrderStatus.PENDING_PAYMENT);

        System.out.println(order);

        // Conversão de String para enum

        OrderStatus os1 = OrderStatus.DELIVERED;

        OrderStatus os2 = OrderStatus.valueOf("DELIVERED");

        System.out.println(os1);
        System.out.println(os2);
    }
}
