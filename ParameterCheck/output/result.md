# CloudFormationテンプレート比較結果

## 比較概要
- **申請テンプレート名**: reqested-alb-template.yaml
- **実際のスタック名**: sample-dev-cf-alb

## 詳細比較結果

### SecurityGroup

| 項目 | 申請値 | 実際値 | 比較結果 |
|------|--------|--------|----------|
| Type | AWS::EC2::SecurityGroup | AWS::EC2::SecurityGroup | 〇 |
| SecurityGroupIngress | tcp/80 from 172.31.0.0/16 | tcp/80 from 172.31.0.0/16 | 〇 |
| SecurityGroupEgress | all traffic to 0.0.0.0/0 | all traffic to 0.0.0.0/0 | 〇 |
| GroupDescription | 記載なし | sample-dev-sg-alb | 手動確認 |
| GroupName | 記載なし | sample-dev-sg-alb | 手動確認 |
| VpcId | 記載なし | vpc-b218f4d4 | 手動確認 |

### TargetGroup

| 項目 | 申請値 | 実際値 | 比較結果 |
|------|--------|--------|----------|
| Type | AWS::ElasticLoadBalancingV2::TargetGroup | AWS::ElasticLoadBalancingV2::TargetGroup | 〇 |
| IpAddressType | ipv4 | ipv4 | 〇 |
| HealthCheckPath | / | / | 〇 |
| Port | 80 | 80 | 〇 |
| VpcId | vpc-b218f4d4 | vpc-b218f4d4 | 〇 |
| TargetType | ip | ip | 〇 |
| HealthCheckPort | traffic-port | traffic-port | 〇 |
| Protocol | HTTP | HTTP | 〇 |
| stickiness.enabled | false | false | 〇 |
| Name | 記載なし | sample-dev-tg | 手動確認 |

### LoadBalancer

| 項目 | 申請値 | 実際値 | 比較結果 |
|------|--------|--------|----------|
| Type | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::ElasticLoadBalancingV2::LoadBalancer | 〇 |
| VpcId | vpc-b218f4d4 | vpc-b218f4d4 | 〇 |
| SecurityGroups | !Ref SecurityGroup | sample-dev-sg-alb (SecurityGroupリソース) | 〇 |
| Subnets | subnet-0e43c8c66bcd30b52, subnet-0fd29810dddf03d60 | subnet-0e43c8c66bcd30b52, subnet-0fd29810dddf03d60 | 〇 |
| Type | application | application | 〇 |
| Scheme | internal | internal | 〇 |
| Name | 記載なし | sample-dev-alb | 手動確認 |

### Listener

| 項目 | 申請値 | 実際値 | 比較結果 |
|------|--------|--------|----------|
| Type | AWS::ElasticLoadBalancingV2::Listener | AWS::ElasticLoadBalancingV2::Listener | 〇 |
| Protocol | HTTP | HTTP | 〇 |
| LoadBalancerArn | !Ref LoadBalancer | sample-dev-alb (LoadBalancerリソース) | 〇 |
| Port | 80 | 80 | 〇 |
| DefaultActions | fixed-response (503 status) | fixed-response (503 status) | 〇 |

### ListenerRule

| 項目 | 申請値 | 実際値 | 比較結果 |
|------|--------|--------|----------|
| Type | AWS::ElasticLoadBalancingV2::ListenerRule | AWS::ElasticLoadBalancingV2::ListenerRule | 〇 |
| TargetGroupArn | !Ref TargetGroup | sample-dev-tg (TargetGroupリソース) | 〇 |
| Priority | 10 | 10 | 〇 |
| Conditions | path-pattern "/sample*" | path-pattern "/sample*" | 〇 |
| ListenerArn | !Ref Listener | sample-dev-alb Listener (Listenerリソース) | 〇 |

## 総合評価

- **一致項目**: 20項目
- **不一致項目**: 0項目
- **手動確認必要項目**: 5項目

申請されたテンプレートの主要パラメータは全て正しく設定されています。手動確認が必要な項目は、申請テンプレートに記載されていないリソース名やメタデータ項目のみです。
