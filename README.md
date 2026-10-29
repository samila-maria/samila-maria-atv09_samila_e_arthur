# ATV09 — Portal Django

**Dupla:** Samila Maria Pereira Cabral e Arthur Barbosa dos Santos  
**Turma:** 523  
**Atividade:** Migração do portal (ATV06) para Django

Pasta de entrega: `ATV09_Samila_Arthur`

## Descrição

Portal institucional da dupla, migrado da ATV06 para Django. O layout (cabeçalho, menu, área de conteúdo e rodapé) fica nos templates. Os textos das páginas e os itens do menu são cadastrados no Django Admin e lidos do banco de dados.

- Conteúdos internos: Início, Currículo Samila, Tema livre Samila, Currículo Arthur, Tema livre Arthur
- Links externos: GitHub Samila e GitHub Arthur

Alterações feitas no Admin (ativar/desativar, reordenar o menu, editar HTML) aparecem no portal sem mudar o template.

## Tecnologias

- Python 3
- Django 6.1.2
- SQLite
- HTML semântico, CSS (Flexbox e Media Queries) e JavaScript para a troca de imagens do tema do Arthur

## Como executar

Os comandos abaixo devem ser rodados na pasta do projeto Django, onde está o arquivo `manage.py`.

### 1. Ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Dependências

```bash
pip install -r requirements.txt
```

### 3. Migrations

```bash
python manage.py migrate
```

### 4. Dados iniciais (conteúdos e menu)

```bash
python manage.py loaddata portal/fixtures/conteudos_e_menus.json
```

### 5. Superusuário (Django Admin)

```bash
python manage.py createsuperuser
```

Informe usuário, e-mail e senha quando o terminal pedir.

### 6. Servidor

```bash
python manage.py runserver
```

### 7. Acesso

- Portal: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

No Admin é possível cadastrar, editar, ativar/desativar e reordenar conteúdos e itens de menu.

## GitHub

Publique este projeto em um repositório da dupla no GitHub e informe o link na entrega do Classroom.
