package introducao.poo;

public class hasdCodeOrEquals {
    public static void main(String[] args) {
        String a = "Alex";
        String c = "Alex";
        String b = "Maria";
        System.out.println(a.hashCode() == c.hashCode());
        System.out.println(b.hashCode());

        //hashCode e equals personalizados com classes
    }
}
