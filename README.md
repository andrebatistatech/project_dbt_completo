@'
# Project DBT Completo

Projeto de Analytics Engineering com DBT e PostgreSQL desenvolvido por **Andre Luiz** (@andrebatistatech).

## 🚀 Tecnologias

- **Python 3.13.2**
- **Poetry 2.2.1** - Gerenciamento de dependências
- **DBT Core 1.10.13** - Transformação de dados
- **DBT Postgres 1.9.1** - Adaptador PostgreSQL
- **PostgreSQL 16** (Docker) - Database
- **Pandas/Polars** - Análise de dados

## 📁 Estrutura do Projeto
```
project_dbt_completo/
├── .venv/                    # Ambiente virtual Poetry
├── models/                   # Modelos DBT (SQL)
├── seeds/                    # Dados estáticos (CSV)
├── tests/                    # Testes DBT
├── macros/                   # Macros reutilizáveis
├── dbt_project.yml          # Configuração DBT
├── pyproject.toml           # Dependências Poetry
└── README.md                # Este arquivo

C:\Users\andre\.dbt\
└── profiles.yml             # Credenciais PostgreSQL
```
## 🔧 Setup Inicial

### Pré-requisitos

- Python 3.13+
- Poetry instalado (pipx install poetry)
- Docker com PostgreSQL rodando
- Git

### Instalação

Passo 1: Clonar repositório`
```
git clone <url-do-repo>
cd project_dbt_completo
```
Passo 2: Instalar dependências
```
poetry install --no-root
```
Passo 3: Ativar ambiente virtual
```
.\.venv\Scripts\activate
```
Passo 4: Verificar instalação
```
python --version
dbt --version
```
Passo 5: Testar conexão DBT
```
dbt debug
```
## 🐳 Configuração PostgreSQL (Docker)

### Credenciais
```
Host: localhost
Port: 55432
User: admin
Password: admin
Database: northwind
Schema: dbt_dev
```
### Arquivo profiles.yml
```
Localização: C:\Users\<seu-usuario>\.dbt\profiles.yml
```
Conteúdo:
```
default:
  target: postgres_local
  outputs:
    postgres_local:
      type: postgres
      host: localhost
      port: 55432
      user: admin
      password: admin
      dbname: northwind
      schema: dbt_dev
      threads: 4
```
## 📊 Comandos DBT

Testar conexão:
```
dbt debug
```
Executar modelos:
```
dbt run
```
Executar modelos específicos:
```
dbt run --select staging.*
dbt run --select marts.*
```
Carregar seeds (dados CSV):
```
dbt seed
```
Executar testes:
```
dbt test
```
Gerar documentação:
```
dbt docs generate
```
Servir documentação (abre no navegador):
```
dbt docs serve
```
Limpar arquivos temporários:
```
dbt clean
```
## 🛠️ Comandos Poetry

Adicionar nova dependência:
```
poetry add <pacote>
```

Adicionar dependência de desenvolvimento:
```
poetry add --group dev <pacote>
```
Atualizar dependências:
```
poetry update
```
Ver dependências instaladas:
```
poetry show
```
Ver informações do ambiente:
```
poetry env info
```
## 🔄 Workflow de Desenvolvimento

1. Ativar ambiente:
```
   .\.venv\Scripts\activate
```
2. Criar/editar modelos SQL em 
```
models/
```
3. Testar localmente:
```
   dbt run --select <nome_do_modelo>
   dbt test --select <nome_do_modelo>
   ```

4. Commitar mudanças:
```
   git add .
   git commit -m "feat: adicionar modelo X"
   git push
   ```

## 📝 Estrutura de Modelos DBT
```
models/
├── staging/          # Camada de staging (views)
│   └── stg_*.sql
├── intermediate/     # Transformações intermediárias (ephemeral)
│   └── int_*.sql
└── marts/            # Modelos finais (tables)
    └── mart_*.sql
```
## 🧪 Testes

DBT suporta testes nativos em schema.yml

## 📚 Documentação

Gerar e visualizar documentação:
```
dbt docs generate
dbt docs serve
```

Acesse: http://localhost:8080

## 🐛 Troubleshooting

### Erro: "Connection refused"

Verificar se Docker está rodando:
```
docker ps
```
Verificar logs do PostgreSQL:
```
docker logs <container-name>
```

### Erro: "profiles.yml not found"

Verificar localização:
```
dbt debug --config-dir
```

### Erro: "dbt command not found"

Ativar ambiente virtual:
```
.\.venv\Scripts\activate
```
## 👤 Autor

**Andre Luiz**
Analytics Engineer
Email: andre.batista.tech@gmail.com
GitHub: @andrebatistatech

## 📄 Licença

Este projeto é privado e confidencial.

## 🔗 Links Úteis

- Documentação DBT: https://docs.getdbt.com/
- DBT Best Practices: https://docs.getdbt.com/guides/best-practices
- Poetry Documentation: https://python-poetry.org/docs/
'@ | Out-File -Encoding UTF8 README.md

Write-Host "✅ README.md atualizado!" -ForegroundColor Green