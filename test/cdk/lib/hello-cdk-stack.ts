import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as appsync from "aws-cdk-lib/aws-appsync";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as cognito from "aws-cdk-lib/aws-cognito";
import path = require("path");

interface Config {
  userPoolId?: string;
}

interface HelloCdkStackProps extends cdk.StackProps {
  config: Config;
}

export class HelloCdkStack extends cdk.Stack {
  public readonly userPoolId: cdk.CfnOutput;
  public readonly graphqlApiUrl: cdk.CfnOutput;
  public readonly graphqlApiKey: cdk.CfnOutput;

  constructor(scope: Construct, id: string, props: HelloCdkStackProps) {
    super(scope, id, props);

    const env = "dev";

    // Cognito
    let userPool: cdk.aws_cognito.IUserPool;
    if (props.config.userPoolId) {
      userPool = cdk.aws_cognito.UserPool.fromUserPoolId(
        this,
        "user-pool",
        props.config.userPoolId
      );
    } else {
      // create new cognito
      userPool = new cognito.UserPool(this, "user-pool", {
        userPoolName: `${env}-eco`,
        selfSignUpEnabled: false,
        signInAliases: {
          username: true,
          preferredUsername: true,
        },
        passwordPolicy: {
          minLength: 6,
          requireDigits: false,
          requireLowercase: false,
          requireSymbols: false,
          requireUppercase: false,
        },
        mfa: cognito.Mfa.OFF,
        accountRecovery: cognito.AccountRecovery.NONE,
        customAttributes: {
          cci_code: new cognito.StringAttribute({ mutable: true, maxLen: 20 }),
          company_code: new cognito.StringAttribute({
            mutable: true,
            maxLen: 50,
          }),
          member_id: new cognito.StringAttribute({
            mutable: true,
            maxLen: 2024,
          }),
          user_type: new cognito.StringAttribute({ mutable: true, maxLen: 20 }),
        },
        email: cognito.UserPoolEmail.withCognito(),
        deletionProtection: true,
      });
    }
    this.userPoolId = new cdk.CfnOutput(this, "UserPoolId", {
      value: userPool.userPoolId,
    });

    // Appsync
    const graphqlApi = new appsync.GraphqlApi(this, `${env}-realtime`, {
      name: `${env}-realtime`,
      definition: appsync.Definition.fromFile(
        path.join(__dirname, "../asset/schema.graphql")
      ),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.API_KEY,
          apiKeyConfig: {
            expires: cdk.Expiration.after(cdk.Duration.days(365)),
          },
        },
        additionalAuthorizationModes: [
          {
            authorizationType: cdk.aws_appsync.AuthorizationType.IAM,
          },
          {
            authorizationType: cdk.aws_appsync.AuthorizationType.USER_POOL,
            userPoolConfig: { userPool },
          },
        ],
      },
    });

    const noneDS = graphqlApi.addNoneDataSource("NoneDataSource");
    noneDS.createResolver("sendMessageResolver", {
      typeName: "Mutation",
      fieldName: "sendMessage",
      requestMappingTemplate: appsync.MappingTemplate.fromString(
        '{"version": "2018-05-29","payload": $util.toJson($context.arguments.message)}'
      ),
      responseMappingTemplate: appsync.MappingTemplate.fromString(
        "$util.toJson($context.result)"
      ),
    });

    // Prints out URL
    this.graphqlApiUrl = new cdk.CfnOutput(this, "GraphQLAPIURL", {
      value: graphqlApi.graphqlUrl,
    });

    // Prints out the AppSync GraphQL API key to the terminal
    this.graphqlApiKey = new cdk.CfnOutput(this, "GraphQLAPIKey", {
      value: graphqlApi.apiKey || "",
    });
  }
}
