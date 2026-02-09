# Verificacao de Notas Fiscais

Este projeto se trata de um código criado para uma empresa com o intuito de verificar as notas fiscais em aberto no ERP sem necessidade de abrir o sistema, com todos os detalhes necessários, através do Prompt de Comando.

O código é construído puxando os dados para acesso ao banco de dados da empresa, então, através do SQL, é realizado uma pesquisa de todas as informações necessárias das notas fiscais (Nome do Cliente, CNPJ, Filial, Data da NF).

Com essas informações, seguimos utilizando Python para a divisão dos dados por Empresa e Filial, para melhor visualização, e o sistema informa quantas notas em aberto há por empresa.

Após isso, no Prompt de Comando serão mostradas quais filiais possuem no sistema, e quantas notas em aberto cada uma delas possui. Então você poderá escolher uma das filiais para que apareçam todas as notas em aberto com mais detalhes.
