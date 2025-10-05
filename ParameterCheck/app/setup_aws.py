#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def setup_aws_config():
    """Setup AWS CLI configuration files from environment variables"""
    # Get environment variables
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-1')
    
    if not access_key or not secret_key:
        print("Error: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables are required")
        sys.exit(1)
    
    # Create AWS directory
    aws_dir = Path.home() / '.aws'
    aws_dir.mkdir(exist_ok=True)
    
    # Create credentials file
    print("Setting up AWS credentials...")
    credentials_content = f"""[default]
aws_access_key_id = {access_key}
aws_secret_access_key = {secret_key}
"""
    
    with open(aws_dir / 'credentials', 'w') as f:
        f.write(credentials_content)
    
    # Create config file
    print("Setting up AWS config...")
    config_content = f"""[default]
region = {region}
output = json
"""

    # If  AWS_PROFILE environment variable is set, add it to the config file
    if 'AWS_PROFILE' in os.environ:
        profile = os.getenv('AWS_PROFILE')
        profile_role = os.getenv('AWS_PROFILE_ROLE')
        config_content += f"\n\n[profile {profile}]\nrole_arn = {profile_role}\nsource_profile = default"
    
    with open(aws_dir / 'config', 'w') as f:
        f.write(config_content)
    
    print("AWS CLI configuration completed")
    print(f"Region: {region}")
