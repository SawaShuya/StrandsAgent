収集した情報を基に、AWS::ElasticLoadBalancingV2::LoadBalancerの完全な階層構造をYAML形式で出力します。

```yaml
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  EnableCapacityReservationProvisionStabilize: Boolean
  EnablePrefixForIpv6SourceNat: String  # on | off
  EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: String  # on | off
  IpAddressType: String  # ipv4 | dualstack | dualstack-without-public-ipv4
  Ipv4IpamPoolId: String
  LoadBalancerAttributes:
    - Key: String
      Value: String
  MinimumLoadBalancerCapacity:
    CapacityUnits: Integer
  Name: String
  Scheme: String  # internet-facing | internal
  SecurityGroups:
    - String
  SubnetMappings:
    - AllocationId: String
      IPv6Address: String
      PrivateIPv4Address: String
      SourceNatIpv6Prefix: String
      SubnetId: String
  Subnets:
    - String
  Tags:
    - Key: String
      Value: String
  Type: String  # application | network | gateway
```
