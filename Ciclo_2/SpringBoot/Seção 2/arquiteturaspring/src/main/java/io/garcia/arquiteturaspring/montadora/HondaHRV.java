package io.garcia.arquiteturaspring.montadora;

import java.awt.*;

public class HondaHRV extends Carro {
    public HondaHRV(Motor motor) {
        super(motor);
        setModelo("HRV");
        setCor(String.valueOf(Color.BLACK));
        setMontadora(Montadora.HONDA);
    }
}
