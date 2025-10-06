# CreateParameterSheet

AWS CloudFormationの公式リファレンスを参照して、指定したリソースタイプのパラメータシートを自動生成するエージェントシステム

## 事前準備

### 1. IAMユーザー・ロールの準備

以下のいずれかの方法でAWS認証を設定してください：

**方法A: IAMユーザーのアクセスキー**
- Bedrockの実行権限を持つIAMユーザーを作成
- アクセスキーIDとシークレットアクセスキーを取得

**方法B: IAMロール（推奨）**
- Bedrockの実行権限を持つIAMロールを作成
- AssumeRole可能なプロファイルを設定

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

# 作成したいCloudFormationリソースタイプ
CF_TYPE=AWS::EC2::Instance
```

## ソースコード解説

### /app ディレクトリ構成

- **main.py**: メインエントリーポイント
  - AWS設定の初期化
  - Bedrockモデルの設定
  - エージェント実行と結果出力
- **aws_doc_agent.py**: AWS公式ドキュメント参照エージェント
  - MCP（Model Context Protocol）を使用してAWS公式ドキュメントと連携
  - 指定されたCloudFormationリソースタイプの公式リファレンスを検索
  - YAML形式のテンプレート構造を生成
- **setup_aws.py**: AWS認証・設定ヘルパー
  - 環境変数からAWS認証情報を読み取り
  - AWS CLI設定ファイルの自動生成
  - プロファイル認証とBedrockモデルの初期化

## 実行手順

1. **環境変数設定**
   ```bash
   # .envファイルでCF_TYPEを指定
   # 例: CF_TYPE=AWS::ApplicationAutoScaling::ScalableTarget
   ```

2. **Docker実行**
   ```bash
   ./docker-run.sh
   ```

3. **結果確認**
   ```bash
   # 生成されたパラメータシートを確認
   cat output/result.md
   
   # 実行ログ確認
   docker logs strands-agent-create-parameter-sheet
   ```

## 出力形式

- 生成されたパラメータシートは `output/result.md` に保存されます
- YAML形式でCloudFormationテンプレートの構造が出力されます
- 参照先のプロパティも展開された完全な形式で提供されます

## 対応リソースタイプ

AWS CloudFormationの全リソースタイプに対応：
- `AWS::EC2::Instance`
- `AWS::RDS::DBInstance`
- `AWS::S3::Bucket`
- `AWS::Lambda::Function`
- その他すべてのAWSリソースタイプ

## 注意事項

- Windows環境では`docker-run.sh`内でパス変換が自動実行されます
- AWS認証情報は`.env`ファイルで管理し、リポジトリにコミットしないでください
- `CF_TYPE`は正確なAWS CloudFormationリソースタイプ名を指定してください