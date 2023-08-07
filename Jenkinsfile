pipeline {
    agent any

    stage('Test') {
        steps {
            echo "Testing.."
            echo "BEGIN --------"
            pwd
            sh "python3 -m venv venv"
            sh "source venv/bin/activate"
            sh "pip install -r requirements.txt"
            sh "pytest -s -v"
            echo "END --------"

            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
        }
    }
}