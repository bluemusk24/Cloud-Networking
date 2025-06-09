#!/bin/bash

# ==== Configuration ====
STACK_NAME="network-bootcamp"
TEMPLATE_FILE="template.yml"  # Ensure this matches your template filename
REGION="us-east-1"            # Change to your preferred AWS region
AZ="us-east-1a"               # Must match the selected region

# ==== Deployment ====
echo "Deploying CloudFormation stack: $STACK_NAME"

aws cloudformation deploy \
  --template-file "$TEMPLATE_FILE" \
  --stack-name "$STACK_NAME" \
  --region "$REGION" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    AvailabilityZone="$AZ"

# ==== Output results ====
if [ $? -eq 0 ]; then
  echo "✅ Stack '$STACK_NAME' deployed successfully."
  echo "Fetching outputs..."
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    --query "Stacks[0].Outputs" \
    --output table
else
  echo "❌ Failed to deploy stack '$STACK_NAME'."
fi
