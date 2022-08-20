# Update the Sagemaker role to use Amazon Athena

If when using using Athena from a notebook, you get the following permissions error: `An error occurred (AccessDeniedException) when calling the StartQueryExecution operation: User: arn:aws:sts::055102001469:assumed-role/sagemaker-notebook-instance-role/SageMaker is not authorized to perform: athena:StartQueryExecution on resource: arn:aws:athena:us-east-1:055102001469:workgroup/primary because no identity-based policy allows the athena:StartQueryExecution action` then you need to update your IAM permissions.

1) Go to IAM, 
