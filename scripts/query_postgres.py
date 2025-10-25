@'
"""
Script para consultar dados no PostgreSQL
Autor: Andre Luiz
"""
import psycopg2
import pandas as pd

def query_postgres():
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=55432,
            user='admin',
            password='admin',
            dbname='northwind'
        )
        
        print("="*70)
        print("✅ CONECTADO AO POSTGRESQL (Docker - Porta 55432)")
        print("   Database: northwind")
        print("   Schema: dbt_dev")
        print("="*70)
        
        print("\n📋 TABELAS NO SCHEMA dbt_dev:")
        print("-"*70)
        df_tables = pd.read_sql("""
            SELECT 
                table_name,
                table_type
            FROM information_schema.tables 
            WHERE table_schema = 'dbt_dev'
            ORDER BY table_name;
        """, conn)
        
        if len(df_tables) > 0:
            print(df_tables.to_string(index=False))
        else:
            print("   (Nenhuma tabela ainda - execute 'dbt seed' e 'dbt run')")
        
        print("\n\n👥 EMPLOYEES (Seed Data):")
        print("-"*70)
        try:
            df_seed = pd.read_sql("""
                SELECT * FROM dbt_dev.employees
                ORDER BY id;
            """, conn)
            print(df_seed.to_string(index=False))
        except Exception as e:
            print(f"   (Tabela ainda não existe - execute 'dbt seed')")
        
        print("\n\n📦 STG_EMPLOYEES (Staging Layer):")
        print("-"*70)
        try:
            df_staging = pd.read_sql("""
                SELECT 
                    id,
                    name,
                    department,
                    score,
                    hire_date
                FROM dbt_dev.stg_employees
                ORDER BY score DESC
                LIMIT 5;
            """, conn)
            print(df_staging.to_string(index=False))
        except Exception as e:
            print(f"   (View ainda não existe - execute 'dbt run')")
        
        print("\n\n📊 MART_DEPARTMENT_STATS (Analytics Layer):")
        print("-"*70)
        try:
            df_marts = pd.read_sql("""
                SELECT 
                    department,
                    total_employees,
                    avg_score,
                    min_score,
                    max_score,
                    first_hire_date,
                    last_hire_date
                FROM dbt_dev.mart_department_stats
                ORDER BY avg_score DESC;
            """, conn)
            print(df_marts.to_string(index=False))
        except Exception as e:
            print(f"   (Tabela ainda não existe - execute 'dbt run')")
        
        print("\n" + "="*70)
        print("✅ CONSULTA CONCLUÍDA COM SUCESSO!")
        print("="*70 + "\n")
        
        conn.close()
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}\n")
        print("💡 Verifique se:")
        print("   1. Docker está rodando: docker ps")
        print("   2. PostgreSQL está acessível na porta 55432")
        print("   3. Credenciais estão corretas (admin/admin)")

if __name__ == '__main__':
    query_postgres()
'@ | Out-File -Encoding UTF8 scripts\query_postgres.py