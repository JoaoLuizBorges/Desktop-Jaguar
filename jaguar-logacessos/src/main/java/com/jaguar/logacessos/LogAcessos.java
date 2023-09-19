package com.jaguar.logacessos;
import com.jaguar.queriesdados.QueriesDados;
import org.jetbrains.annotations.NotNull;
import java.sql.SQLException;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.*;


public class LogAcessos {
    @NotNull
    private static String Usuario() {

        Scanner userScanner = new Scanner(System.in);
        String loginUser = "";

        try {
            System.out.println("Insira um usuário: ");
            if (userScanner.hasNextLine()) {
                loginUser = userScanner.nextLine();
                loginUser = loginUser.replaceAll("\\s", "");

                if (loginUser.isEmpty()) {
                    System.out.println("Tente novamente!");
                    loginUser = LogAcessos.Usuario();
                }
            }

        } catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
        return loginUser;
    }
    @NotNull
    private static String Senha() {

        Scanner userScanner = new Scanner(System.in);
        String senhaUser = "";

        try {

            System.out.println("Insira uma senha de, no mínimo oito caracteres, que inclua,"
                                + "ao menos, uma letra maiúscula e uma letra minúscula e,"
                                + "no mínimo um caractere especial e um número: ");

            if (userScanner.hasNextLine()) {
                senhaUser = userScanner.nextLine();
                senhaUser = senhaUser.replaceAll("\\s", "");
                Pattern regex = Pattern.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$");
                Matcher matcher = regex.matcher(senhaUser);

                if (!matcher.matches()) {
                    System.out.println("Tente novamente!");
                    senhaUser = LogAcessos.Senha();
                }
            }

        } catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }

        return senhaUser;
    }
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
    private static String @NotNull [] Entrar() {

        String[] infoUser = new String[2];

        try {

            infoUser[0] = LogAcessos.Usuario();
            infoUser[1] = LogAcessos.Senha();

        } catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
        return infoUser;
    }
}
