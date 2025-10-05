from strands import Agent

# Define a focused system prompt for file operations
system_prompt = """
あなたは申請されたAWS CLoudFormationテンプレートと実際に作成されたCLoudFormationテンプレートを比較するスペシャリストです。

主な機能
1. 申請されたCloudFormationテンプレートと作成されたCloudFormationテンプレートを比較してパラメータが正しく設定されているかを確認します。
2. 申請テンプレートと作成されたテンプレートの値が一致するのであれば"〇"、一致しないのであれば"×"、確認ができない場合は"手動確認"というステータスにします。
3. 最終アウトプットはマークダウン形式の文字列にします。最終アウトプットには申請値、申請テンプレート名、実際値、実際のスタック名、比較結果のカラムは必ず入れてください。
"""

def create_final_report(bedrock_model, requested_template, created_template):
    file_agent = Agent(
        system_prompt=system_prompt,
        model=bedrock_model
    )

    result = file_agent(f"申請テンプレート: {requested_template}, 作成されたテンプレート: {created_template} .")

    return str(result)