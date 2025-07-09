import entities.Product;

import java.util.Comparator;

// e uma interface funcional
public class Mycomparator implements Comparator<Product> {
    @Override
    public int compare(Product o1, Product o2) {
        return o1.getName().toUpperCase().compareTo(o2.getName().toUpperCase());
    }
}
