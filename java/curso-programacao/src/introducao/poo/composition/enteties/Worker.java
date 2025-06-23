package introducao.poo.composition.enteties;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class Worker {
    private String name;
    private WorkerLevel level;
    private Double baseSalary;

    private Department department;
    private List<HourContrant> contrants = new ArrayList<>();


    public Worker(String name, WorkerLevel level, Double baseSalary, Department department) {
        this.name = name;
        this.level = level;
        this.baseSalary = baseSalary;
        this.department = department;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


    public Double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(Double baseSalary) {
        this.baseSalary = baseSalary;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    public void setLevel(WorkerLevel level) {
        this.level = level;
    }

    public WorkerLevel getLevel() {
        return level;
    }

    public List<HourContrant> getContrants() {
        return contrants;
    }

    public void setContrants(List<HourContrant> contrants) {
        this.contrants = contrants;
    }

    public void addContrant(HourContrant contrant) {
        contrants.add(contrant);
    }

    public void removeContrant(HourContrant contrant) {
        contrants.remove(contrant);
    }

    public double income(int year, int mouth) {
        double sum = baseSalary;
        Calendar cal = Calendar.getInstance();
        for (HourContrant c : contrants) {
            cal.setTime(c.getDate());
            int c_year = cal.get(Calendar.YEAR);
            int c_mouth = 1 + cal.get(Calendar.MONTH);
            if (c_mouth == mouth && c_year == year) {
                sum += c.totalValue();
            }
        }
        return sum;
    }

}
