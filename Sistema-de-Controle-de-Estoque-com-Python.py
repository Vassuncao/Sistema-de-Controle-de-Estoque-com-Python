# =========================
# CLASSE PRODUTO
# =========================
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade


# =========================
# CLASSE ESTOQUE
# =========================
class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.produtos:
            print("❌ Produto já existe no estoque.")
        else:
            self.produtos[produto.nome] = produto
            print(f"✅ Produto '{produto.nome}' adicionado com sucesso!")

    def atualizar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            self.produtos[nome].atualizar(preco, quantidade)
            print("✅ Produto atualizado com sucesso!")
        else:
            print("❌ Produto não encontrado.")

    def excluir_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print("✅ Produto excluído com sucesso!")
        else:
            print("❌ Produto não encontrado.")

    def visualizar_estoque(self):
        if not self.produtos:
            print("📦 Estoque vazio.")
            return

        print("\n===== ESTOQUE ATUAL =====")
        for produto in self.produtos.values():
            print(f"Produto: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {produto.quantidade}")
            print("-" * 30)


# =========================
# CLASSE SISTEMA
# =========================
class SistemaEstoque:
    def __init__(self):
        self.estoque = Estoque()
        self.carregar_produtos_iniciais()

    def carregar_produtos_iniciais(self):
        produtos_iniciais = [
            Produto("Teclado Gamer Logitech", 200.50, 10),
            Produto("Notebook Acer", 2899.00, 5),
            Produto("Fone de Ouvido Bluetooth JBL", 399.90, 20),
            Produto("Monitor 27 polegadas", 799.00, 7),
            Produto("Mouse Gamer Logitech", 149.90, 15)
        ]

        for produto in produtos_iniciais:
            self.estoque.produtos[produto.nome] = produto

    def menu(self):
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Atualizar produto")
        print("3 - Excluir produto")
        print("4 - Visualizar estoque")
        print("5 - Sair")

    def executar(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar()
            elif opcao == "2":
                self.atualizar()
            elif opcao == "3":
                self.excluir()
            elif opcao == "4":
                self.estoque.visualizar_estoque()
            elif opcao == "5":
                print("👋 Saindo do sistema...")
                break
            else:
                print("❌ Opção inválida.")

    def adicionar(self):
        try:
            nome = input("Nome do produto: ").strip()
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))

            produto = Produto(nome, preco, quantidade)
            self.estoque.adicionar_produto(produto)
        except ValueError:
            print("❌ Erro: digite valores válidos.")

    def atualizar(self):
        try:
            nome = input("Nome do produto: ").strip()
            preco = float(input("Novo preço: "))
            quantidade = int(input("Nova quantidade: "))

            self.estoque.atualizar_produto(nome, preco, quantidade)
        except ValueError:
            print("❌ Erro: digite valores válidos.")

    def excluir(self):
        nome = input("Nome do produto para excluir: ").strip()
        self.estoque.excluir_produto(nome)


# =========================
# EXECUÇÃO DO SISTEMA
# =========================
sistema = SistemaEstoque()
sistema.executar()

# Obrigado por comprar conosco! ;-)
