pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Program Files\\Python312'
        PATH = "${PYTHON_HOME};${PATH}"
    }

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: '831267fe-b684-40dd-812d-d2dc3fa39c61', url: 'https://github.com/Saumitra-171/repo.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: '831267fe-b684-40dd-812d-d2dc3fa39c61', url: 'https://github.com/Saumitra-171/repo.git'
                bat 'python listsort.py' // Use 'python3' if necessary
            }
        }
    }
}
