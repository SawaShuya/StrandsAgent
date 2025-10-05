from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from strands.models import BedrockModel

from request_management_agent import get_requested_template
from aws_cfn_agent import get_cfn_template
from check_agent import create_final_report

if __name__ == "__main__":
    print("\n\nStart main process ---------------------------------------------------------------")
    # リクエストテンプレートの取得
    requested_template = get_requested_template()
    # print(f"Requested Template:\n{requested_template}")

    # # CFNテンプレートの確認
    created_template = get_cfn_template(requested_template)
    # print(f"Created Template:\ncreated_template")
    
    # # パラメータチェック
    final_report = create_final_report(requested_template, created_template)
    # print(f"Final Report:\n{final_report}")



