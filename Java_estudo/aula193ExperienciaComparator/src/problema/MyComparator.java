package problema;

import entidade.Produto2;

import java.util.Comparator;

public class MyComparator implements Comparator<Produto2> {

    @Override
    public int compare(Produto2 p1, Produto2 p2) {
        return p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase());
    }
}
