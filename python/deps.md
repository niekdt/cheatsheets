---
layout: default
title: Dependency management
parent: Python
nav_order: 500
---

# Dependency management
{: .no_toc}

1. TOC
{:toc}

## Pip

| What | How | Details |
|---|---|---|
| Upgrade pip | `python -m pip install --upgrade pip` | |
| Update all packages | ? | |
| Install packages from `requirements.txt` | `pip install -r requirements.txt` | |
| Generate `requirements.txt` from used imports only | `pigar generate` | `pipreqs` fails for misnamed modules | 
| Generate `requirements.txt` from **all** installed packages | `pip freeze > requirements.txt` | Great way to bloat your deps list... |


## Virtualenv

## Venv

## Poetry

Manages dependencies, package setup and building using the standardized `pyproject.toml` file. This replaces the need for `setup.py`, `requirements.txt`, `MANIFEST.in` and `Pipfile.*`.
Poetry isolates the virtualenv from the project.

| What | How | Details |
|---|---|---|
| Start a new Python project | `poetry new $pkg` | |
| Start a new Python package project | `poetry new --src $pkg` | |
| Initialize poetry env | `poetry init` | |
| List available packages | `poetry show` | |
| Install all dependencies as defined in `pyproject.toml` | `poetry install` | |
| Synchronize the environment with `pyproject.toml` | `poetry install --sync` | |
| Add specific packages | `poetry add $pkg1 $pkg2` | |
| Add a package for a specific version | `poetry add $pkg==1.0.1` | |
| Add a dev package | `poetry add -D $pkg` | |
| Add git dependency | `poetry add git+https://github.com/sdispater/pendulum.git` | |
| Add git dependency with version | `poetry add git+https://github.com/sdispater/pendulum.git#2.0.5` | |
| Add local dependency | `poetry add ./my-package/` | |
| Add local dependency archive | `poetry add ../my-package/dist/my-package-0.1.0.tar.gz` | |
| Remove packages | `poetry remove $pkg1 $pkg2` | |
| Update poetry | `poetry self update` | |
| Update all packages | `poetry update` | |
| Update specific packages | `poetry update $pkg1 $pkg2` | | 
| Export environment as `requirements.txt` | `poetry export -f requirements.txt --output requirements.txt` | |
