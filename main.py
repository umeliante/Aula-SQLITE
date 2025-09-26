#Criar um banco de dados SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamado de "cursor" que será usado para executar os comandos sql
cursor = conexao.cursor()

#Criar uma tabela no banco
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT
#     )
# """)

# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ")

# #Inserir um dado na tabela 
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,
# (nome, idade, curso)
# )

# #Confimar as alterações no banco 
# conexao.commit()


#Iserir varios alunos de uma só vez
# alunos = [
#     ("Yago", 28, "Direito"),
#     ("Jessica", 24, "Computação"),
#     ("Breno", 54, "Computação"),
# ]
# #executemany permite inserir mútiplas linhas de um vez só
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,
# (alunos)
# )
# conexao.commit()


#Atulizar dados no banco 
cursor.execute("""
UPDATE alunos
SET idade = ?, curso = ?
WHERE id = ?
""", (61, "Medicina", 2)
)
conexao.commit()