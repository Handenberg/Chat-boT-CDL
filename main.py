import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Para a emissão do certificado digital E-CPF (Pessoa Física) Tipo : A1, será necessário a apresentação de sua documentação pessoal: RG, CNH, Carteira profissional ou Carteira de conselho profissional{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome},  Para a emissão do certificado digital E-CNPJ (Pessoa Jurídica) Tipo : A1, será necessário a apresentação de sua documentação pessoal: RG, CNH, Carteira profissional ou Carteira de conselho profissional + Documentação original da empresa: Contrato social, Requerimento do empresário, comprovante MEI.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, O certificado digital para pessoa física do tipo A1, custa R$ 130,00 que pode ser pago em espécie, PIX, Cartões de crédito ou débito e boleto bancário (no boleto, o certificado só será liberado mediante a compensação do boleto .{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação, porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para criar aplicações em python e estar pronto para o mercado, recomendo o cursodepython.net.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a Certificação Digital - CDL Campina Grande')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'Deseja adquirir um certificado digital? Nos informe qual tipo de certificado digital deseja:{os.linesep}'
            f'Digite a opção correspondente:{os.linesep}'
            f'[1] - E-CPF?{os.linesep}'
            f'[2] - E-CNPJ?{os.linesep}'
            f'[3] - Valor do certificado E-CPF A1 e formas de pagamento?{os.linesep}'
            f'[4] - Valor do certificado E-CNPJ A1 e formas de pagamento?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()


