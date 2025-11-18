from abc import ABC, abstractmethod

# Interface Abstrata: Pontuavel
class Pontuavel(ABC):

    @abstractmethod
    def calcular_pontuacao(self):
        pass

# Classe Abstrata Pergunta
class Pergunta(Pontuavel, ABC):

    def __init__(self, enunciado, respostaCerta, pontuacaoBase):
        self._enunciado = enunciado # Todos os atributos estão privados (uso do _)
        self._respostaCerta = respostaCerta
        self._pontuacaoBase = pontuacaoBase

# Getter para o atributo enunciado
    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, pergunta):
        if not pergunta or not pergunta.strip():
            raise ValueError("Enunciado inválido, tente novamente")
        self._enunciado = pergunta.strip().capitalize()

    @property
    def respostaCerta(self):
        return self._respostaCerta

    @respostaCerta.setter
    def respostaCerta(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Resposta correta inválida, tente novamente")
        self._respostaCerta = valor.strip().upper()

    @property
    def pontuacaoBase(self):
        return self._pontuacaoBase

    @pontuacaoBase.setter
    def pontuacaoBase(self, valor):
        if valor > 0:
            self._pontuacaoBase = valor
        else:
            raise ValueError("Pontuação base deve ser positiva")

    @abstractmethod
    def verificar_resposta(self, resposta):
        pass

# Pergunta de Múltipla Escolha
class perguntaMultiplaEscolha(Pergunta): # Está herdando da classe abstrata Pergunta

    def __init__(self, enunciado, respostaCerta, alternativas, pontuacaoBase):
        super().__init__(enunciado, respostaCerta, pontuacaoBase)
        self.alternativas = alternativas

    def verificar_resposta(self, resposta):
        if not resposta or not resposta.strip():
            return False
        resposta = resposta.strip().upper()

        if resposta in ['A', 'B', 'C', 'D']:
            return resposta == self.respostaCerta
        else:
            raise ValueError('Digite uma alternativa válida!')

    def calcular_pontuacao(self):
        return self.pontuacaoBase

    def mostrar_alternativas(self):
        return "\n".join(self.alternativas)

# Pergunta de Verdadeiro ou Falso
class perguntaVerdadeiroFalso(Pergunta): # Também herda da classe asbtrata Pergunta 

    def __init__(self, enunciado, respostaVerdadeira, pontuacaoBase):
        respostaCerta = "V" if respostaVerdadeira else "F"
        super().__init__(enunciado, respostaCerta, pontuacaoBase)
        self.respostaVerdadeira = respostaVerdadeira

    def verificar_resposta(self, resposta):
        if not resposta or not resposta.strip():
            return False
        resposta = resposta.strip().upper()

        if resposta in ["V", "VERDADEIRO", "TRUE"]:
            return self.respostaVerdadeira
        if resposta in ["F", "FALSO", "FALSE"]:
            return not self.respostaVerdadeira

        return False

    def calcular_pontuacao(self):
        return max(1, self.pontuacaoBase // 2)

# Classe jogador (está encapsulada)
class jogador:

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Nome inválido")
        self._nome = valor.strip().capitalize()

    @property
    def pontuacao(self):
        return self._pontuacao

    @pontuacao.setter
    def pontuacao(self, valor):
        if valor < 0:
            raise ValueError("Pontuação não pode ser negativa")
        self._pontuacao = valor

    def adicionar_pontos(self, pontos):
        if pontos < 0:
            raise ValueError("Pontos inválidos")
        self._pontuacao += pontos

# Sistema de Logs
class sistemaLogs:

    @staticmethod
    def registrar_evento(mensagem, codigo=None, contexto=None):
        linha = f"{mensagem}"

        if codigo is not None:
            linha += f" (COD={codigo})"
        if contexto is not None:
            linha += f" [{contexto}]"

        print(linha)

# Classe Quiz 
class Quiz:

    totalQuizzesJogos = 0

    def __init__(self, perguntas, jogador):
        self.perguntas = perguntas
        self.jogador = jogador
        Quiz.totalQuizzesJogos += 1

    
    # | Menu do quizz |
 
    @staticmethod
    def menu():
        perguntas = Quiz.montar_perguntas()
        jogadorAtual = None

        while True:
            print("\n=========== QUIZZ DE POO ===========")
            print("1) Iniciar jogo")
            print("2) Criar novo jogador")
            print("3) Ver total de quizzes jogados")
            print("4) Sair")
            print("=" * 36)
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                if jogadorAtual is None:
                    jogadorAtual = jogador(input("Qual o seu nome, Jogador? "))
                quiz = Quiz(perguntas, jogadorAtual)
                quiz.iniciar()

            elif opcao == "2":
                jogadorAtual = jogador(input("Qual o nome do novo jogador? "))
                print("Jogador novo adicionado!")

            elif opcao == "3":
                print("Total de quizzes jogados:", Quiz.totalQuizzesJogos)

            elif opcao == "4":
                print("Finalizando, volte sempre...")
                break

            else:
                print("Opção inválida, tente novamente!")

    # Início do jogo
    def iniciar(self):
        sistemaLogs.registrar_evento("Iniciando o melhor quiz do Brasil...", contexto="RUN")

        for i, pergunta in enumerate(self.perguntas, start=1):
            print("\n(Digite MENU para voltar ao menu principal)")
            print(f"\nPergunta {i}:")
            print(pergunta.enunciado)

            if isinstance(pergunta, perguntaMultiplaEscolha):
                print(pergunta.mostrar_alternativas())

            resposta = input("Digite a sua resposta: ").strip()

            if resposta.upper() == "MENU":
                print("\nVoltando ao menu...")
                return

            correto = pergunta.verificar_resposta(resposta)
            pontos = pergunta.calcular_pontuacao() if correto else 0
            self.jogador.adicionar_pontos(pontos)

            sistemaLogs.registrar_evento(
                f"Pergunta {i} respondida | Acerto: {correto} | Pontos: +{pontos}",
                codigo=100
            )

        self.finalizar()

    # Finalização do jogo
    def finalizar(self):
        print("\n=========== RESULTADO ===========")
        print("Jogador:", self.jogador.nome)
        print("Pontuação final:", self.jogador.pontuacao)

        print("=================================")

    # PERGUNTAS DE EXEMPLO
    @staticmethod
    def montar_perguntas():
        pergunta1 = perguntaMultiplaEscolha(
            "Qual o nome do metódo que é usado para herdar atributos e métodos de outra classe?",
            "C",
            ["A) extends()", "B) herdar()", "C) super()", "D) pai()"],
            50
        )

        pergunta2 = perguntaVerdadeiroFalso(
            "Em Python, um método privado é aquele que começa com um único underline, como _metodo().",
            False,
            40
        )

        pergunta3 = perguntaMultiplaEscolha(
            "O que é uma classe abstrata?",
            "B",
            ["A) Uma classe que só tem atributos privados", "B) Uma classe que não pode ser instanciada", "C) Uma classe filha de outra classe", "D) Uma classe que não herda métodos"],
            60
        )

        pergunta4 = perguntaVerdadeiroFalso(
            "Em Python, o polimorfismo permite que métodos com o mesmo nome, mas em classes diferentes, se comportem de maneira diferente.",
            True,
            40
        )

        return [pergunta1, pergunta2, pergunta3, pergunta4]

# MAIN
if __name__ == "__main__":
    Quiz.menu()