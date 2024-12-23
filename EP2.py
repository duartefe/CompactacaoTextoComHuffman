# Classe para nós da árvore de Huffman
class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

# Classe para fila de prioridade manual
class FilaDePrioridade:
    def __init__(self):
        self.elementos = []

    def obter_frequencia(self, no):
        return no.frequencia

    def inserir(self, no):
        self.elementos.append(no)
        self.elementos.sort(key=self.obter_frequencia)

    def remover_menor(self):
        return self.elementos.pop(0) if self.elementos else None

    def __len__(self):
        return len(self.elementos)

# Funções auxiliares
def contar_frequencias(texto):
    frequencias = {}
    for caractere in texto:
        frequencias[caractere] = frequencias.get(caractere, 0) + 1
    return frequencias

def exibir_frequencias(frequencias):
    print("Frequências dos caracteres:")
    print(", ".join([f"'{caractere}': {frequencia}" for caractere, frequencia in frequencias.items()]))

def encontrar_caractere(no):
    while no.esquerda is not None:
        no = no.esquerda
    return no.caractere

def construir_arvore(frequencias):
    fila = FilaDePrioridade()
    for caractere, frequencia in frequencias.items():
        fila.inserir(No(caractere, frequencia))
    while len(fila) > 1:
        no1 = fila.remover_menor()
        no2 = fila.remover_menor()
        novo_no = No(None, no1.frequencia + no2.frequencia)
        novo_no.esquerda = no1
        novo_no.direita = no2
        fila.inserir(novo_no)
    return fila.remover_menor()

def exibir_arvore_preordem(raiz):
    resultado = []
    def preordem_aux(no):
        if no is not None:
            if no.caractere is not None:
                resultado.append(f"'{no.caractere}': {no.frequencia}")
            else:
                caractere_esquerdo = encontrar_caractere(no.esquerda)
                resultado.append(f"'{caractere_esquerdo}': {no.frequencia}")
            preordem_aux(no.esquerda)
            preordem_aux(no.direita)
    preordem_aux(raiz)
    print(", ".join(resultado))

def gerar_codigos(raiz):
    codigos = {}
    def gerar_codigos_aux(no, codigo_atual):
        if no is not None:
            if no.caractere is not None:
                codigos[no.caractere] = codigo_atual
            gerar_codigos_aux(no.esquerda, codigo_atual + "0")
            gerar_codigos_aux(no.direita, codigo_atual + "1")
    gerar_codigos_aux(raiz, "")
    return codigos

def codificar_texto(texto, codigos):
    return "".join([codigos[caractere] for caractere in texto])

def salvar_arquivo_compactado(nome_arquivo, texto_compactado):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto_compactado)

def ler_arquivo_compactado(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

def decodificar_texto(texto_compactado, raiz):
    texto_decodificado = []
    no_atual = raiz
    for bit in texto_compactado:
        no_atual = no_atual.esquerda if bit == '0' else no_atual.direita
        if no_atual.caractere is not None:
            texto_decodificado.append(no_atual.caractere)
            no_atual = raiz
    return "".join(texto_decodificado)

# Programa principal
def principal():
    nome_arquivo = input("Digite o nome do arquivo com a extensão (.txt): ")
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        if not texto.strip():
            print("Erro: O arquivo está vazio. Por favor, forneça um arquivo válido.")
            return
        frequencias = contar_frequencias(texto)
        exibir_frequencias(frequencias)
        raiz = construir_arvore(frequencias)
        print("\nÁrvore de Huffman (Pré-Ordem):")
        exibir_arvore_preordem(raiz)
        codigos = gerar_codigos(raiz)
        texto_compactado = codificar_texto(texto, codigos)
        print("\nTexto Compactado:")
        print(texto_compactado)
        nome_arquivo_compactado = nome_arquivo.replace(".txt", "_compactado.txt")
        salvar_arquivo_compactado(nome_arquivo_compactado, texto_compactado)
        print(f"\nTexto compactado salvo em: {nome_arquivo_compactado}")
        texto_compactado_lido = ler_arquivo_compactado(nome_arquivo_compactado)
        texto_decodificado = decodificar_texto(texto_compactado_lido, raiz)
        print("\nTexto Decodificado:")
        print(texto_decodificado)
        if texto == texto_decodificado:
            print("\nA decodificação foi bem-sucedida e corresponde ao texto original!")
        else:
            print("\nA decodificação não corresponde ao texto original. Verifique o código.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Verifique o caminho e tente novamente.")

if __name__ == "__main__":
    principal()
