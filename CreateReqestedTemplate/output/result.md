## 収集した情報の整理

**申請情報（requested-alb.csv）：**
- TemplateType: AWS::ElasticLoadBalancingV2::LoadBalancer
- VpcId: vpc-b218f4d4
- SecurityGroup: 作成後に記載
- Subnet: subnet-0e43c8c66bcd30b52, subnet-0fd29810dddf03d60
- Type: application
- Schema: internal

**参照テンプレート（alb-reference.yaml）：**
- AWS::ElasticLoadBalancingV2::LoadBalancerの完全なテンプレート構造

申請情報に基づいて、参照テンプレートから必要な要素のみを抽出し、申請値をマッピングしたCloudFormationテンプレートを作成いたします。

```yaml
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  Scheme: internal
  SecurityGroups:
    - !Ref SecurityGroup
  Subnets:
    - subnet-0e43c8c66bcd30b52
    - subnet-0fd29810dddf03d60
  Type: application
```

**マッピング詳細：**
- `Scheme`: "internal" (申請のSchemaから)
- `SecurityGroups`: "作成後に記載" → `!Ref SecurityGroup`として参照形式に変換
- `Subnets`: 申請された2つのサブネットIDを配列として設定
- `Type`: "application" (申請のTypeから)
- VpcIdは直接的なプロパティではないため、サブネット指定により間接的に指定される形となります

申請にない要素（Name、Tags、LoadBalancerAttributesなど）は削除し、申請された情報のみでテンプレートを構成しました。
