import os
import boto3

from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters


KEYWORD = os.getenv('KEYWORD')

system_prompt = f"""
あなたはCloudFormationのテンプレートを確認するエージェントです。
1. スタック名に{KEYWORD}が入ったスタックを探します。
2. 申請者から提出されているテンプレートを参照し、該当する作成済みテンプレート情報のみをレスポンスします。構成概要などの説明はしません。
3. CloudFormationのテンプレート内に!Refや!Sub、!GetAttrなどの参照があった場合には、参照先の情報に書き換えてください。
"""

if 'AWS_PROFILE' in os.environ:
    profile = os.getenv('AWS_PROFILE')
    env={"AWS_PROFILE": profile, "AWS_REGION": "ap-northeast-1"}
else:
    env={"AWS_REGION": "ap-northeast-1"}

aws_cfn_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            # CloudFormation MCP Server
            args=["awslabs.cfn-mcp-server@latest", "--readonly"],
            # AWS CLI Profile
            env=env
        )
    )
)

# bedrock_model = BedrockModel(
#     model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
#     temperature=0.0,
#     boto_session=session
# )

def get_cfn_template(bedrock_model, requested_template):
    print("\n\nStart get_cfn_template ---------------------------------------------------------------")
    with aws_cfn_mcp_client:
        tools = aws_cfn_mcp_client.list_tools_sync()
        agent = Agent(
            system_prompt=system_prompt, tools=tools, model=bedrock_model
        )

        result = agent(f"申請者からのテンプレート: {requested_template} . 利用可能なツールを活用し、情報収集してください。")
        return str(result)

