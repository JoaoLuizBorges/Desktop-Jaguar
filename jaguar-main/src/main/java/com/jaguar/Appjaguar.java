package com.jaguar;
import com.jaguar.logacessos.LogAcessos;
import java.util.Scanner;

public class Appjaguar {
    public static void main(String[] args) throws Exception{
        try(Scanner inputUser = new Scanner(System.in)){
            for(;;){
                System.out.print("É a sua primeira vez acessando o sistema? <S>/<N>: ");
                String escolhaUsuario = inputUser.nextLine();
                escolhaUsuario = escolhaUsuario.toUpperCase().trim();
                System.out.println(escolhaUsuario);

                do{
                    if(escolhaUsuario.equals("S")){
                        System.out.println("Indo para o Registro!");
                        LogAcessos.Registro();
                    } else if (escolhaUsuario.equals("N")) {
                        System.out.println("Indo para o Login!");
                        LogAcessos.Busca();
                    }else
                        System.out.print("Insira uma opção válida!");
                        System.out.println("É a sua primeira vez acessando o sistema? <S>/<N>: ");
                        escolhaUsuario = inputUser.nextLine();
                        escolhaUsuario = escolhaUsuario.toUpperCase().trim();

                }while(escolhaUsuario.equals("S") || escolhaUsuario.equals("N"));
            }
        }
    }
}
