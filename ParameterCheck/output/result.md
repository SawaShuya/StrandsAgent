# CloudFormationテンプレート比較結果

## 比較結果サマリー

| 申請テンプレート名 | 実際のスタック名 | 総合判定 |
|---|---|---|
| reqested-alb-template.yaml | sample-dev-* | ○ |

## 詳細比較結果

### SecurityGroup

| 項目 | 申請値 | 実際値 | 比較結果 |
|---|---|---|---|
| Type | AWS::EC2::SecurityGroup | AWS::EC2::SecurityGroup | ○ |
| SecurityGroupIngress | tcp/80 from 172.31.0.0/16 | tcp/80 from 172.31.0.0/16 | ○ |
| SecurityGroupEgress | all traffic to 0.0.0.0/0 | all traffic to 0.0.0.0/0 | ○ |
| VpcId | 未指定 | vpc-b218f4d4 | 手動確認 |

### TargetGroup

| 項目 | 申請値 | 実際値 | 比較結果 |
|---|---|---|---|
| Type | AWS::ElasticLoadBalancingV2::TargetGroup | AWS::ElasticLoadBalancingV2::TargetGroup | ○ |
| IpAddressType | ipv4 | ipv4 | ○ |
| HealthCheckPath | / | / | ○ |
| Port | 80 | 80 | ○ |
| VpcId | vpc-b218f4d4 | vpc-b218f4d4 | ○ |
| TargetType | ip | ip | ○ |
| HealthCheckPort | traffic-port | traffic-port | ○ |
| Protocol | HTTP | HTTP | ○ |
| stickiness.enabled | false | false | ○ |

### LoadBalancer

| 項目 | 申請値 | 実際値 | 比較結果 |
|---|---|---|---|
| Type | AWS::ElasticLoadBalancingV2::LoadBalancer | AWS::ElasticLoadBalancingV2::LoadBalancer | ○ |
| VpcId | vpc-b218f4d4 | 手動確認（Subnetsから推定） | 手動確認 |
| SecurityGroups | !Ref SecurityGroup | sample-dev-sg-alb (SecurityGroup参照) | ○ |
| Subnets | subnet-0e43c8c66bcd30b52, subnet-0fd29810dddf03d60 | subnet-0e43c8c66bcd30b52, subnet-0fd29810dddf03d60 | ○ |
| Type | application | application | ○ |
| Scheme | internal | internal | ○ |

### Listener

| 項目 | 申請値 | 実際値 | 比較結果 |
|---|---|---|---|
| Type | AWS::ElasticLoadBalancingV2::Listener | AWS::ElasticLoadBalancingV2::Listener | ○ |
| Protocol | HTTP | HTTP | ○ |
| LoadBalancerArn | !Ref LoadBalancer | sample-dev-alb (LoadBalancer参照) | ○ |
| Port | 80 | 80 | ○ |
| DefaultActions | fixed-response (503, text/plain) | fixed-response (503, text/plain) | ○ |

### ListenerRule

| 項目 | 申請値 | 実際値 | 比較結果 |
|---|---|---|---|
| Type | AWS::ElasticLoadBalancingV2::ListenerRule | AWS::ElasticLoadBalancingV2::ListenerRule | ○ |
| Actions | TargetGroupArn !Ref TargetGroup | TargetGroupArn sample-dev-tg (TargetGroup参照) | ○ |
| Priority | 10 | 10 | ○ |
| Conditions | path-pattern "/sample*" | path-pattern "/sample*" | ○ |
| ListenerArn | !Ref Listener | sample-dev-alb Listener (Listener参照) | ○ |

## 注意事項

- 申請テンプレートではCloudFormation参照（!Ref）を使用していますが、実際のスタックでは具体的なリソース名で参照されています。これは正常な動作です。
- SecurityGroupのVpcIdが申請テンプレートでは明示的に指定されていませんが、実際のスタックでは設定されています。この点は手動確認が必要です。
- 全体的に申請内容と実際の作成内容は一致しており、適切にデプロイされています。
