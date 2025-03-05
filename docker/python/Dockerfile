FROM python:3.11.0

WORKDIR /liff-app-backend

# Poetryのインストール
RUN pip install --no-cache-dir poetry

# `poetry.lock` もあればキャッシュ効くのでコピー
COPY pyproject.toml poetry.lock* /liff-app-backend/

ENV PATH /root/.local/bin:$PATH

RUN poetry env use python3.11
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root

# アプリコードのコピー
COPY . /liff-app-backend
