package introducao.poo.herance_poliformismo.exercicies.aplication;

import introducao.poo.herance_poliformismo.exercicies.entities.ImportedProduct;
import introducao.poo.herance_poliformismo.exercicies.entities.Product;
import introducao.poo.herance_poliformismo.exercicies.entities.UsedProduct;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class aplicationProduct {
    public static void main(String[] args) throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner input = new Scanner(System.in);

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        List<introducao.poo.herance_poliformismo.exercicies.entities.Product> products = new ArrayList<>();

        System.out.print("Enter the number of products: ");
        int quant = input.nextInt();
        for (int i = 0; i < quant; i++) {
            System.out.printf("Product #%d data: %n", (i+1));
            System.out.print("Common, used or import (c/u/i)? ");
            char resp = input.next().charAt(0);
            System.out.print("Name: ");
            input.nextLine();
            String name = input.nextLine();
            System.out.print("Price: ");
            double price = input.nextDouble();
            if (resp == 'i'){
                System.out.print("Customs fee: ");
                double customfee = input.nextDouble();
                introducao.poo.herance_poliformismo.exercicies.entities.Product iproduct = new ImportedProduct(name , price , customfee);
                ((ImportedProduct) iproduct).totalPrice(customfee);
                products.add(iproduct);
            } else if (resp == 'u') {
                System.out.print("Manufacture Date (DD/MM/YYYY): ");
                Date manufacture = sdf.parse(input.next());
                Product product = new UsedProduct(name , price , manufacture);
                products.add(product);
            }
            else {
                Product product = new Product(name , price);
                products.add(product);

            }
        }
        System.out.println("Price Tags: ");
        for (Product product : products) {
            System.out.println(product.toString());
        }


    }
}
