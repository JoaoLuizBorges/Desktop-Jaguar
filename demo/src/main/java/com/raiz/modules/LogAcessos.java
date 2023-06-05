package com.raiz.modules;

/**
 * Classe Java contendo os métodos Busca(),Registro() e Entrar(). As quais realizam respectivamente:
 * 
 * Busca(), faz a chamada do método Entrar() dentro da criação da String InfoUser, que irá receber as
 * informações de usuario e login. Para depois passar como parâmetro a String InfoUser para o método
 * ConsultaLogin da Classe QUeriesDados.
 * 
 * Registro(), faz a chamada do métrodo Registro(), também dentro da String InfoUser, que irá receber as
 * informações de usuario e login. Para depois, passar como parâmetro a String InfoUser para o método
 * VerificaDados(),[que verifica se os dados de InfoUser já estão dentro do banco de dados] e também para
 * o método PopulandoLogin(), [que insere os dados de InfoUser dentro do banco de dados, se não existir]
 * Os condicionais de Registro(), funcionam do seguinte modo:
 * 
 * if, vai para método Busca()
 * else if, sai do programa
 * else, executa o condicional novamente em caso de opção inválida
 * 
 * Entrar(), recebe os dados inseridos pelo usuário dentro de um vetor String chamado InfoUser.
 * 
 * @author joaob
 */

import java.util.Scanner;
import java.sql.SQLException;

public class LogAcessos {

    public static void Busca () throws SQLException {
            
        String[] InfoUser = LogAcessos.Entrar();
        System.out.println("Logando...");
        QueriesDados.ConsultaLogin(InfoUser[0],InfoUser[1]);
            
    }

	public static void Registro () throws SQLException{
		
		String[] InfoUser = LogAcessos.Entrar();
        System.out.println("Estamos verificando seu acesso!");
        QueriesDados.VerificaDados(InfoUser[0],InfoUser[1]);
        
		System.out.println("Criando acesso...");
		QueriesDados.PopulandoLogin(InfoUser[0],InfoUser[1]);
        
        try(Scanner inputScanner = new Scanner(System.in)){

        System.out.println("Acesso criado! Deseja fazer o login? [S]/[N]");
        String EscolhaUsuario = inputScanner.nextLine();
        EscolhaUsuario = EscolhaUsuario.toUpperCase().trim();
        System.out.println(EscolhaUsuario); 

            for(;;){
                do{
                    if(EscolhaUsuario.equals("S")){
                        System.out.println("Indo para o Login");
                        LogAcessos.Busca();

                    }else if(EscolhaUsuario.equals("N")) {
                        System.out.println("Saindo do programa...");
                        System.exit(1);
                    }else
                        System.out.println("Insira uma opção válida");
                        System.out.println("É a sua primeira vez acessando o sistema? [S]/[N]: ");
						EscolhaUsuario = inputScanner.nextLine();
						EscolhaUsuario = EscolhaUsuario.toUpperCase().trim();

                }while (EscolhaUsuario.equals("S") || EscolhaUsuario.equals("N"));
            }                   
        }     
    }
	
	public static String[] Entrar(){
        
        Scanner UserScanner = new Scanner(System.in);
        String [] InfoUser = new String[2];
		    try{
                System.out.println("Insira o usuário: ");
                if(UserScanner.hasNextLine()){
                    String LoginUser = UserScanner.next();
                    InfoUser[0] = LoginUser;
                }
                System.out.println("Insira a senha: ");
                if(UserScanner.hasNextLine()){
                    String SenhaUser = UserScanner.next();
                    InfoUser[1] = SenhaUser;
                }
            }finally{
                //UserScanner.close();
            }
        return InfoUser;
    }		
}

