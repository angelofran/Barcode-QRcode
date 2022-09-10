import barcode
from barcode.writer import ImageWriter, SVGWriter
import os 
from io import BytesIO
import qrcode

print("BarQ, o seu leitor.")
print("O que você quer usar? [Barcode/QRcode] ")
escolha = str(input("O que você escolhe? [B/Q] ")).upper().strip()[0]


if escolha in "B":
    os.system('cls')
    print("""1 - Criar barcode""")
    opc1 = int(input("Qual você escolhe? "))

    if opc1 == 1:
        pergunta = str(input("Em que formato você quer salvar o arquivo? [SVG/PNG] ")).upper()

        if pergunta in 'PNG':
            try:
                valor = str(input("Conteúdo do código de barras: "))
                nome_arq = str(input("Nome do arquivo: "))
                code_bar = barcode.EAN13(valor, writer=ImageWriter())
                code_bar.save(nome_arq)
                print('\033[34mArquivo criado com sucesso!\033[m')
            except barcode.errors.NumberOfDigitsError:
                print('1033[1;31mDigite apenas 12 digitos')

        elif pergunta in 'SVG':
            valor1 = str(input("Conteúdo do código de barras: "))
            nome_arq1 = str(input("Nome do arquivo: "))
            code_bar1 = barcode.EAN13(valor1, writer=SVGWriter())
            code_bar1.save(nome_arq1)
            print('\033[34mArquivo criado com sucesso!\033[m')

        else:
            print("\033[1;31mPor favor, insira valores  válidos, reinicie o programa para tentar novamente.\033[m") 
    else:
        print("\033[1;31mPor favor, insira valores  válidos, reinicie o programa para tentar novamente.\033[m") 



elif escolha in "Q":
    os.system('cls')
    print("""1 - Criar qrcode""")
    opc2 = int(input("Qual você escolhe? "))

    if opc2 == 1:
        nome_arq = str(input("Nome do arquivo: "))
        valor = str(input("Conteúdo do qrcode: "))
        meu_qrcode = qrcode.make(valor)
        meu_qrcode.save(f"{nome_arq}.png")   
        print("\033[7;34mArquivo gerado com sucesso!\033[m")  
    else:
        print("\033[1;31mPor favor, insira valores  válidos, reinicie o programa para tentar novamente.\033[m") 

else:
    print("\033[1;31mPor favor, insira valores  válidos, reinicie o programa para tentar novamente.\033[m")

