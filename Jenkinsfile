pipeline {
    agent any
    environment {
        HOST = ""
        USER_EMAIL = ""
        USER_PASSWORD = ""
        CLOSE_BROWSER = "true"
        DEBUG = "true"
        DISPLAY = ':99'
    }
    stages {
        stage('Clean up'){
            steps {
                cleanWs()
            }
        }
        stage('Clone repo'){
            steps {
                sh 'git clone https://github.com/romanbarabash/pytest_wix.git'
            }
        }
        stage('Build'){
            steps {
                dir('pytest_wix') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests'){
            steps {
                dir('pytest_wix') {
                    sh 'pytest --tb=auto tests --alluredir ./allure-results'
                    sh 'allure generate allure-results --clean'
                }
            }
        }
    }
    post {
        always {
            script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'pytest_wix/allure-results']]
                ])
            }
        }
    }
}