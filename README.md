## Sistema Bancário em Python
Este projeto é um sistema bancário em Python que permite o cadastro e gerenciamento de bancos, clientes e contas bancárias. Inclui funcionalidades para operações básicas como saques, depósitos e o fechamento de contas.

## Funcionalidades
- **Cadastro de Bancos**: Adicione e gerencie informações sobre diferentes bancos.
- **Cadastro de Clientes**: Registre clientes com nome, sobrenome, idade e CPF.
- **Contas Bancárias**: Crie contas correntes e poupança, com funcionalidades de depósito, saque e aplicação de taxas ou rendimentos mensais.
- **Operações Bancárias**: Realize saques e depósitos em contas, além de permitir o fechamento de contas.
- **Relatórios**: Consulte informações detalhadas sobre bancos, clientes e suas contas.

## Estrutura do Projeto
- `Pessoa`: Classe que representa um cliente com atributos como nome, sobrenome, idade e CPF.
- `Banco`: Classe que representa um banco com nome, CNPJ e número identificador, além de gerenciar contas bancárias.
- `ContaBancaria`: Classe abstrata base para contas, com funcionalidades básicas de saque, depósito e verificação de senha.
- `ContaCorrente`: Subclasse de ContaBancaria com taxas mensais aplicadas ao saldo.
- `ContaPoupanca`: Subclasse de ContaBancaria com rendimento mensal e limite de saques mensais.
- `menu_principal`: Função que gerencia o menu principal do sistema e suas funcionalidades.
