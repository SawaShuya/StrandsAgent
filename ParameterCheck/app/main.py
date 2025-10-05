from setup_aws import setup_aws_config, set_bedrock_model
from request_management_agent import get_requested_template
from aws_cfn_agent import get_cfn_template
from check_agent import create_final_report

if __name__ == "__main__":
    print("\n\nStart main process ---------------------------------------------------------------")

    # Set up AWS CLI
    setup_aws_config()

    # Get Bedrock Model
    bedrock_model = set_bedrock_model()

    # リクエストテンプレートの取得
    requested_template = get_requested_template(bedrock_model)
    # print(f"Requested Template:\n{requested_template}")

    # CFNテンプレートの確認
    created_template = get_cfn_template(bedrock_model, requested_template)
    # print(f"Created Template:\ncreated_template")
    
    # パラメータチェック
    final_report = create_final_report(bedrock_model, requested_template, created_template)
    # print(f"Final Report:\n{final_report}")


    print("\n\nWrite result to ./output/result.md ---------------------------------------------------------------")
    with open('./output/result.md', 'w', encoding='utf-8') as f:
        f.write(final_report)



