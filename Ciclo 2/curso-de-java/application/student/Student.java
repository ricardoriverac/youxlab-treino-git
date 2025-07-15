package application.student;

public class Student {
    private String name;
    private double grade1, grade2, grade3;

    public Student(String name, double grade1, double grade2, double grade3) {
        this.name = name;
        this.grade1 = grade1;
        this.grade2 = grade2;
        this.grade3 = grade3;
    }

    public double finalGrade() {
        return grade1 + grade2 + grade3;
    }

    public boolean isPassed() {
        return finalGrade() >= 60.0;
    }

    public double missingPoints() {
        if (isPassed()) {
            return 0.0;
        }
        return 60.0 - finalGrade();
    }

    public String getName() {
        return name;
    }
}