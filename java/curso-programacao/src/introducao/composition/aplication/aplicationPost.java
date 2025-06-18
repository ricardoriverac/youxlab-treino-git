package introducao.composition.aplication;

import introducao.composition.enteties.Comment;
import introducao.composition.enteties.Post;

import java.text.ParseException;
import java.text.SimpleDateFormat;

public class aplicationPost {
    public static void main(String[] args) throws ParseException {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        Comment c1 = new Comment("Uau que incrivel");
        Comment c2 = new Comment("Queria ter ido");
        Post p1 = new Post(sdf.parse("21/06/2018 13:05:44") , "Indo para nova zelandia" , "Primeira viagem do ano vai ser incrível" , 12);
        p1.addComments(c1);
        p1.addComments(c2);
        System.out.println(p1);
    }
}
