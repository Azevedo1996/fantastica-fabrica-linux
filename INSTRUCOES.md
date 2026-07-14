# Instruções — A Fantástica Fábrica do Linux

## Visão geral

Este projeto é um jogo web em Django inspirado no treinamento "A Fantástica Fábrica do Linux".

A ideia é usar a metáfora da fábrica para ensinar comandos Linux de forma simples, mas sem tratar comandos como mágica. Cada desafio apresenta uma situação e pede o comando ou conceito correto.

## Fases implementadas

### Fase 1 — A Visita à Fábrica

Conteúdo:

1. Linux
2. Hardware
3. Kernel
4. Terminal
5. pwd
6. ls
7. ls -l
8. ls -la
9. cd
10. cd ..

## Sistema de pontuação

Cada missão possui o campo `points`.

Por padrão:

```text
10 pontos por missão
```

Ao acertar uma resposta:

- o jogador recebe os pontos da missão;
- a recompensa da missão é adicionada à sessão;
- a explicação do comando é exibida;
- o jogador avança para a próxima missão.

## Recompensas

Cada missão tem uma recompensa didática, por exemplo:

```text
Mapa de Localização da Sala
Interruptor do Comando ls
Passe dos Corredores da Fábrica
```

As recompensas aparecem no feedback e no relatório final da fase.

## Carregar perguntas

Após rodar as migrações, execute:

```bash
python manage.py seed_missions
```

## Editar perguntas

Use o Django Admin:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Depois acesse:

```text
http://127.0.0.1:8000/admin/
```

## Próximas fases sugeridas

- Fase 2 — A Mão na Massa: implementada com `mkdir`, `touch`, `echo`, `cat`, `cp`, `mv`, `cp -r`, `rm`
- Fase 3 — As Salas da Fábrica: `/`, `/home`, `/etc`, `/var`, `/tmp`
- Fase 4 — Os Donos da Receita: usuários, grupos e root
- Fase 5 — Os Sabores Linux: Ubuntu, Debian, RHEL, SUSE
- Fase 6 — O Bilhete Dourado Final: revisão geral


### Fase 2 — A Mão na Massa

Conteúdo:

1. mkdir
2. touch
3. echo
4. cat
5. cp
6. mv para renomear
7. mv para mover
8. cp -r
9. rm
10. ls para conferência

Objetivo: fazer o aluno criar, ler, copiar, mover, renomear, duplicar e remover arquivos e diretórios usando comandos reais do Linux.


### Fase 3 — Os Sabores da Fábrica

Conteúdo:

1. Distribuição Linux
2. Ubuntu
3. Debian
4. RHEL
5. SUSE
6. apt
7. dnf
8. apt update
9. apt install
10. Revisão de distribuições Linux

Objetivo: fazer o aluno entender que diferentes distribuições são variações do Linux, cada uma com escolhas próprias de pacotes, ferramentas, suporte e público-alvo.


### Fase 4 — O Elevador de Vidro

Conteúdo:

1. Linux
2. Kernel
3. Terminal
4. pwd
5. ls
6. cd
7. mkdir
8. touch
9. distribuições Linux
10. continuar aprendendo Linux

Objetivo: fechar o meetup de 2 horas com uma revisão geral e uma mensagem final de incentivo para que os participantes continuem praticando Linux.

Ao responder a última pergunta, o jogo exibe uma tela especial de parabéns com convite para continuar aprendendo Linux.


## Convite final para o Detetive Linux

A tela final da Fase 4 agora convida os participantes a continuarem aprendendo no jogo **Detetive Linux — O Mistério da Fábrica**.

Mensagem adicionada ao encerramento:

```text
Se você gostou da visita pela fábrica, continue a jornada jogando Detetive Linux — O Mistério da Fábrica.
Nele, você vai investigar problemas reais da infraestrutura, praticar comandos e aprender a pensar como uma pessoa de suporte ou infraestrutura Linux.
```
