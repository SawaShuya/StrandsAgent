# StrandsAgent
https://strandsagents.com/latest/

CloudFormationテンプレートの申請内容と実際のスタック構成を比較・検証するエージェントシステム

## 事前準備

### 1. IAMユーザー・ロールの準備

以下のいずれかの方法でAWS認証を設定してください：

**方法A: IAMユーザーのアクセスキー**
- CloudFormationの読み取り権限を持つIAMユーザーを作成
- アクセスキーIDとシークレットアクセスキーを取得

**方法B: IAMロール（推奨）**
- CloudFormationの読み取り権限を持つIAMロールを作成
- AssumeRole可能なプロファイルを設定

### 2. Docker環境

- Docker Desktop または Docker Engine をインストール
- Windows環境では Docker Desktop for Windows を推奨

### 3. 環境変数ファイル

`.env.sample`を参考に`.env`ファイルを作成：

```bash
cp ParameterCheck/.env.sample ParameterCheck/.env
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

# スタック検索キーワード
KEYWORD=search_keyword
```

## ソースコード解説

### /app ディレクトリ構成

- **main.py**: メインエントリーポイント。各エージェントを順次実行
- **request_management_agent.py**: 申請テンプレート読み込みエージェント
  - `requested-template/`ディレクトリからCloudFormationテンプレートを読み取り
  - リソース情報を抽出・構造化
- **aws_cfn_agent.py**: AWS CloudFormation確認エージェント  
  - MCP（Model Context Protocol）を使用してAWS CloudFormationと連携
  - 指定キーワードでスタックを検索し、実際の構成を取得
- **check_agent.py**: 比較・検証エージェント
  - 申請テンプレートと実際のスタック構成を比較
  - マークダウン形式のレポートを生成
- **setup_aws.py**: AWS CLI設定ヘルパー

## 実行手順

1. **ParameterCheckディレクトリに移動**
   ```bash
   cd ParameterCheck
   ```

2. **申請テンプレートを配置**
   ```bash
   # requested-template/ディレクトリに検証対象のCloudFormationテンプレートを配置
   cp your-template.yaml requested-template/
   ```

3. **Docker実行**
   ```bash
   ./docker-run.sh
   ```

4. **実行結果確認**
   ```bash
   docker logs strands-agent
   ```

## 注意事項

- Windows環境では`docker-run.sh`内でパス変換が自動実行されます
- AWS認証情報は`.env`ファイルで管理し、リポジトリにコミットしないでください
- `KEYWORD`は実際のスタック名に含まれる文字列を指定してください