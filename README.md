# 社内グルメ掲載LIFFアプリ　バックエンドコード

## 環境構築
### MySQL
#### DBコンテナをビルド&起動
プロジェクトルートにて以下コマンドを実行。
```
$ docker compose up -d --build
```

##　AWS SAM によるローカル環境構築
### 事前準備 
#### SAMのインストール
https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/csharp-package-sam.html
#### aws cliのインストール
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html
#### aws configureの設定
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html
```
region は ap-northeast-1
```

#### ビルド
```
sam build
```

#### ローカルでのapi起動
```
sam local start-api
```

#### SAMによるlambda、APIGatewayのデプロイ
```
sam deploy
```
