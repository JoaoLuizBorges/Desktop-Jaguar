package com.raiz;

/**
 * Método Java que serve como interface principal. A partir daqui o programa ramifica para as opçções desejadas
 * de login. O condicional if, está detalhado abaixo:
 * 
 * if, vai para o método Registro
 * else if, vai para o método Busca
 * else, executa o condicional novamente em caso de opção inválida
 *
 * @author joaob
 */
import java.util.Scanner;
import modules;

public class AppJaguar {
	
    public static void main(String args[]) throws Exception{
		
		try(Scanner inputUser = new Scanner(System.in)){

			for(;;){
				
				System.out.println("É a sua primeira vez acessando o sistema? [S]/[N]: ");
				String EscolhaUsuario = inputUser.nextLine();
				EscolhaUsuario = EscolhaUsuario.toUpperCase().trim();
				System.out.println(EscolhaUsuario); 
				
				do{
					if(EscolhaUsuario.equals("S")){
						System.out.println("Indo para o Registro");
						//LogAcessos.Registro();
					}else if(EscolhaUsuario.equals("N")) {
						System.out.println("Indo para Login");
						//LogAcessos.Busca();
					}else
						System.out.println("Insira uma opção válida");
						System.out.println("É a sua primeira vez acessando o sistema? [S]/[N]: ");
						EscolhaUsuario = inputUser.nextLine();
						EscolhaUsuario = EscolhaUsuario.toUpperCase().trim();
						
				} while (EscolhaUsuario.equals("S") || EscolhaUsuario.equals("N"));	
			}
		}					
	}
}


	
