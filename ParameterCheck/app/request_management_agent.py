from strands import Agent
from strands_tools import file_read

# Define a focused system prompt for file operations
system_prompt = """
あなたは申請されたAWS CLoudFormationテンプレートを管理するスペシャリストです。
申請された構造化テンプレートはrequested-templateディレクトリに格納されます。

主な機能
1. requested_templateディレクトリ内の構造化ファイルを開きます。
2. テンプレート内から情報を取得し、CloudFormationのTypeや各種設定値を抽出します。
3. 抽出した情報は文字列として出力します。リソース情報のみを出力に含め、構成概要などの説明はしません。

回答時には明確化のため、必ずファイル名も明記してください。
"""

def get_requested_template(bedrock_model):
    print("\n\nStart get_requested_template ---------------------------------------------------------------")
    file_agent = Agent(
        system_prompt=system_prompt,
        tools=[file_read],
        model=bedrock_model
    )

    result = file_agent("必要な情報を収集してください。")

    return str(result)
