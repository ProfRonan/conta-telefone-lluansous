"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    NumLig= int(input('Digite o número de ligações:'))
    Valor= 200
    if NumLig <=100:
      Valor+=0
    elif 150>= NumLig > 100:
      Valor +=(NumLig-100)*0.60  
    elif 200 >= NumLig > 150:
      Valor+=(NumLig - 150) *0.5 + 30
    else:
      Valor+= (NumLig - 200) * 0.4 +55
    print(f'O valor devido é R$ {Valor:.2f}.')    

    


if __name__ == '__main__':
    main()
