# UniMater - SINF4NA - Avaliação 1 - Segundo Bimestre

## Professor: Cezar Augusto Mezzalira

## Instruções para esta avaliação

1 - Faça um fork do projeto em seu GitHub

2 - Clone o repositório que acabou de criar em sua máquina

3 - Abra o projeto no seu editor (Recomendo VSCode)

4 - Abra o arquivo `pyproject.toml` e dentro da propriedade `authors` altere com o seu nome e seu email o primeiro item do array.

5 - Siga os passos abaixo para inicializar seu projeto

## Inicializando o banco de dados

Abra um janela do PowerShell ou GitBash e acesse seu Linux. Para acessa-lo basta digitar o comando `wsl`.

Dentro do seu Linux, execute a linha de comando abaixo:

```sh
docker run --name pg-arline-db -p 54323:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=airline_db -d postgres:14
```

Dessa forma, será criado o banco de dados que você irá usar na prova.

## Instalando as dependências

O próximo passo é instalar as dependências do projeto. Como estamos usando o poetry, basta executar comando abaixo:

```sh
poetry install
```

## Iniciando o servidor HTTP para começar a prova

Agora, é só executar o servidor http através do comando abaixo:

```sh
poetry run uvicorn src.server:app --reload
```

## Próximos passos

Siga as instruções da prova que estão no moodle