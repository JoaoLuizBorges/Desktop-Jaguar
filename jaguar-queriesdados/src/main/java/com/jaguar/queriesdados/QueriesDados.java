package com.jaguar.queriesdados;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.jaguar.logacessos.LogAcessos;
import org.jetbrains.annotations.NotNull;
import org.json.simple.parser.JSONParser;
import java.io.FileReader;
import org.python.util.PythonInterpreter;
import java.sql.*;
import java.util.*;
import java.util.concurrent.TimeUnit;
import java.io.File;

public class QueriesDados {
    public static void ConectaPython() throws Exception {

        try {
            String SCRIPTPATH = "C:\\Users\\joaob\\Desktop\\Desenvolvimento\\jaguar\\python\\main.py";
            PythonInterpreter interpreter = new PythonInterpreter();
            interpreter.exec(SCRIPTPATH);
        } catch(Exception e){
            e.printStackTrace();
        }
        //Process pb = new ProcessBuilder("python", "C:\\Users\\joaob\\Desktop\\Desenvolvimento\\jaguar\\python\\main.py").start();
        String JSONPATH = "C:\\Users\\joaob\\Desktop\\Desenvolvimento\\jaguar\\python\\InfoCliente.json";
        File f = new File(JSONPATH);
        if (f.exists()) {
            try {
                String key = null;
                ArrayList<String> value = new ArrayList<String>();
                JSONParser parser = new JSONParser();
                Object object = parser.parse(new FileReader(JSONPATH));
                String Dados = object.toString();
                ObjectMapper mapper = new ObjectMapper();

                Map<String, ArrayList<String>> map = mapper.readValue(Dados, Map.class);

                for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
                    value.add(entry.getValue().toString());
                }
                String[] idArr = null;
                String id = value.get(0);
                id = id.replaceAll("'", "").replace("[", " ");
                idArr = id.split(",");

                String[] nomeClienteArr = null;
                String nomeCliente = value.get(1);
                nomeCliente = nomeCliente.replaceAll("'", "").replace("[", " ");
                nomeClienteArr = nomeCliente.split(",");

                String[] geracaodiaArr = null;
                String geracaoDia = value.get(2);
                geracaoDia = geracaoDia.replaceAll("'", "").replace("[", " ");
                geracaodiaArr = geracaoDia.split(",");

                for (int i = 0; i < idArr.length - 1; i++) {
                    QueriesDados.QueriesMonit(idArr[i], nomeClienteArr[i], geracaodiaArr[i]);
                }

            }catch(Exception e){
                e.printStackTrace();
            }
        }
    }
    public static String @NotNull [] Conecta(){

        String [] conecta = new String [3];

        conecta[0] = "jdbc:mysql://localhost/local";
        conecta[1] = "root";
        conecta[2] = "@Zt3cenergia";

        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
        }catch (ClassNotFoundException e){
            e.printStackTrace();
        }
        return conecta;
    }
    public static void QueriesMonit(String id_locais, String nome_cliente, String energia_dia) throws SQLException{

        String [] conecta = QueriesDados.Conecta();

        QueriesDados.VerificaExisteLocal();

        try(Connection conexao = DriverManager.getConnection(conecta[0],conecta[1],conecta[2])){

            Statement stmt = (Statement)conexao.createStatement();
            String select = "SELECT id_locais, nome_cliente FROM geracao WHERE id_locais = '"+id_locais+"'";
            ResultSet rs = stmt.executeQuery(select);

            if(rs.next()) {
                String update = "UPDATE geracao SET energia_dia = ? WHERE id_locais = ?;";
                PreparedStatement st = conexao.prepareStatement(update);
                st.setString(1,energia_dia);
                st.setString(2,id_locais);
                st.executeUpdate();
                conexao.close();
                TimeUnit.SECONDS.sleep(3);
                File f = new File("C:\\Users\\joaob\\Desktop\\Desenvolvimento\\jaguar\\python\\InfoCliente.json");
                f.delete();

            }else {
                Statement stmtInsert = (Statement) conexao.createStatement();
                String insert = "INSERT INTO geracao VALUES ('" + id_locais + "','" + nome_cliente + "','" + energia_dia + "')";
                stmtInsert.executeUpdate(insert);
                conexao.close();
                TimeUnit.SECONDS.sleep(3);
                File f = new File("C:\\Users\\joaob\\Desktop\\Desenvolvimento\\jaguar\\python\\InfoCliente.json");
                f.delete();

            }
        }catch (SQLException ex){
            System.out.println("Ocorreu um erro ao acessar o banco: " +ex.getMessage());
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
    public static void VerificaDados(String usuario, String senha) throws SQLException{

        String [] conecta = QueriesDados.Conecta();

        QueriesDados.VerificaExisteLocal();

        try(Connection conexao = DriverManager.getConnection(conecta[0],conecta[1],conecta[2])){

            Statement stmt = (Statement)conexao.createStatement();
            String select = "SELECT usuario FROM usuarios WHERE usuario = '"+usuario+"'";
            ResultSet rs = stmt.executeQuery(select);

            if(rs.next()){
                conexao.close();
                System.out.println("Este usuário já existe!");
                LogAcessos.ControleAcesso();
            }
        }catch(SQLException ex){
            System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }
    }
    public static void VerificaExisteLocal() throws SQLException{
        Connection conexao = null;
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexao = DriverManager.getConnection("jdbc:mysql://localhost/mysql?","root","@Zt3cenergia");
            Statement stmt = (Statement)conexao.createStatement();
            String criadbString = "CREATE DATABASE IF NOT EXISTS local;";
            stmt.executeUpdate(criadbString);
            String usedbString = "USE local;";
            stmt.executeUpdate(usedbString);
            String criatbUsuarios = "CREATE TABLE IF NOT EXISTS usuarios (usuario VARCHAR(50) NOT NULL, senha VARCHAR(50) NOT NULL, PRIMARY KEY (usuario));";
            String criatbGeracao = "CREATE TABLE IF NOT EXISTS geracao (id_locais VARCHAR(50) NOT NULL, nome_cliente VARCHAR(50) NOT NULL, energia_dia VARCHAR(50), PRIMARY KEY (id_locais));";

            stmt.executeUpdate(criatbUsuarios);
            stmt.executeUpdate(criatbGeracao);

        }catch(ClassNotFoundException ex){
            System.out.println("Driver do banco de dados não localizado");
        }catch(SQLException ex){
            System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }finally {
            if(conexao != null){
                conexao.close();
            }
        }
    }
    public static void PopulandoLogin(String usuario, String senha) throws SQLException{

        String [] conecta = QueriesDados.Conecta();

        QueriesDados.VerificaExisteLocal();

        try(Connection conexao = DriverManager.getConnection(conecta[0],conecta[1],conecta[2])){

            Statement stmt = (Statement)conexao.createStatement();
            String insert = "INSERT INTO usuarios VALUES('"+usuario+"','"+senha+"');";
            stmt.executeUpdate(insert);
            conexao.close();

        }catch (SQLException ex){
            System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        }
    }
    public static void ConsultaLogin(String usuario, String senha) throws SQLException{

        String [] conecta = QueriesDados.Conecta();

        QueriesDados.VerificaExisteLocal();

        try(Connection conexao = DriverManager.getConnection(conecta[0],conecta[1],conecta[2])){

            Statement stmt = (Statement)conexao.createStatement();
            String select = "SELECT usuario,senha FROM usuarios WHERE usuario = '"+usuario+"' AND senha = '"+senha+"';";
            ResultSet rs = stmt.executeQuery(select);

            if(rs.next()){
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
        }catch (SQLException ex){
            System.out.println("Ocorreu um erro ao acessar o banco: " + ex.getMessage());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
