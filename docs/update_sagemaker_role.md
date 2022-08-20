# Update the Sagemaker role to use Amazon Athena

If when using using Athena from a notebook, you get the following permissions error: `An error occurred (AccessDeniedException) when calling the StartQueryExecution operation: User: arn:aws:sts::055102001469:assumed-role/sagemaker-notebook-instance-role/SageMaker is not authorized to perform: athena:StartQueryExecution on resource: arn:aws:athena:us-east-1:055102001469:workgroup/primary because no identity-based policy allows the athena:StartQueryExecution action` then you need to update your IAM permissions.

1) Go to IAM, and click on **Roles**.

<img src="/docs/images/1_click_roles.png" width="550" height="400">

2) Search for the `sagemaker-notebook-instance-role` from the error message. Select the role in blue.

<img src="/docs/images/2_sagemaker_role.png" width="550" height="400">

3) Click **Add permissions** then **Create inline policy**.

<img src="/docs/images/3_inline_policy.png" width="550" height="350">

4) Fill out the form as in the screen shot below to attach the permission to the Sagemaker Role. Click **Review Policy**

<img src="/docs/images/4_add_inline_form.png" width="550" height="400">

5) Name your policy and click **Create policy**

<img src="/docs/images/5_name_and_create.png" width="550" height="450">

6) Confirm that the new policy is listed for the Sagemaker Role.

<img src="/docs/images/6_confirm_policy.png" width="550" height="400">
