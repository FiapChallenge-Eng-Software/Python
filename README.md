# CP_Python
Checkpoint 2 - Python 

# VinheriaAgnello - Controle de Compras e Estoque

## Descrição
Este programa tem como objetivo auxiliar a Vinheria Agnello no controle de suas compras de suprimentos e no gerenciamento de seu estoque. Com ele, será possível cadastrar as compras realizadas, controlar as entradas e saídas de produtos do estoque, além de verificar o estoque atual de cada item.

## Funcionalidades
O programa conta com dois menus principais: Compras e Estoque.

### Compras
No menu de Compras, é possível realizar as seguintes operações:
- Cadastrar nova compra: permite adicionar uma nova compra ao sistema, informando a descrição do item, a quantidade adquirida e o valor unitário. O programa irá calcular o valor total da compra e atualizar o estoque.
- Mostrar todas as compras: exibe um relatório com todas as compras realizadas, incluindo a descrição do item, a quantidade, o valor unitário, o valor total e a data da compra.

### Estoque
No menu de Estoque, é possível realizar as seguintes operações:
- Registrar entrada de produto: permite adicionar uma nova entrada de produto no estoque, informando a descrição do item e a quantidade recebida.
- Registrar saída de produto: permite registrar a venda de um produto, informando a descrição do item e a quantidade vendida. O programa irá calcular o valor total da venda e atualizar o estoque.
- Mostrar estoque atual: exibe um relatório com o estoque atual de todos os produtos, incluindo a descrição do item e a quantidade disponível.

## Requisitos
Para o programa funcionar corretamente, é necessário ter instalado em seu computador uma versão recente do Python (recomenda-se a versão 3.6 ou superior). Além disso, é preciso baixar o arquivo "VinheriaAgnello.py" e executá-lo em um terminal.

## Como executar
Para executar o programa, basta abrir um terminal e navegar até a pasta onde o arquivo "VinheriaAgnello.py" foi salvo. Em seguida, digite o comando "python VinheriaAgnello.py" e pressione Enter. O programa irá rodar e exibir o menu principal.

## Observações
- Todos os blocos do código estão comentados para facilitar a compreensão e a manutenção do programa.
- O programa utiliza estruturas condicionais, laços de repetição, listas e estruturas Match-Case para realizar as operações solicitadas.
- O CNPJ dos fornecedores não é armazenado no sistema, pois não é necessário para o controle de compras e estoque.