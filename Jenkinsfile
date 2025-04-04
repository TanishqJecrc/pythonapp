pipeline {
    agent any
    environment {
        AZURE_CREDENTIALS_ID = 'azure-service-principal'
        RESOURCE_GROUP = 'rg-jenkins'
        APP_SERVICE_NAME = 'linapptanishq'
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/TanishqJecrc/pythonapp.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                bat 'python --version'
                bat  'python -m venv env'
                bat '.\\env\\scripts\\activate && .\\env\\scripts\\python.exe  -m pip install -r requirements.txt'
            }
        }

        stage('Package FastAPI App') {
            steps {
                bat "powershell Compress-Archive -Path ./myapp.py, ./Templates, ./requirements.txt -DestinationPath ./deploy.zip -Force"
            }
        }

        stage('Check ZIP Contents') {
            steps {
                bat 'powershell Expand-Archive -Path deploy.zip -DestinationPath temp -Force'
                bat 'cmd /c powershell -Command "Get-ChildItem -Path temp -Recurse | ForEach-Object { Write-Output $_.FullName }"'

            }
        }

        stage('Deploy') {
            steps {
                withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                    bat "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"
                    bat "az webapp deploy --resource-group $RESOURCE_GROUP --name $APP_SERVICE_NAME --src-path ./deploy.zip --type zip"
                }
            }
        }
    }
     post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
