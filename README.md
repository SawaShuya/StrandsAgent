# StrandsAgent

AWS CloudFormationテンプレート管理のための3つのエージェントシステム

## プロジェクト構成

### 1. CreateParameterSheet
AWS CloudFormationの公式リファレンスを参照して、指定したリソースタイプのパラメータシートを自動生成するエージェント

**主な機能:**
- AWS公式ドキュメントからCloudFormationリソースタイプの仕様を取得
- YAML形式のテンプレート構造を自動生成
- 全AWSリソースタイプに対応

**使用例:**
```bash
cd CreateParameterSheet
# .envでCF_TYPE=AWS::EC2::Instanceを設定
./docker-run.sh
```

### 2. CreateRequestedTemplate
CSVファイルの申請情報をCloudFormationテンプレートに変換するエージェント

**主な機能:**
- CSVファイルから申請情報を読み取り
- 参照テンプレートをベースにCloudFormationテンプレートを生成
- 申請にない要素の自動削除
- 作成後記載項目の!Ref変換

**使用例:**
```bash
cd CreateRequestedTemplate
# requested-simple-sheet/にCSVファイルを配置
# reference-template/に参照テンプレートを配置
./docker-run.sh
```

### 3. ParameterCheck
CloudFormationテンプレートの申請内容と実際のスタック構成を比較・検証するエージェント

**主な機能:**
- 申請テンプレートと実際のAWSスタック構成を比較
- MCP（Model Context Protocol）を使用したAWS連携
- マークダウン形式の検証レポート生成

**使用例:**
```bash
cd ParameterCheck
# requested-template/に検証対象テンプレートを配置
# .envでKEYWORDを設定
./docker-run.sh
```

## 共通要件

### AWS認証設定
各ディレクトリで`.env`ファイルを設定：
```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=ap-northeast-1
AWS_PROFILE=your_profile_name
AWS_PROFILE_ROLE=arn:aws:iam::account:role/role_name
```

### Docker環境
- Docker Desktop または Docker Engine
- Windows環境では Docker Desktop for Windows を推奨

## ワークフロー例

1. **CreateParameterSheet**: 新しいリソースタイプのテンプレート雛形を生成
2. **CreateRequestedTemplate**: 申請情報をもとに実際のテンプレートを作成
3. **ParameterCheck**: 作成したテンプレートと既存スタックの整合性を検証

各エージェントの詳細は、対応するディレクトリのREADME.mdを参照してください。