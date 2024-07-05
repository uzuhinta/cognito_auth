import {
  AppConfigClient,
  CreateApplicationCommand,
  CreateEnvironmentCommand,
  CreateConfigurationProfileCommand,
  CreateHostedConfigurationVersionCommand,
  StartDeploymentCommand,
  GetApplicationCommand,
  GetEnvironmentCommand,
  GetHostedConfigurationVersionCommand,
  GetConfigurationProfileCommand,
} from "@aws-sdk/client-appconfig";

const main = async () => {
  const appconfig = new AppConfigClient();

  // create an application
  const application = await appconfig.send(
    new GetApplicationCommand({
      ApplicationId: "u7ncvfu",
    })
  );

  // create an environment
  const environment = await appconfig.send(
    new GetEnvironmentCommand({
      ApplicationId: application.Id,
      EnvironmentId: "e4n4jtr",
    })
  );

  // create a configuration profile
  const config_profile = await appconfig.send(
    new GetConfigurationProfileCommand({
      ApplicationId: application.Id,
      ConfigurationProfileId: "wx0bar5",
    })
  );

  // create a hosted configuration version
  const hcv = await appconfig.send(
    new GetHostedConfigurationVersionCommand({
      ApplicationId: application.Id,
      ConfigurationProfileId: config_profile.Id,
      VersionNumber: 1,
    })
  );

  console.log("hcv", hcv);

  // start a deployment
  await appconfig.send(
    new StartDeploymentCommand({
      ApplicationId: application.Id,
      EnvironmentId: environment.Id,
      ConfigurationProfileId: config_profile.Id,
      ConfigurationVersion: hcv.VersionNumber?.toString(),
      DeploymentStrategyId: "AppConfig.Linear20PercentEvery6Minutes",
    })
  );
};

main();
