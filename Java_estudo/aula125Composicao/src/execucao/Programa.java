package execucao;
import entidades.Comment;
import entidades.Post;

import java.text.ParseException;
import java.text.SimpleDateFormat;

public class Programa {
    public static void main(String[] args)throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        Comment c1 = new Comment("Tenha um bom dia ");
        Comment c2 = new Comment("Que incrível ");
        Post p1 = new Post(
                sdf.parse("21/06/2018 13:05:44 "),
                "Estando na Nova Zelândia ","Vou visitar esse país lindo ",12);
        p1.addComment(c1);
        p1.addComment(c2);

        System.out.println(p1);
    }

}
