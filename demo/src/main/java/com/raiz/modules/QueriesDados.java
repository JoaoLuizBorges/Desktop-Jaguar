package com.raiz.modules;

/**
 * Classe Java contendo os métodos VerificaDados(),VerificaExiste(),PopulandoLogin(),ConsultaLogin()
 * que realizam respectivamente: A verificação dos dados de login; A averiguação que se o banco de dados 
 * existe (temporário?); A população da tabela usuarios, dentro do banco de dados db_local; A consulta
 * dos dados de db_local.
 * 
 * @author joaob
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.InputStream;

public class QueriesDados{

    public static void ConectaPython() throws SQLException{
        
        String SCRIPTPATH = "C:\\Users\\joaob\\Desktop\\Desenvolvimento\\AppJaguar\\src\\main.py";
        try{InputStream is = new FileInputStream("InfoCliente.json");
            //JSONParser parser = new JSONParser();

            
            ProcessBuilder pb = new ProcessBuilder("python",SCRIPTPATH);
            Process p = pb.start();
            
                   
        }catch(Exception e){
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
    }

    public static void VerificaExisteMonit() throws SQLException{
        System.out.println("TESTE");
        Connection conexao = null;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexao = DriverManager.getConnection("jdbc:mysql://localhost/mysql?","root","@Zt3cenergia");              
            Statement stmt = (Statement)conexao.createStatement();
            String verdbString = "CREATE DATABASE IF NOT EXISTS db_local;";
            stmt.executeUpdate(verdbString);
            String useString = "USE db_local;";
            stmt.executeUpdate(useString);
            String vertabString = "CREATE TABLE IF NOT EXISTS geracao(id_locais VARCHAR(50) NOT NULL, nome_cliente VARCHAR(50) NOT NULL, energia_dia VARCHAR(50), PRIMARY KEY (id_locais));";
            stmt.executeUpdate(vertabString);

        }catch(ClassNotFoundException ex) {
                System.out.println("Driver do banco de dados não localizado");
        }catch (SQLException ex) {
                System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }finally{
            if(conexao != null){
                conexao.close();
            }
        }
    }

    public static void PopulandoMonit(String id_locais,String nome_cliente,String energia_dia) throws SQLException{

        String url = "jdbc:mysql://localhost/db_local";
            String usuariodb = "root";
            String senhadb = "@Zt3cenergia";

            try{
                Class.forName("com.mysql.cj.jdbc.Driver");
            }catch (ClassNotFoundException e){
                e.printStackTrace();
            }

            QueriesDados.VerificaExisteMonit();

            try(Connection conexao = DriverManager.getConnection(url,usuariodb,senhadb)){

                Statement stmt = (Statement)conexao.createStatement();
                String insert = "INSERT INTO usuarios VALUES('"+id_locais+"','"+nome_cliente+"','"+energia_dia+"')";
                stmt.executeUpdate(insert);
                conexao.close();
                
            }catch (SQLException ex) {
                System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
            } 
	}	

    public static void VerificaDados(String usuario, String senha) throws SQLException{
        
        String url = "jdbc:mysql://localhost/db_local";
        String usuariodb = "root";
        String senhadb = "@Zt3cenergia";

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        QueriesDados.VerificaExisteUsuarios();

        try(Connection conexao = DriverManager.getConnection(url,usuariodb,senhadb)){

            Statement stmt = (Statement)conexao.createStatement();
            String select = "SELECT usuario FROM usuarios WHERE usuario = '"+usuario+"'";
            ResultSet rs = stmt.executeQuery(select);

            if(rs.next() == true){
                conexao.close();
                System.out.println("Este usuário já existe!");
                try(Scanner sc = new Scanner(System.in)){
                
                System.out.println("Deseja fazer login? [S]/[N]");
                String EscolhaUsario = sc.nextLine();
                EscolhaUsario = EscolhaUsario.toUpperCase().trim();
                System.out.println(EscolhaUsario);

                    for(;;){
                         do{
                            if(EscolhaUsario.equals("S")){
                                System.out.println("Indo para o Login!");
                                LogAcessos.Busca();
                            }else if(EscolhaUsario.equals("N")){
                                System.out.println("Saindo do programa");
                                System.exit(1);
                            }else
                                System.out.println("Insira uma opção válida");
                                System.out.println("Deseja fazer o login? [S]/[N]: ");
                                EscolhaUsario = sc.nextLine();
                                EscolhaUsario = EscolhaUsario.toUpperCase().trim(); 

                        }while(EscolhaUsario.equals("S") || EscolhaUsario.equals("N"));
                    }
                }
            }                                     
        }catch (SQLException ex) {
            System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }
    }

    public static void VerificaExisteUsuarios() throws SQLException{
        Connection conexao = null;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexao = DriverManager.getConnection("jdbc:mysql://localhost/mysql?","root","@Zt3cenergia");              
            Statement stmt = (Statement)conexao.createStatement();
            String verdbString = "CREATE DATABASE IF NOT EXISTS db_local;";
            stmt.executeUpdate(verdbString);
            String useString = "USE db_local;";
            stmt.executeUpdate(useString);
            String vertabString = "CREATE TABLE IF NOT EXISTS usuarios (usuario VARCHAR(50) NOT NULL, senha VARCHAR(50) NOT NULL, PRIMARY KEY (usuario));";
            stmt.executeUpdate(vertabString);

        }catch(ClassNotFoundException ex) {
                System.out.println("Driver do banco de dados não localizado");
        }catch (SQLException ex) {
                System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }finally{
            if(conexao != null){
                conexao.close();
            }
        }
    }
    
	public static void PopulandoLogin (String usuario,String senha) throws SQLException{

            String url = "jdbc:mysql://localhost/db_local";
            String usuariodb = "root";
            String senhadb = "@Zt3cenergia";

            try{
                Class.forName("com.mysql.cj.jdbc.Driver");
            }catch (ClassNotFoundException e){
                e.printStackTrace();
            }

            QueriesDados.VerificaExisteUsuarios();

            try(Connection conexao = DriverManager.getConnection(url,usuariodb,senhadb)){

                Statement stmt = (Statement)conexao.createStatement();
                String insert = "INSERT INTO usuarios VALUES('"+usuario+"','"+senha+"')";
                stmt.executeUpdate(insert);
                conexao.close();
                
            }catch (SQLException ex) {
                System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
            } 
	}	

	public static void ConsultaLogin(String usuario,String senha) throws SQLException {
	        
            String url = "jdbc:mysql://localhost/db_local";
            String usuariodb = "root";
            String senhadb = "@Zt3cenergia";

            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }

            QueriesDados.VerificaExisteUsuarios();

            try(Connection conexao = DriverManager.getConnection(url,usuariodb,senhadb)){

                Statement stmt = (Statement)conexao.createStatement();
                String select = "SELECT usuario,senha FROM usuarios WHERE usuario = '"+usuario+"' AND senha = '"+senha+"'";
                ResultSet rs = stmt.executeQuery(select);

                if(rs.next() ==  true){
                    conexao.close();
                    System.out.println("Dados verificados!");
                    System.out.println("Aqui vamos entrar no programa!");
                    QueriesDados.ConectaPython();
                    System.exit(1);
                }else{
                    conexao.close();
                    System.out.println("Login incorreto... Tente novamente");
                    LogAcessos.Busca();   
                }                                   
                    
            }catch (SQLException ex) {
                System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
            }
	    }    
    }  
 