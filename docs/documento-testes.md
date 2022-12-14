# Plano de Teste
 
**Gestor Lab**
 
*versão 0.5*
 
## Histórico das alterações
 
  ## Histórico de Revisão
 
Data | Versão |  Descrição |  Autor
---- | ------ | ---------- | -----
02/05/2022 | 0.0.1 | Detalhamento do User Story RF001 | Eduardo
17/05/2022 |0.0.2|Atualização dos User Stories|Renildo
13/06/2022 |0.0.3|Atualização dos User Stories|Jeison
19/07/2022 |0.0.4|Atualização dos User Stories|Renildo
 
 
 
## 1 - Introdução
 
Lista de Casos de Uso a testar
 
- User Story US01
- User Story US02
- User Story US03
- User Story US04
- User Story US05
- User Story US06
- User Story US07
- User Story US08
- User Story US09
- User Story US10
 
 
 
Também é possível apresentar aqui o programa que será testado.
 
## 2 - Requisitos a Testar
 
### Casos de uso:
 
Codigo User Stories | Nome User Stories
----------- | ----------
US001 | Manter Laboratório
US002 | Manter Linha de Pesquisa
US003 | Manter Membros do Laboratórios
US004 | Manter projetos de Ensino, Pesquisa e Extensão
US005 | Manter Eventos
US006 | Manter Artigos publicados
US007 | Manter TCC
US008 | Manter Horário
US009 | Manter Apresentação
US010 | Manter Estágio
 
 
 
 
 
## 3 - Tipos de teste
 
Esta seção deve conter os tipos de testes escolhidos para cada iteração do projeto.
Pode-se definir inicialmente apenas os tipos de testes que serão usadas na próxima iteração, mas é possível também já registrar eventuais tipos de teste que se espera utilizar nas demais iterações.
Com base no guia de testes, indique os tipos de testes que melhor se adéquam aos requisitos, tipo da aplicação e seus recursos disponíveis e, caso necessário complemente ou forneça mais detalhes da técnica e dos critérios de completude sugeridos no guia para cada tipo de teste indicado.
 
- Teste de interface de usuário;
- Teste de performance;
- Teste de carga;
- Teste de stress;
- Teste de segurança e controle de acesso;
- Teste de instalação;
- Entre outros.
 
### 3.1 - Métodos da Classe
 
Para teste de funcionalidade.
Aqui deve-se verificar se cada classe retorna o esperado.
Se possível usar teste automatizado.
 
</th>
        <th colspan="2">
        </th>
    </tr><br/>
<table>
    <tr>
        <th>
            Objetivo: Teste de Classes
        </th>
        <th colspan="4">
            É realizado teste de unidade no CRUD, verificando a maioria das entradas com resultado correto, e entradas incorretas, verificando se tem o resultado esperado e verificando se o código responde corretamente às situações, como colocar um valor inesperado ou maior que o suportado, por exemplo. Verificar a velocidade de resposta do cadastro. Testar o tipo de retorno.
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            (x) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade (x)
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
         <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
<tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Darlan, Evandir
        </th>
    </tr>
</table>
<br/>
 
</th>
    </tr><br/>
<table>
    <tr>
        <th>
            Objetivo: Teste do User Story 002
        </th>
        <th colspan="4">
            É realizado teste de unidade no cadastro, verificando a maioria das entradas com resultado correto, e entradas incorretas, verificando se tem o resultado esperado e verificando se o código responde corretamente às situações, como colocar um valor inesperado ou maior que o suportado, por exemplo. Verificar a velocidade de resposta do cadastro. Testar o tipo de retorno.
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            (x) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade (x)
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
         <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
<tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Darlan, Evandir
        </th>
    </tr>
</table>
<br/>
 
 
### 3.2 - Persistência de Dados
 
Para teste de integridade de dados e do banco de dados.
Aqui deve-se verificar se os dados não se perdem ao desligar o programa. Se o programa consegue se recuperar em caso de falha ou fechamento repentino.
Se possível usar teste automatizado.
 
<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            Verificar se dados são mantidos após súbito desligamento do programa .
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            (x) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema (x)
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>
 
### 3.3 - Integração dos Componentes
 
Para teste de funcionalidade.
Aqui deve-se verificar se as classes e métodos conseguem fazer a integração entre elas para uma sequência de ações do programa.
Se possível usar teste automatizado.
 
<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            (x) manual
        </th>
        <th colspan="2">
            (x) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração (x)
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca (x)
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>
 
### 3.4 - Tempo de Resposta
 
Para teste de funcionalidade.
Aqui deve-se verificar se o tempo de respostas das ações do programa são consideradas aceitáveis.
Se possível usar teste automatizado.
 
<br/>
<table>
    <tr>
        <th>
            Objetivo
        </th>
        <th colspan="4">
            descreva aqui o objetivo
        </th>
    </tr>
    <tr>
        <th>
            Técnica:
        </th>
        <th colspan="2">
            ( ) manual
        </th>
        <th colspan="2">
            ( ) automática
        </th>
    </tr>
    <tr>
        <th>
            Estágio do teste
        </th>
        <th>
            Integração ( )
        </th>
        <th>
            Sistema ( )
        </th>
        <th>
            Unidade ( )
        </th>
        <th>
            Aceitação ( )
        </th>
    </tr>
    <tr>
        <th>
            Abordagem do teste
        </th>
        <th colspan="2">
            Caixa branca ( )
        </th>
        <th colspan="2">
            Caixa preta ( )
        </th>
    </tr>
    <tr>
        <th>
            Responsável(is)
        </th>
        <th colspan="4">
            Programador(es) ou equipe de testes
        </th>
    </tr>
</table>
<br/>
 
## 4 - Recursos
 
- Python
- Django
- PostgreSQL
- Docker
 
### 4.1 - Ambiente de teste - Software e Hardware
 
Utilizando o framework Django para desenvolvimento de sistemas web,temos acesso a biblioteca de testes, unittests, que além de facilitar a criação de testes unitários, também dá suporte aos testes de integração, utilizando-se de estratégias orientadas a objetos, o unittests pode criar bancos de dados temporários ou criar um processo de servidor para facilitar a criação de testes, as unidades de teste individual são chamadas de test case, e o conjunto de test cases é chamado de test suite, na test suite as unidades individuais são integradas para executar testes que devem ser feitos juntos.
 
### 4.2 - Ferramenta de teste
 
- unittest
- doctests
- pyunit
 
 
## 5 - Cronograma
 
Tipo de teste      | Duração | data de início | data de término
-------------------|---------|----------------|-----------------
planejar teste     |         | 28/09/2022     | 13/12/2022
projetar teste     |         | 30/09/2022     | 06/09/2022
implementar teste  |         | 07/09/2022    | 13/12/2022
executar teste     |         | 14/09/2022     | 13/12/2022
avaliar teste      |         | 08/11/2022     | 13/12/2022
 
 
 
 


