# 社内グルメ掲載LIFFアプリ　バックエンドコード

=======
## 環境構築
### MySQL
#### DBコンテナをビルド&起動
プロジェクトルートにて以下コマンドを実行。
```
$ docker compose up -d --build
``

#lambda、samの準備

# 事前準備 
## samのインストール
https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/csharp-package-sam.html

## 第五開発のaws アカウントの自分ユーザーにliff-app-groupを紐づける
liff-app-group

## aws cliのインストール

## aws configureの設定
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html

region は ap-northeast-1

# ビルドコマンド
```
sam build
```

# ローカルでのapi起動
```
sam local start-api
```

# デプロイコマンド
```
sam deploy
```