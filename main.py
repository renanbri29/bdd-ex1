import sqlite3

# 1. Conectar ao banco de dados (cria o arquivo 'crud.db' se não existir)
con = sqlite3.connect("crud.db")
cur = con.cursor()

# 2. Criar a tabela 'table1'
cur.execute("""
CREATE TABLE IF NOT EXISTS table1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
con.commit()

# --- OPERAÇÕES DO CRUD ---

# C - CREATE (Inserir dados)
def criar_usuario(nome, idade):
    cur.execute("INSERT INTO table1 (name, age) VALUES (?, ?)", (nome, idade))
    con.commit()
    print(f"Usuário '{nome}' criado com sucesso!")

# R - READ (Ler/Buscar dados)
def listar_usuarios():
    cur.execute("SELECT * FROM table1")
    usuarios = cur.fetchall()
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]}")
    print("-------------------------\n")

# U - UPDATE (Atualizar dados)
def atualizar_usuario(id_usuario, novo_nome, nova_idade):
    cur.execute("UPDATE table1 SET name = ?, age = ? WHERE id = ?", (novo_nome, nova_idade, id_usuario))
    con.commit()
    print(f"Usuário ID {id_usuario} atualizado com sucesso!")

# D - DELETE (Excluir dados)
def deletar_usuario(id_usuario):
    cur.execute("DELETE FROM table1 WHERE id = ?", (id_usuario,))
    con.commit()
    print(f"Usuário ID {id_usuario} removido com sucesso!")


# --- TESTANDO AS FUNÇÕES ---

# Exemplo de uso:
criar_usuario("Alice", 25)
criar_usuario("Bob", 30)

listar_usuarios()  # Exibe Alice e Bob

atualizar_usuario(1, "Alice Silva", 26)  # Atualiza o cadastro do ID 1
listar_usuarios()  # Exibe os dados atualizados

deletar_usuario(2)  # Remove o ID 2 (Bob)
listar_usuarios()  # Exibe apenas Alice Silva

# Fechar a conexão
con.close()