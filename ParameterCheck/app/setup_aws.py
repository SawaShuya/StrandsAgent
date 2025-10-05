import os
import sys
import boto3
from pathlib import Path
from strands.models import BedrockModel

# Get environment variables
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-1')

if 'AWS_PROFILE' in os.environ:
    profile = os.getenv('AWS_PROFILE')
    profile_role = os.getenv('AWS_PROFILE_ROLE')

def setup_aws_config():
    print("\n\nStart setup_aws_config ---------------------------------------------------------------")
    """Setup AWS CLI configuration files from environment variables"""
    
    if not access_key or not secret_key:
        print("Error: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables are required")
        sys.exit(1)
    
    # Create AWS directory
    aws_dir = Path.home() / '.aws'
    aws_dir.mkdir(exist_ok=True)
    
    # Create credentials file
    print("Setting up AWS credentials...")
    credentials_content = f"[default]\naws_access_key_id = {access_key}\naws_secret_access_key = {secret_key}"
    
    with open(aws_dir / 'credentials', 'w') as f:
        f.write(credentials_content)
    
    # Create config file
    print("Setting up AWS config...")
    config_content = f"[default]\nregion = {region}\noutput = json"

    # If  AWS_PROFILE environment variable is set, add it to the config file
    if 'AWS_PROFILE' in os.environ:
        print("Setting up AWS profile...")
        config_content += f"\n[profile {profile}]\nrole_arn = {profile_role}\nsource_profile = default\nregion = {region}"

    with open(aws_dir / 'config', 'w') as f:
        f.write(config_content)
    
    print("AWS CLI configuration completed")
    print(f"Region: {region}")

def get_session():
    sts = boto3.client('sts')
    assumed_role_response = sts.assume_role(
        RoleArn=profile_role,
        RoleSessionName="AssumeRoleSession"
    )

    credentials = assumed_role_response['Credentials']

    print(f"profile : {profile}")
    session = boto3.Session(
        profile_name=profile, 
        aws_access_key_id=credentials['AccessKeyId'], 
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    return session

def set_bedrock_model():
    print("\n\nStart set_bedrock_model ---------------------------------------------------------------")
    if 'AWS_PROFILE' in os.environ:
        print("Use Profile")
        session = get_session()
        bedrock_model = BedrockModel(
            model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
            temperature=0.0,
            boto_session=session
        )
    else:
        bedrock_model = BedrockModel(
            model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
            temperature=0.0
        )
    return bedrock_model