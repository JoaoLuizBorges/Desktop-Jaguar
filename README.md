# Aplicativo Jaguar

<p align="justify"> 
O seguinte projeto tem como objetivo agregar as informações vindas dos principais Monitoramentos
de Sistemas Fovoltaicos. Tais monitoramentos realizam a aquisição de dados por meio de suas 
respectivas aplicações web.
</p>

Neste aplicativo temos agregados os seguintes monitoramentos: 

 | Monitoramento |    Adicionado    | Estado                     |
 |---------------|------------------|----------------------------|
 | SolarEdge     | Quinto Commit    | _Funcional_                |
 | SolarMan      | Oitavo Commit    | _Funcional_                |
 | Hoymilles     | Oitavo Commit    | _Pausar Desenvolvimento_   |
 | Canadian      | Oitavo Commit    | _Funcional_                |
 | REFUlog       | Oitavo Commit    | _Pausar Desenvolvimento_   |
 | AuroraVision  | Nono Commit      | _Site Inoperante_          |
 | Growatt       | Nono Commit      | _Funcional_                |
 | EcoSolys      | Décimo Commit    | _Sistema GD não conectado_ |
 | Fronius       | Undécimo Commit  | _API indisponível_         |

## Estrutura e Fluxo do pragrama

### Estrutura

Por enquanto, no Undécimo Commit, o projeto utiliza a seguinte estrutra:

* Interface com o usuário:
  - _AppJaguar.java_ - Java 20 usando da ferramento MAVEN (**Provisório**)
  - _LogAcesso.java_ - Java 20 usando da ferramento MAVEN (**Provisório**)
    
* Interface e Controle do Banco de Dados:
  - _QueriesDados.java_ - Java 20 usando da ferramento MAVEN
    
* Consumo de API e _requests_:
  - Scripts python - Python 3.11

### Fluxo do programa

<img src = "https://github.com/JoaoLuizBorges/Desktop-Jaguar/blob/master/Fluxograma%20Jaguar.png" />

## Objetivos futuros

- [ ] Estudos da linguagem JavaScript;
- [ ] Estudos de Mecanismos de autênticação, por exemplo OAtuh2;
- [ ] Estudos Java;
> * ~~Anotações Inferidas;~~
> * ~~Expressões Lambda;~~
> * ~~Modificadores de Acesso;~~
> * Spring framework.
- [ ] Estudos GitHub;
- [X] ~~Rever Programação Orientada a Objeto;~~
- [ ] Docker;
- [ ] Automação de Processos.
> * CyPress;
> * ~~PyAutoGui~~;
> * RPA (?).
