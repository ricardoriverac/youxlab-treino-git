package introducao.poo.list;

public class unboxing_boxing {
    public static void main(String[] args) {
        int x = 20;
        // Se eu dar wrapped na minha classe como Integer o compilador entende que e tipo references
        Object obj = x;

        System.out.println(obj);

        Integer y = (Integer) obj;


    }
}
