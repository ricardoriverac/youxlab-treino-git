package introducao.poo.composition.exercicios.aplication;

import introducao.poo.composition.exercicios.entities.*;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class pedidoCliente {
    public static void main(String[] args) throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        System.out.println("Enter Cliente Data: ");
        System.out.print("Name: ");
        String name = input.nextLine();
        System.out.print("Email: ");
        String email = input.nextLine();
        System.out.print("Birth Date: ");
        Date birthdate = sdf.parse(input.next());
        Client client = new Client(name , email , birthdate);
        System.out.println("Enter order Status: ");
        System.out.print("Status: ");
        // OBS: quando for dar input em tipo enumerado tem usar (next);
        OrderStatus od1 = OrderStatus.valueOf(input.next());

        Order order = new Order(new Date(), od1 , client);

        System.out.print("How many itemns to this order? ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            input.nextLine();
            System.out.println("Enter #" + (i+1) + " item data:");
            System.out.print("Product name: ");
            String nameProduct = input.nextLine();
            System.out.print("Product Price: ");
            double priceProduct = input.nextDouble();
            System.out.print("Quantity: ");
            int quantidade = input.nextInt();
            Product product = new Product(nameProduct , priceProduct);
            OrdemItem ordemItem = new OrdemItem(quantidade, priceProduct , product);
            order.addItem(ordemItem);
        }

        System.out.println(order);
        System.out.println(client);



    }
}
