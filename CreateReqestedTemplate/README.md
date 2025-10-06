# CreateRequestedTemplate

CSVファイルの申請情報をCloudFormationテンプレートに変換するエージェントシステム

## 事前準備

### 1. IAMユーザー・ロールの準備

以下のいずれかの方法でAWS認証を設定してください：

**方法A: IAMユーザー/グループの権限で利用する場合**
- CloudFormationの読み取り権限を持つIAMユーザーを作成
- アクセスキーIDとシークレットアクセスキーを取得

**方法B: IAMロール（Profile）の権限で利用する場合（推奨）**
- AssumeRole権限を持つIAMユーザーを作成
- CloudFormationの読み取り権限を持つIAMロールを作成（信頼ポリシーのプリンシパルはアカウントを設定すること）

### 2. Docker環境

- Docker Desktop または Docker Engine をインストール
- Windows環境では Docker Desktop for Windows を推奨

### 3. 環境変数ファイル

`.env.sample`を参考に`.env`ファイルを作成：

```bash
cp .env.sample .env
```

`.env`ファイルを編集し、以下の値を設定：

```env
# IAMユーザー認証の場合
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=ap-northeast-1

# プロファイル認証の場合（上記に加えて）
AWS_PROFILE=your_profile_name
AWS_PROFILE_ROLE=arn:aws:iam::account:role/role_name
```

## ソースコード解説

### /app ディレクトリ構成

- **main.py**: メインエントリーポイント
  - AWS設定の初期化
  - Bedrockモデルの設定
  - テンプレート変換処理の実行と結果出力
- **request_management_agent.py**: 申請テンプレート変換エージェント
  - `requested-simple-sheet/`ディレクトリからCSVファイルを読み取り
  - `reference-template/`ディレクトリからベースとなるCloudFormationテンプレートを参照
  - CSVの申請情報をCloudFormationテンプレートにマッピング
  - 申請にない要素は削除し、作成後記載項目は!Refに変換
- **setup_aws.py**: AWS認証・設定ヘルパー
  - 環境変数からAWS認証情報を読み取り
  - AWS CLI設定ファイルの自動生成
  - プロファイル認証とBedrockモデルの初期化

## 実行手順

1. **申請ファイルを配置**
   ```bash
   # CSVファイルをrequested-simple-sheet/ディレクトリに配置
   cp your-request.csv requested-simple-sheet/
   
   # 参照テンプレートをreference-template/ディレクトリに配置
   cp your-reference.yaml reference-template/
   ```

2. **Docker実行**
   ```bash
   ./docker-run.sh
   ```

3. **結果確認**
   ```bash
   # 生成されたCloudFormationテンプレートを確認
   cat output/result.md
   
   # 実行ログ確認
   docker logs strands-agent-create-requested-template
   ```

## 入力ファイル形式

### CSVファイル（requested-simple-sheet/）
申請情報を含むCSVファイル。リソースのパラメータや設定値を記載。

### 参照テンプレート（reference-template/）
ベースとなるCloudFormationテンプレート（YAML形式）。申請情報がマッピングされる雛形。

## 出力形式

- 生成されたCloudFormationテンプレートは `output/result.md` に保存されます
- YAML形式で申請情報が反映されたテンプレートが出力されます
- 申請にない要素は自動的に削除されます
- 作成後記載項目は `!Ref` 形式に変換されます

## 注意事項

- Windows環境では`docker-run.sh`内でパス変換が自動実行されます
- AWS認証情報は`.env`ファイルで管理し、リポジトリにコミットしないでください
- CSVファイルと参照テンプレートの対応関係を事前に確認してください