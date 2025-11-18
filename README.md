# AV2-POO
Este é o meu projeto de um quiz interativo no console feito em Python, valendo como objeto de avaliação para a AV2 da matéria Programação Orientada à Objeto (POO), ministrada pelo professor/coordenador Amaury Nogueira.

# 🧠 Quiz Interativo de POO em Python

o quiz interativo utiliza diversos conceitos fundamentais da orientação a objetos como **abstração**, **herança**, **encapsulamento**, **polimorfismo**, além de boas práticas como interface com `ABC` e logs.

---

## 🚀 Como Executar o Projeto

### 📌 Requisitos:

- Python 3.10 ou superior instalado
- Terminal ou prompt de comando

- # 🧩 Conceitos de POO Aplicados

O projeto demonstra os seguintes princípios:

## 🔷 1. Interface

Pontuavel é uma interface (implementada via ABC) que define o método abstrato calcular_pontuacao.

Todas as perguntas (subclasses de Pergunta) são pontuáveis porque implementam calcular_pontuacao().

## 🔷 2. Abstração

Utilizada com a interface Pontuavel e a classe abstrata Pergunta, ambas herdando de ABC e usando métodos abstratos.

## 🔷 3. Herança

Classes perguntaMultiplaEscolha e perguntaVerdadeiroFalso herdam da classe abstrata Pergunta, aproveitando atributos e métodos comuns.

## 🔷 4. Sobrescrita (Override)

Sobrescrita acontece quando as subclasses redefinem métodos abstratos da superclasse:

verificar_resposta() é implementado de formas diferentes em perguntaMultiplaEscolha e perguntaVerdadeiroFalso.

calcular_pontuacao() também é implementado de forma específica por tipo de pergunta.

## 🔷 5. Construtores com super()

Subclasses chamam o construtor da superclasse com super().__init__(...) para garantir que os atributos da classe pai sejam inicializados corretamente:

## 🔷 6. Encapsulamento

Atributos iniciados com _ são tratados como privados

Uso de getters e setters para validação dos dados:

## 🔷 7. Polimorfismo

Método verificar_resposta() é implementado de maneira distinta em cada tipo de pergunta.

## 🔷 8. Composição

A classe Quiz contém uma lista de objetos Pergunta, além de um objeto jogador.

## 🔷 9. Métodos Estáticos

Quiz.menu() e sistemaLogs.registrar_evento() demonstram be uso de @staticmethod.

## 🧭 Coesão e Baixo Acoplamento

Coesão e baixo acoplamento são práticas de design que tornam o sistema mais compreensível, testável e manutenível. Veja como foram aplicadas:

### ✅ Coesão (cada módulo faz uma coisa bem definida)

Pergunta e suas subclasses: responsabilidade única — representar e validar uma pergunta e verificar respostas.

jogador: responsabilidade de representar um jogador e gerenciar sua pontuação.

sistemaLogs: responsabilidade única de registrar eventos (seja print simples ou log futuro).

Quiz: orquestra o fluxo do jogo (menu, iteração pelas perguntas, pontuação).

Cada classe possui alta coesão — funções relacionadas estão agrupadas na mesma classe.

### ✅ Baixo Acoplamento (dependências reduzidas e bem definidas)

Interfaces e abstrações (Pergunta, Pontuavel) isolam detalhes de implementação — Quiz depende apenas da interface pública das perguntas (métodos verificar_resposta e calcular_pontuacao) e não de implementações concretas.

Uso de getters/setters para acessar atributos permite mudar implementação interna sem afetar código externo.

sistemaLogs é estático e desacoplado da lógica do quiz — trocar a implementação de logs (por exemplo, para escrever em arquivo) não exige mudança em Quiz ou Pergunta.

Baixa dependência direta: Quiz não manipula internamente como uma pergunta valida sua resposta — isso evita acoplamento excessivo entre classes.

Esses princípios facilitam:

adicionar novos tipos de pergunta sem alterar Quiz,

trocar a estratégia de logs sem reescrever lógica de jogo,

criar testes unitários para cada componente isolado.

# 🎮 Funcionalidades do Quiz

## Menu interativo:

Criar novo jogador

Iniciar quiz

Consultar número total de jogos

Sair

## Tipos de perguntas:

Múltipla escolha (A, B, C, D)

Verdadeiro ou Falso (V/F)

## Pontuação:

Base por pergunta

Redução pela metade em perguntas VF

## Registro de eventos:

Cada pergunta respondida gera um log com status e pontuação
