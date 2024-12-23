# Compressão de Arquivos com Huffman

## Introdução

Este programa implementa a compressão e descompressão de arquivos utilizando o algoritmo de Huffman, sem o uso de bibliotecas prontas do Python. O objetivo é aplicar a técnica de codificação de Huffman para reduzir o tamanho de um arquivo de texto e permitir sua posterior descompressão, restaurando o conteúdo original. O programa lê um arquivo de texto, cria a árvore de Huffman, gera os códigos para compressão, salva o arquivo compactado, e então permite a descompressão para recuperar o texto original.

## Requisitos

- **Python**: Versão 3.13.0 ou superior.
- **Sistema operacional**: Windows 10 (recomendado para testes).
- **Editor de código**: Visual Studio Code.
- **Bibliotecas**: Apenas a biblioteca padrão do Python (sem dependências externas).

## Instruções de Execução

1. Salve todos os arquivos do exercício na mesma pasta.
2. Edite o arquivo `teste.txt` e escreva uma frase ou utilize a frase já salva nele.
3. Execute o arquivo Python `EP2.py`:
    - Abra o arquivo no Visual Studio Code e rode-o com o comando `F5`.
    - **Ou** abra um prompt de comando (Cmd), navegue até a pasta dos arquivos e execute o comando: `python EP2.py`.
4. O programa solicitará o nome do arquivo `.txt` para compactação. Use o arquivo `teste.txt` ou crie seu próprio arquivo `.txt`.
5. O programa exibirá as seguintes informações:
    - Frequências dos caracteres.
    - Árvore de Huffman.
    - Texto compactado.
    - Texto descompactado.

## Fluxo do Programa

1. O programa solicita o nome de um arquivo `.txt`.
2. O conteúdo do arquivo é lido e as frequências dos caracteres são calculadas.
3. A árvore de Huffman é construída a partir das frequências.
4. A árvore de Huffman é exibida no formato pré-ordem.
5. O código de Huffman é gerado para cada caractere.
6. O texto é compactado utilizando os códigos gerados.
7. O texto compactado é salvo em um arquivo com o sufixo `_compactado`.
8. O texto compactado é lido e descompactado, e o texto original é exibido.

## Exemplos de Testes

### 1. Carregar e Compactar Arquivo

- **Comando**: Insira o nome do arquivo `.txt` (exemplo: `teste.txt`).
- **Saída esperada**:
  - Exibição das frequências dos caracteres.
  - Exibição da árvore de Huffman.
  - Texto compactado.
  - Nome do arquivo onde o texto compactado foi salvo.

### 2. Descompactar Arquivo

- **Comando**: O arquivo compactado será lido e o texto será descompactado corretamente.
- **Saída esperada**:
  - O conteúdo original do arquivo será exibido após a descompressão.

## Considerações Finais

Este programa foi desenvolvido como parte de um exercício do Mestrado Profissional em Computação Aplicada, com o objetivo de aplicar o algoritmo de Huffman para compressão e descompressão de arquivos. A implementação foi realizada sem o uso de bibliotecas prontas de Python para manipulação de filas de prioridade e árvores.

Caso haja dúvidas ou sugestões, entre em contato.
