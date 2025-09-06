public class Anotacao {
//expressão comparativas:
//operadores comparativos:
// > maior
// < menor
// >= maior ou igual
// <= menor ou igual
// == igual
// != diferente

// Exemplos de expressões comparativas
// int x = 5;
// X > 0 Resultado: V
// X == 3 Resultado: F
// 10 <= 30 Resultado: V
// X != 2 Resultado: V

// Operadores lógicos:
// && = E
// || = OU
// ! = NÃO


// Exemplos de expressões lógicas com o E (&&):
//        (suponha x igual a 5)

//        X <= 20 && X == 10 = Resultado: F

//        X > 0 && X != 3 = Resultado: V

//        X <= 20 && X == 10 && X != 3 Resultado: F



//        Exemplos de expressões lógicas com o OU (||):
//        (suponha x igual a 5)
//        X > 0 || X != 3
//        V         V
//        Resultado: V

//        X == 10 || X <= 20
//        F             V
//        Resultado: V

//        X <= 0 || X != 3 || X != 5
//        F             V       F
//        Resultado: V


//        Exemplos de expressões lógicas com o NÃO (!):

//        (suponha x igual a 5)
//        !(X == 10)
//            F
//        Resultado: V

//        !(X >= 2)
//            V
//        Resultado: F



//        Exemplos de expressões lógicas com o NÃO (!):
//        (suponha x igual a 5)

//        !(X <= 20 && X == 10)
//            V            F
//                   F
//             V
//        Resultado: V



//        Conceito:

//        Estrutura condicional:

//        É uma estrutura de controle
//        que permite definir que um
//        certo bloco de comandos
//        somente será executado
//        dependendo de uma condição



        //Sintaxe da estrutura condicional simples:

        //if ( <condição> ) {
        //<comando 1>
        //<comando 2>
        //}

        //Importante:
        //Repare na endentação!

        //REGRA:
        //V: executa o bloco de comandos
        //F: pula o bloco de comandos


        //Sintaxe da estrutura condicional Composta:
        //REGRA:
        //V: executa somente o bloco do if
        //F: executa somente o bloco do else

        //if ( <condição> ) {
        //<comando 1>
        //<comando 2>
        //}

        //else {
        //<comando 3>
        //<comando 4>
        //}

        //Encadeamento de estruturas condicionais:

        //if ( condição 1 ) {
        //comando 1
        //comando 2
        //}

        //else {
        //if ( condição 2 ) {
        //comando 3
        //comando 4
        //}
        //else {
        //comando 5
        //comando 6
        //}
//  }  
}
