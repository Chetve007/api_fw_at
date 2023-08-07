pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh '''#!/bin/bash

                echo "Testing.."
                echo "BEGIN --------"
                sh "pwd"
                sh "python3 -m venv venv"
                sh "source venv/bin/activate"
                sh "pip install -r requirements.txt"
                sh "pytest -s -v"
                echo "END --------"
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                '''
            }
        }
    }
}