from setup_aws import setup_aws_config, set_bedrock_model
from request_management_agent import create_requested_template

if __name__ == "__main__":
    print("\n\nStart main process ---------------------------------------------------------------")

    # Set up AWS CLI
    setup_aws_config()

    # Get Bedrock Model
    bedrock_model = set_bedrock_model()

    # CFNテンプレートの公式リファレンス参照
    requested_template = create_requested_template(bedrock_model)

    # 出力
    print("\n\nWrite result to ./output/result.md ---------------------------------------------------------------")
    with open('./output/result.md', 'w', encoding='utf-8') as f:
        f.write(requested_template)

