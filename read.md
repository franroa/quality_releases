Run the script terraform_azure_backend.sh

In Pipelines:
- You can upload a public key in the pipeline's library which will be downloaded by the pipeline in the step "Download Public SSH Key"
- install environment
- install vm for the environment
- install the agent for the pipeline https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=browser
# TODO 
Use environment variables instead of the terraform varibles for tenant id, subscription and api key

In the first run (when terraform is applied the first time) the
second job will fail cause azure needs some time to configure the WebApp


Configure apache jmeter for reporting:
in ~/apache-jmeter-5.3/bin/reportgenerator.properties follow:
https://jmeter.apache.org/usermanual/generating-dashboard.html


#7 Point
For the seventh point you need to send your WebApp logs to Azure Analytics (see Diagnostic setting and https://knowledge.udacity.com/questions/294963)
The idea is that Azure will parse the logs set up on your agent in the path you have
define in "collection paths"
https://techcommunity.microsoft.com/t5/azure-monitor/azure-not-collecting-custom-log-data/m-p/631780
https://techcommunity.microsoft.com/t5/azure-sentinel/ingestion-of-custom-logs-of-files-never-updated-in-azure/m-p/1849856
#IMPORTANT TO POINT 7: 
When you create a file to be collected by azure, all the logs that exist in that file will not be collected. Azure only 
collects after having registered the file


#NOTE
take a look to the terraform.tfvars and the values set to "xxxxxx"