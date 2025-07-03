package entities;

import java.util.Objects;

public class LogEntry implements Comparable<LogEntry>{
    private String username;
    private Double price;

    public LogEntry(String username, Double price) {
        this.username = username;
        this.price = price;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        LogEntry logEntry = (LogEntry) o;
        return Objects.equals(username, logEntry.username);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(username);
    }

    @Override
    public int compareTo(LogEntry other) {
        return username.compareTo(other.username);
    }
}
