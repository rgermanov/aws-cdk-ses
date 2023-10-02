import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { LambdaDestination } from 'aws-cdk-lib/aws-lambda-destinations';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class AwsSesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'AwsSesQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });

    const fn = new lambda.Function(this, 'AwsSesFunction', {
      runtime: lambda.Runtime.PYTHON_3_9,
      handler: 'send_email.handler',
      code: lambda.Code.fromAsset('src'),
    });

    // Grant SES permissions to the Lambda function
    fn.addToRolePolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
          "ses:SendEmail",
          "ses:SendRawEmail"
      ],
      resources: ["*"]
    }));

  }
}
