pipeline {
    agent any

    stage('Test') {
        steps {
            echo "Testing.."
            echo "BEGIN --------"
            pwd
            python3 -m venv venv
            source venv/bin/activate
            pip install -r requirements.txt
            pytest -s -v
            echo "END --------"

            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
        }
    }
}