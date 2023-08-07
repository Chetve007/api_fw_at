pipeline {
    agent any

    stages {
        stage('Preparing') {
            steps {
                echo "Testing.."
                echo "BEGIN --------"
                sh "pwd"
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash

                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                pytest -s -v
                '''
            }
        }
        stage('Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure_report']]
                    ])
                }
            }
        }
        stage('Ending') {
            steps {
                echo "END --------"
            }
        }
    }
}
