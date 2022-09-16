import smtplib

conexao = smtplib.SMTP('smtp.gmail.com', 587)

type(conexao)

conexao.ehlo()

conexao.starttls()