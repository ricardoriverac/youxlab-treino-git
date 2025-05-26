package desafiobanco;

import java.util.List;
import java.util.ArrayList;


public class BancoKev {
    List<ContaBancaria> contas = new ArrayList<>();

    void adicionarConta(ContaBancaria conta){
        contas.add(conta);
    }
    

    ContaBancaria buscarConta(int numeroConta){
        for(ContaBancaria conta : contas){
            if(conta.numero == numeroConta){
                return conta;
            }
        }
        return null;
    }


    void exibirConta(int numeroConta){
        ContaBancaria conta = buscarConta(numeroConta);
        if(conta == null){
            System.out.println("Não foi possivel achar a conta " + numeroConta);
        }
        else{
            System.out.println("Conta encontrada com sucesso! ");
            System.out.println(conta);
        }

    }



    void transferir(int origem, int destino, double valor){
        ContaBancaria contaOrigem = buscarConta(origem);
        ContaBancaria contaDestino = buscarConta(destino);

        if (contaOrigem == null && contaDestino == null){
            System.out.println("Não encontramos as contas de origem e destino");
        }
        else{
            if(valor > contaOrigem.saldo){
                System.out.println("Não será possivel transferir! ");
            }
            else{
                if(valor <= contaOrigem.saldo){
                    contaOrigem.saldo -= valor;
                    contaDestino.saldo += valor;
                    System.out.println("Transferencia Realizada com sucesso! ");
                }
            }
        }
    }

    
}
