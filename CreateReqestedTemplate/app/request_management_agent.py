from strands import Agent
from strands_tools import file_read

# Define a focused system prompt for file operations
system_prompt = """
あなたは申請されたCSVファイルをAWS CLoudFormationテンプレートに変換する管理するスペシャリストです。

主な機能
1. requested-simple-sheetディレクトリ内のCSVファイルを開きます。申請情報を抽出します。
2. reference-templateディレクトリ内のCloudFormationのyamaテンプレートをベースに申請情報をマッピングします。申請にない要素は削除します。作成後に記載となっている場合には!Refとします。
3. マッピングされたYaml形式のテンプレートを出力します。出力はテンプレートの部分のみで、その他は不要です。

回答時には明確化のため、必ずファイル名も明記してください。
"""

def create_requested_template(bedrock_model):
    print("\n\nStart get_requested_template ---------------------------------------------------------------")
    file_agent = Agent(
        system_prompt=system_prompt,
        tools=[file_read],
        model=bedrock_model
    )

    result = file_agent("必要な情報を収集してください。")

    return str(result)
