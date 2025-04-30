# 🚨 Aviso para Técnicos - GLPI

Automação que envia alertas por e-mail para os técnicos responsáveis por chamados no GLPI que estão a **30 minutos de vencer o tempo para solução**.

O script é executado automaticamente a cada 5 minutos (via Agendador de Tarefas do Windows), garantindo que os técnicos sejam notificados a tempo de tomar providências.

## 📁 Estrutura dos Arquivos

- **main.py**  
  Arquivo principal que orquestra a execução das demais classes e funções do sistema.

- **glpi.py**  
  Realiza o acesso à URL do GLPI, extrai e gera a lista de chamados em aberto.

- **alerta.py**  
  Processa os dados dos chamados e gera uma lista separada por técnico com os chamados que vencerão em até 30 minutos.

- **formatacao_email.py**  
  Formata o conteúdo do e-mail em HTML para uma apresentação visual mais clara e profissional.

- **envio_email.py**  
  Responsável por enviar os e-mails de notificação aos técnicos.

- **salvar_chamados.py**  
  Salva os chamados notificados em um arquivo JSON para evitar notificações repetidas. Isso é essencial já que o script é executado a cada 5 minutos.

- **notificados.json**  
  Arquivo JSON gerado pela automação contendo os números dos chamados que já foram notificados, evitando redundância.

## 🛠️ Funcionamento

1. A automação acessa o GLPI e coleta os chamados atribuídos.
2. Filtra os chamados cujo tempo restante para solução é menor ou igual a 30 minutos.
3. Gera um e-mail para cada técnico com seus respectivos chamados urgentes.
4. Envia os e-mails utilizando HTML formatado.
5. Salva os chamados notificados no `notificados.json`.
6. Repetição da execução a cada 5 minutos via Agendador de Tarefas do Windows.


## 📌 Observações

- O controle de chamados já notificados evita que um mesmo chamado seja enviado repetidamente enquanto estiver prestes a vencer.
- O script deve ser mantido rodando constantemente no servidor/local adequado para garantir a eficácia da notificação.

---

Feito com 💻 para melhorar a comunicação e gestão de tempo no suporte técnico via GLPI.
