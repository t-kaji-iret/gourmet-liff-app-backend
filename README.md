# 社内グルメ掲載LIFFアプリ　バックエンドコード

## 環境構築

### MySQL

#### DBコンテナをビルド&起動

プロジェクトルートにて以下コマンドを実行。

```shell
docker compose up -d --build
```

### API（API Gateway + Lambda）

#### 事前準備

- SAMのインストール
    - https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/csharp-package-sam.html

- aws cliのインストール
    - https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html

- aws configureの設定
    - https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html

#### ビルド

```shell
sam build -m requirements.txt -t template.local.yaml
```

#### ローカル開発用のAPIエンドポイントを起動

```shell
sam local start-api --docker-network docker.internal
```

### パッケージ管理

#### 事前準備

- poetryのインストール
    - https://python-poetry.org/docs/#installing-with-the-official-installer
- poetryプラグインのインストール
    - https://github.com/python-poetry/poetry-plugin-export

#### パッケージ追加

```shell
poetry add パッケージ
```

#### パッケージをrequirements.txtにエクスポート

```shell
poetry export -f requirements.txt --output requirements.txt
```

※ パッケージ追加後は上記コマンドを実行するようにしてください。でないとsam build時にLambda環境に反映されません。


