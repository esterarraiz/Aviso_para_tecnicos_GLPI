import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EnvioEmail:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.smtp_server = "smtp.office365.com"
        self.smtp_port = 587

    def enviar_email(self, destinatario, assunto, mensagem, cc=None):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Adiciona os e-mails em cópia, se houver
        if cc:
            msg['Cc'] = ", ".join(cc)
            destinatarios = [destinatario] + cc  # Inclui os CC na lista final de destinatários
        else:
            destinatarios = [destinatario]

        msg.attach(MIMEText(mensagem, 'html', "utf-8"))

        try:
            print("\nEnviando e-mail...\n")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.senha)

            # Enviar o e-mail para todos os destinatários (incluindo CC)
            server.sendmail(self.email, destinatarios, msg.as_string())
            print("E-mail enviado com sucesso!")

        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")

        finally:
            server.quit()
