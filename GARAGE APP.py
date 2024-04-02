import os


class Carro:

    carros = []
    
    def __init__(self, empresa=None, ano=None, modelo=None):
        self.empresa = empresa.title() if empresa is not None else None
        self.ano = ano
        self.modelo = modelo.title() if modelo is not None else None
        if all([self.empresa, self.ano, self.modelo]):
            Carro.carros.append(self)

    def cadastrar_ano(self):
        while True:
            ano = input("Digite o ano do veículo (no formato de 4 dígitos xxxx): ")
            if len(ano) == 4 and ano.isdigit():
                return int(ano)
            else:
                print("Ano inválido! O ano deve conter exatamente 4 dígitos.")

    @classmethod
    def listar_carros(cls):
        os.system("cls")
        print("LISTA DE CARROS:\n")
        for i, veiculo in enumerate(cls.carros, start=1):
            empresa = veiculo.empresa if veiculo.empresa is not None else ""
            ano = veiculo.ano if veiculo.ano is not None else ""
            modelo = veiculo.modelo if veiculo.modelo is not None else ""
            print(f"{i}. {empresa.ljust(18)} | {str(ano).ljust(18)} | {modelo.ljust(18)}")
    

    @classmethod
    def adicionar_carros(cls):
        empresa = input("Digite o nome da empresa do veículo: \n")
        ano = cls().cadastrar_ano()
        modelo = input("Digite o nome do veículo: \n")
        novo_carro = cls(empresa, ano, modelo)
        os.system("cls")
        print("Carro adicionado com sucesso!")

    @classmethod
    def alterar_atributos(cls):
        os.system("cls")
        cls.listar_carros()
        index = input("Digite o número do carro que deseja alterar: ")
        try:
            index = int(index)
            if 1 <= index <= len(cls.carros):
                carro = cls.carros[index - 1]
                atributo = input("Digite o atributo que deseja alterar (empresa, ano, modelo): ").lower()
                if atributo == "ano":
                    novo_ano = cls().cadastrar_ano()
                    setattr(carro, atributo, novo_ano)
                    print("Ano alterado com sucesso!")
                elif atributo in ["empresa", "modelo"]:
                    novo_valor = input(f"Digite o novo valor para {atributo}: ")
                    setattr(carro, atributo, novo_valor.title() if novo_valor else None)
                    print("Atributo alterado com sucesso!")
                else:
                    print("Atributo inválido!")
            else:
                print("Índice fora dos limites!")
        except ValueError:
            print("Índice inválido! Digite um número válido.")


def inicializar_programa():
    os.system("cls")
    print("""    
    ───────────────────────────────────────────────────────────────────────────────────────────────
    ─██████████████─██████████████─████████████████───██████████████─██████████████─██████████████─
    ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██░░██████████─██░░██████░░██─██░░████████░░██───██░░██████░░██─██░░██████████─██░░██████████─
    ─██░░██─────────██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██─────────██░░██─────────
    ─██░░██─────────██░░██████░░██─██░░████████░░██───██░░██████░░██─██░░██─────────██░░██████████─
    ─██░░██──██████─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─
    ─██░░██──██░░██─██░░██████░░██─██░░██████░░████───██░░██████░░██─██░░██──██░░██─██░░██████████─
    ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─██░░██─────────
    ─██░░██████░░██─██░░██──██░░██─██░░██──██░░██████─██░░██──██░░██─██░░██████░░██─██░░██████████─
    ─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██████████████─██████──██████─██████──██████████─██████──██████─██████████████─██████████████─
    ───────────────────────────────────────────────────────────────────────────────────────────────╝ """)

    print("\n")
    opcoes_menu()

def opcoes_menu():
    print(f"{"1 - ADICIONE NOVOS CARROS"} \n".ljust(25)) 
    print(f"{"2 - VEJA SUA LISTA DE CARROS"} \n".ljust(25))
    print(f"{"3 - ALTERAR ATRIBUTOS DE UM CARRO"} \n".ljust(25))
    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1 :
        Carro.adicionar_carros()
        input("Digite alguma tecla para retornar ao menu!")
        inicializar_programa()
    elif opcao_escolhida == 2:
        Carro.listar_carros()
        input("Digite alguma tecla para retornar ao menu!")
        inicializar_programa()
    elif opcao_escolhida == 3:
        Carro.alterar_atributos()
        input("Pressione Enter para retornar ao menu principal...")
        inicializar_programa()
    else:
        opcao_invalida()    
        
def opcao_invalida():
    print("opção invalida!\n")
    voltar_ao_menu()
    
def voltar_ao_menu():
    input("digite uma tecla para retornar ao menu principal: ")
    inicializar_programa()

supra = Carro("toyota", 2011, "supra")

inicializar_programa()
