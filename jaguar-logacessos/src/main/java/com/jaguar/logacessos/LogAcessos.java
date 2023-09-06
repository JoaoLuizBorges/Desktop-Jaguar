package com.jaguar.logacessos;
import com.jaguar.Usuario;
import com.jaguar.queriesdados.QueriesDados;
import org.jetbrains.annotations.NotNull;
import java.sql.SQLException;
import java.util.Scanner;

public class LogAcessos {

    public static void ControleAcesso() throws SQLException {

        try (Scanner inputScanner = new Scanner(System.in)) {
            System.out.println("Deseja fazer o login? <S>/<N>: ");
            String escolhaUsuario = inputScanner.nextLine();
            escolhaUsuario = escolhaUsuario.toUpperCase().trim();
            System.out.println(escolhaUsuario);

            for (;;) {
                do {
                    if (escolhaUsuario.equals("S")) {
                        System.out.println("Indo para o Login!");
                        LogAcessos.Busca();
                    } else if (escolhaUsuario.equals("N")) {
                        System.out.println("Saindo do programa...");
                        System.exit(1);
                    } else System.out.println("Insira uma opção válida");
                        System.out.println("É a sua primeira vez acessando o sistema? <S>/<N>: ");
                        escolhaUsuario = inputScanner.nextLine();
                        escolhaUsuario = escolhaUsuario.toUpperCase().trim();

                } while (escolhaUsuario.equals("S") || escolhaUsuario.equals("N"));
            }
        }
    }
    public static void Busca() throws SQLException {
        String[] infoUser = LogAcessos.Entrar();
        System.out.println("Logando...");
        QueriesDados.ConsultaLogin(infoUser[0], infoUser[1]);
    }
    public static void Registro() throws SQLException {
        String[] infoUser = LogAcessos.Entrar();
        System.out.println("Estamos verificando seu acesso!");
        QueriesDados.VerificaDados(infoUser[0], infoUser[1]);

        System.out.println("Criando acesso!");
        QueriesDados.PopulandoLogin(infoUser[0], infoUser[1]);

        LogAcessos.ControleAcesso();
    }
    private static String @NotNull [] Entrar(){
        Scanner userScanner = new Scanner(System.in);
        String [] infoUser = new String[2];
        try{
            System.out.println("Insira um usuário: ");
            if(userScanner.hasNextLine()){
                String loginUser = userScanner.nextLine();
                loginUser = loginUser.replaceAll("\\s", "");
                infoUser[0] = loginUser;
            }
            System.out.println("Insira a senha: ");
            if(userScanner.hasNextLine()){
                String senhaUser = userScanner.nextLine();
                senhaUser = senhaUser.replaceAll("\\s","");
                infoUser[1] = senhaUser;

            }
        }catch(Exception e){
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
    return infoUser;
    }
}