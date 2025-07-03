import entities.LogEntry;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
        Set<LogEntry> logEntries = new TreeSet<>();
        String path = "/home/youx/workspace-git/youxlab-treino-git/java/exercicioSet/src/in.txt";
        BufferedReader bw = new BufferedReader(new FileReader(path));
        String line = bw.readLine();
        while (line != null){
            String[] campos = line.split(" ");
            logEntries.add(new LogEntry(campos[0] , Double.parseDouble(campos[1])));
            line = bw.readLine();
        }
        for (LogEntry logEntry : logEntries) {
            System.out.println(logEntry.getUsername() + ": " + logEntry.getPrice());
        }
    }
}
