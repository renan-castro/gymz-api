from peewee import PostgresqlDatabase
from peewee import OperationalError

db = PostgresqlDatabase(
    'verceldb',  # Nome do banco de dados
    user='default',  # Usuário
    password='o0x9fwmFyhbK',  # Senha
    host='ep-orange-recipe-a4dedixq-pooler.us-east-1.aws.neon.tech',  # Host
    port=5432,  # Porta padrão do PostgreSQL
    sslmode='require'  # SSL mode
)

def test_connection():
    try:
        db.connect()
        print("Conexão bem-sucedida!")
    except OperationalError as e:
        print(f"Erro na conexão: {e}")
    finally:
        if not db.is_closed():
            db.close()

if __name__ == '__main__':
    test_connection()
