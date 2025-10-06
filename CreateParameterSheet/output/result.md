これで、AWS::ElasticLoadBalancingV2::LoadBalancerの完全な情報を収集できました。すべての参照先プロパティタイプも展開して、YAML形式で階層構造を出力します。

## AWS::ElasticLoadBalancingV2::LoadBalancer - CloudFormation Template Reference

以下は、AWS::ElasticLoadBalancingV2::LoadBalancerの完全な階層構造をYAML形式で表現したものです。すべての参照先プロパティタイプを展開し、各項目の必須/任意の区別と制約をインラインコメントで記載しています。

```yaml
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  EnableCapacityReservationProvisionStabilize: Boolean  # Optional - プロビジョニング安定化の有効化
  EnablePrefixForIpv6SourceNat: String  # Optional - IPv6ソースNATプレフィックス使用 (on|off)
  EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: String  # Optional - PrivateLinkトラフィックでのSG規則適用 (on|off)
  IpAddressType: String  # Optional - IPアドレスタイプ (ipv4|dualstack|dualstack-without-public-ipv4)
  Ipv4IpamPoolId: String  # Optional - IPv4 IPAMプールID (Pattern: ^(ipam-pool-)[a-zA-Z0-9]+$, Max: 1000)
  LoadBalancerAttributes:  # Optional - ロードバランサー属性 (Max: 20)
    - Key: String  # Optional - 属性名 (Pattern: ^[a-zA-Z0-9._]+$, Max: 256)
      Value: String  # Optional - 属性値 (Max: 1024)
  MinimumLoadBalancerCapacity:  # Optional - 最小ロードバランサー容量
    CapacityUnits: Integer  # Required - 容量ユニット数
  Name: String  # Optional - ロードバランサー名 (最大32文字、英数字とハイフンのみ、internal-で開始不可)
  Scheme: String  # Optional - スキーム (internet-facing|internal)
  SecurityGroups:  # Optional - セキュリティグループID配列
    - String  # セキュリティグループID
  SubnetMappings:  # Conditional - サブネットマッピング (SubnetsまたはSubnetMappingsのいずれか必須)
    - AllocationId: String  # Optional - Elastic IP割り当てID (NLBのインターネット向け用)
      IPv6Address: String  # Optional - IPv6アドレス (NLB用)
      PrivateIPv4Address: String  # Optional - プライベートIPv4アドレス (NLB内部用)
      SourceNatIpv6Prefix: String  # Optional - ソースNAT用IPv6プレフィックス (NLB UDP用)
      SubnetId: String  # Required - サブネットID
  Subnets:  # Conditional - サブネットID配列 (SubnetsまたはSubnetMappingsのいずれか必須)
    - String  # サブネットID
  Tags:  # Optional - タグ配列 (Min: 1)
    - Key: String  # Required - タグキー (Pattern: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$, Min: 1, Max: 128)
      Value: String  # Optional - タグ値 (Pattern: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$, Min: 0, Max: 256)
  Type: String  # Optional - ロードバランサータイプ (application|network|gateway) デフォルト: application

# Return Values (参考)
# Ref: LoadBalancerのARNを返す
# Fn::GetAtt:
#   CanonicalHostedZoneID: Route 53ホストゾーンID
#   DNSName: DNSネーム
#   LoadBalancerArn: LoadBalancerのARN
#   LoadBalancerFullName: LoadBalancerのフルネーム
#   LoadBalancerName: LoadBalancerの名前
#   SecurityGroups: セキュリティグループID配列
```

### 重要な制約とポイント

1. **必須条件**: `Subnets`または`SubnetMappings`のいずれか一方は必須です
2. **Application Load Balancer**: 最低2つのAvailability Zoneのサブネットが必要
3. **Network Load Balancer**: 1つ以上のAvailability Zoneのサブネットが必要
4. **Gateway Load Balancer**: 1つ以上のAvailability Zoneのサブネットが必要
5. **名前制約**: 32文字以内、英数字とハイフンのみ、"internal-"で開始不可
6. **セキュリティグループ**: Application Load BalancerとNetwork Load Balancerでサポート
7. **LoadBalancerAttributes**: 最大20個まで設定可能で、削除保護やアクセスログなど様々な設定が可能

この構造により、Application Load Balancer、Network Load Balancer、Gateway Load Balancerのいずれも作成できます。
