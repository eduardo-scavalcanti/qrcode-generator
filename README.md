# Gerador de QR Code com Flask

Aplicação web desenvolvida em Python com Flask que permite gerar QR Codes a partir de URLs, exibir o resultado na tela e realizar o download da imagem gerada.

---

## Tecnologias utilizadas

- Python 3
- Flask
- HTML5
- Tailwind CSS
- JavaScript

### Outros
- qrcode
- Pillow (PIL) (dependência do qrcode)

---

## Funcionalidades

- Gerar QR Code a partir de uma URL
- Exibir o QR Code gerado na página
- Download do QR Code em formato `.png`
- Validação de URL no front-end
- Geração de nomes únicos para evitar sobrescrita de arquivos
- Limpeza automática de arquivos antigos no servidor

---

## Conceitos aplicados

- Rotas HTTP (`GET` e `POST`)
- Comunicação entre back-end e front-end
- Renderização de templates com Jinja2
- Manipulação de arquivos no sistema operacional
- Validação de dados no lado do cliente
- Gerenciamento de arquivos temporários

---

## Estrutura do projeto

```
qr_code_project/
│
├── app.py
├── static/
│ ├── qrcodes/
│ └── js/
│ └── validation.js
│
├── templates/
│ └── index.html
│
└── README.md
```

## Como executar o projeto

### 1° Clonar o repositório
```
git clone https://github.com/eduardo-scavalcanti/qrcode-generator
cd qrcode-generator
```

### 2° Criar e ativar o ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

### 3° Instalar as dependências
```
pip install -r requirements.txt
```

### 4° Executar a aplicação
```
python app.py
```

### 5° Acessar no navegador
http://127.0.0.1:5000
