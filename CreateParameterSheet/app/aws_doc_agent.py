import os
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters

CF_TYPE = os.getenv('CF_TYPE')

system_prompt = f"""
あなたはCloudFormation Template Referenceの読み込みを行うスペシャリストです。

主な機能
1. AWSの公式のCloudFormation Template Referenceの参照を行います。
2. CloudFormationのTypeの値が{CF_TYPE}と一致したものを探します。
3. 階層構造をYmal形式の文字列として出力します。参照先がある場合にはそれらをすべて展開した形で出力を行います。出力はテンプレートのみで、解説などは行いません。
"""

aws_doc_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx",
            # AWS Document MCP Server
            args=["awslabs.aws-documentation-mcp-server@latest"],
        )
    )
)


def get_cfn_reference(bedrock_model):
    print("\n\nStart get_cfn_reference ---------------------------------------------------------------")
    with aws_doc_mcp_client:
        tools = aws_doc_mcp_client.list_tools_sync()
        agent = Agent(
            system_prompt=system_prompt, tools=tools, model=bedrock_model
        )

        result = agent(f"利用可能なツールを活用し、情報収集してください。")
        return str(result)

