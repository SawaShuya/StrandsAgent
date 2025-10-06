from setup_aws import setup_aws_config, set_bedrock_model
from aws_doc_agent import get_cfn_reference

if __name__ == "__main__":
    print("\n\nStart main process ---------------------------------------------------------------")

    # Set up AWS CLI
    setup_aws_config()

    # Get Bedrock Model
    bedrock_model = set_bedrock_model()

    # CFNテンプレートの公式リファレンス参照
    cfn_reference = get_cfn_reference(bedrock_model)

    # 出力
    print("\n\nWrite result to ./output/result.md ---------------------------------------------------------------")
    with open('./output/result.md', 'w', encoding='utf-8') as f:
        f.write(cfn_reference)

