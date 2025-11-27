# sistema_clinica.py
# Sistema de Gestão para Clínica Vida+
# Versão Corrigida e Testada

class SistemaClinica:
    def __init__(self):
        self.pacientes = []
    
    def cadastrar_paciente(self):
        print("\n=== CADASTRO DE PACIENTE ===")
        try:
            nome = input("Nome do paciente: ").strip()
            if not nome:
                print("Erro: Nome não pode estar vazio.")
                return
            
            idade = int(input("Idade: "))
            if idade < 0 or idade > 150:
                print("Erro: Idade deve estar entre 0 e 150 anos.")
                return
            
            telefone = input("Telefone: ").strip()
            if not telefone:
                print("Erro: Telefone não pode estar vazio.")
                return
            
            paciente = {
                "nome": nome,
                "idade": idade,
                "telefone": telefone
            }
            
            self.pacientes.append(paciente)
            print("Paciente cadastrado com sucesso!")
            
        except ValueError:
            print("Erro: Idade deve ser um número inteiro.")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    
    def ver_estatisticas(self):
        if not self.pacientes:
            print("\nNenhum paciente cadastrado ainda.")
            return
        
        print("\n=== ESTATÍSTICAS DOS PACIENTES ===")
        total_pacientes = len(self.pacientes)
        soma_idades = sum(paciente["idade"] for paciente in self.pacientes)
        idade_media = soma_idades / total_pacientes
        
        paciente_mais_novo = min(self.pacientes, key=lambda x: x["idade"])
        paciente_mais_velho = max(self.pacientes, key=lambda x: x["idade"])
        
        print(f"Total de pacientes cadastrados: {total_pacientes}")
        print(f"Idade média dos pacientes: {idade_media:.1f} anos")
        print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
        print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")
    
    def buscar_paciente(self):
        if not self.pacientes:
            print("\nNenhum paciente cadastrado ainda.")
            return
        
        print("\n=== BUSCAR PACIENTE ===")
        nome_busca = input("Digite o nome do paciente: ").strip().lower()
        
        encontrados = []
        for paciente in self.pacientes:
            if nome_busca in paciente["nome"].lower():
                encontrados.append(paciente)
        
        if not encontrados:
            print("Nenhum paciente encontrado com esse nome.")
        else:
            print(f"\n{len(encontrados)} paciente(s) encontrado(s):")
            for i, paciente in enumerate(encontrados, 1):
                print(f"{i}. Nome: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")
    
    def listar_pacientes(self):
        if not self.pacientes:
            print("\nNenhum paciente cadastrado ainda.")
            return
        
        print("\n=== TODOS OS PACIENTES CADASTRADOS ===")
        for i, paciente in enumerate(self.pacientes, 1):
            print(f"{i}. Nome: {paciente['nome']} | Idade: {paciente['idade']} | Telefone: {paciente['telefone']}")
    
    def mostrar_questoes_teoricas(self):
        print("\n" + "="*50)
        print("RESPOSTAS DAS QUESTÕES TEÓRICAS")
        print("="*50)
        
        print("\n1. EXPRESSÕES LÓGICAS:")
        print("   Consulta Normal: (A and B and C) or (B and C and D)")
        print("   Emergência: C and (B or D)")
        
        print("\n4. ANÁLISE:")
        print("   Consulta Normal: 6 situações diferentes")
        print("   Emergência: 8 situações diferentes")
        
        print("\n5. SITUAÇÃO PRÁTICA:")
        print("   Condições: A=F, B=V, C=V, D=F")
        consulta_normal = (False and True and True) or (True and True and False)
        emergencia = True and (True or False)
        print(f"   Consulta Normal: {'SIM' if consulta_normal else 'NÃO'}")
        print(f"   Emergência: {'SIM' if emergencia else 'NÃO'}")

    def simular_fila_atendimento(self):
        print("\n" + "="*50)
        print("FILA DE ATENDIMENTO")
        print("="*50)
        
        fila = []
        
        # Inserir 3 pacientes na fila
        print("\nInserindo 3 pacientes na fila:")
        for i in range(3):
            nome = input(f"Nome do paciente {i+1}: ")
            cpf = input(f"CPF do paciente {i+1}: ")
            fila.append({"nome": nome, "cpf": cpf})
            print(f"Paciente {nome} adicionado à fila.")
        
        # Remover o primeiro paciente para atendimento
        if fila:
            primeiro_paciente = fila.pop(0)
            print(f"\nAtendendo: {primeiro_paciente['nome']} (CPF: {primeiro_paciente['cpf']})")
        
        # Mostrar quem ainda está na fila
        print("\nPacientes restantes na fila:")
        if fila:
            for i, paciente in enumerate(fila, 1):
                print(f"{i}. {paciente['nome']} (CPF: {paciente['cpf']})")
        else:
            print("Nenhum paciente na fila.")

    def executar(self):
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        
        while True:
            print("\nMenu Principal:")
            print("1. Cadastrar paciente")
            print("2. Ver estatísticas")
            print("3. Buscar paciente")
            print("4. Listar todos os pacientes")
            print("5. Questões Teóricas")
            print("6. Simular Fila de Atendimento")
            print("7. Sair")
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == "1":
                    self.cadastrar_paciente()
                elif opcao == "2":
                    self.ver_estatisticas()
                elif opcao == "3":
                    self.buscar_paciente()
                elif opcao == "4":
                    self.listar_pacientes()
                elif opcao == "5":
                    self.mostrar_questoes_teoricas()
                elif opcao == "6":
                    self.simular_fila_atendimento()
                elif opcao == "7":
                    print("Obrigado por usar o Sistema Clínica Vida+!")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção de 1 a 7.")
                    
            except KeyboardInterrupt:
                print("\nPrograma interrompido pelo usuário.")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")

# Executar o programa
if __name__ == "__main__":
    sistema = SistemaClinica()
    sistema.executar()