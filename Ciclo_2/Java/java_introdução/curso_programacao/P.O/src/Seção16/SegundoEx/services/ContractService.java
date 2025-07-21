package Seção16.SegundoEx.services;

import Seção16.SegundoEx.ent.Contract;
import Seção16.SegundoEx.ent.Installment;

import java.time.LocalDate;

public class ContractService {
    private OPS ops;

    public ContractService(OPS ops){
        this.ops = ops;
    }

    public void processContract(Contract contract, int months){
        contract.getInstallments().add(new Installment(LocalDate.of(2018,7,25), 206.04));
        contract.getInstallments().add(new Installment(LocalDate.of(2018,8,25), 208.08));

    }
}
