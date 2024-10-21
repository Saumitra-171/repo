# repo
# Create a new pipeline in jenkins without using docker container as it may give error
# Scroll down and select pipeline script under definition
# A sample code will be generated
# Scroll down again and click pipeline syntax
# In sample step select git:Git
# In Repo Url enter the URL of the repository you want to insert it in
# Set branch to Main
# Give the credentials created in GitHub
# And then generate pipeline
# Copy the generated pipeline and return to the main tab
# Under stages create a stage called build in the following format:
stages{
      stage('Build'){
            steps{
                git branch: 'main', credentialsId: 'cf9ddf5f-447b-46a8-8c33-edbae156f8b4', url: 'https://github.com/Saumitra-171/repo.git'
                }
              }
# Again select Pipeline syntax
# In sample step select checkout
# In SCM select Git and add the URL and credentials as before
# In branch replace master with main and click generate pipeline. Copy it
# In main tab create another new stage in the following format under stages:
        stage('Checkout') {
            steps{
            checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'cf9ddf5f-447b-46a8-8c33-edbae156f8b4', url: 'https://github.com/Saumitra-171/repo.git']])
            }
        }
# Again in pipeline syntax choose bat for windows
# In batch script type python "pythonfile.py" (the file which was uploaded in github before hand and the one ypu want to process)
# Click generate and copy it
# Paste it inside Build stage after the branch line:
stage('build'){
            steps{
                git branch: 'main', credentialsId: 'cf9ddf5f-447b-46a8-8c33-edbae156f8b4', url: 'https://github.com/Saumitra-171/repo.git'
                bat 'python lisss.py'
            }
        }
# Before stages insert an environment block to specify the python path in the local machine
environment {
        PYTHON_HOME = 'C:\\Program Files\\Python312'
        PATH = "${PYTHON_HOME};${PATH}"
    }
# Click save and then Build Now
