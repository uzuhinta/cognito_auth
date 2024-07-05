import boto3

application_name = 'Application_test_name'
environment_name = 'MyTestEnvironment'
config_profile_name = 'FeatureFlagStore'

appconfigdata = boto3.client('appconfigdata')

print('appconfigdata', appconfigdata)

# start a new configuration session.
# this operation does not return configuration data.
# rather, it returns an initial configuration token that should be passed to GetLatestConfiguration.
#
# note: this operation should only be performed once (per configuration).
#   all subsequent calls to AppConfigData should be via GetLatestConfiguration.
scs = appconfigdata.start_configuration_session(
    ApplicationIdentifier=application_name,
    EnvironmentIdentifier=environment_name,
    ConfigurationProfileIdentifier=config_profile_name,
)
initial_token = scs['InitialConfigurationToken']

print('initial_token', initial_token)

# retrieve configuration data from the session.
# this operation returns your configuration data.
# each invocation of this operation returns a unique token that should be passed to the subsequent invocation.
#
# note: this operation does not always return configuration data after the first invocation.
#   data is only returned if the configuration has changed within AWS AppConfig (i.e. a deployment occurred).
#   therefore, you should cache the data returned by this call so that you can use it later.
glc = appconfigdata.get_latest_configuration(ConfigurationToken=initial_token)
config = glc['Configuration'].read()
print(config)