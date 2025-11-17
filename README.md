# Atlas&us backend

This project contains the backend of the Atlas&Us project. It's using `Fast API` and an SQL database

## Project installation

### Python and UV
In order to run this project, you'll need [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)
and python 3.13

In order to start the project, please use :
```bash
uv sync
```

### Database
You'll also need a PostgreSQL Database (see .env.sample for config)

## Running project
In order to run the project (once the config is done)

```bash
  # With your .venv activated
  uvicorn main:app
```

## Development feature
In order to simplify development, we've added some pre-commit check. To install them, you'll need to :

```bash
  # With your .venv activated
  pre-commit install --install-hooks
```

You can run all the checks with
```bash
  pre-commit run --all
```

## Authors

[Romb38](https://github.com/Romb38)  
[Lsa2222](https://github.com/Lsa2222)