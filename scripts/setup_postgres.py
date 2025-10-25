@'
"""
Script para criar schema no PostgreSQL
Autor: Andre Luiz
"""
import psycopg2

def create_schema():
    try:
        print("🔌 Conectando ao PostgreSQL...")
        print("   Host: localhost:55432")
        print("   User: admin")
        print("   Database: northwind")
        
        conn = psycopg2.connect(
            host='localhost',
            port=55432,
            user='admin',
            password='admin',
            dbname='northwind'
        )
        
        print("✅ Conectado com sucesso!\n")
        
        cur = conn.cursor()
        
        print("📦 Criando schema dbt_dev...")
        cur.execute("CREATE SCHEMA IF NOT EXISTS dbt_dev;")
        
        cur.execute("""
            SELECT schema_name 
            FROM information_schema.schemata 
            WHERE schema_name NOT IN ('pg_catalog', 'information_schema')
            ORDER BY schema_name;
        """)
        
        schemas = cur.fetchall()
        
        print("✅ Schema criado com sucesso!\n")
        print("📋 Schemas disponíveis:")
        for schema in schemas:
            print(f"   - {schema[0]}")
        
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"\n🐘 PostgreSQL: {version.split(',')[0]}")
        
        conn.commit()
        cur.close()
        conn.close()
        
        print("\n✅ Tudo pronto para usar o DBT!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n💡 Verifique se o Docker está rodando:")
        print("   docker ps")

if __name__ == '__main__':
    create_schema()
'@ | Out-File -Encoding UTF8 scripts\setup_postgres.py