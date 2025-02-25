pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = '1'
        GIT_REPO = 'git@github.com:MrShudu-LFI/MathFunctions.git'
        BRANCH = 'master'
        PYTHON_ENV = 'venv'  // Virtual environment name (if needed)
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: "${BRANCH}", credentialsId: "${GIT_CREDENTIALS_ID}", url: "${GIT_REPO}"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python3 -m venv ${PYTHON_ENV}'  // Create virtual environment (optional)
                    sh 'source ${PYTHON_ENV}/bin/activate && pip install -r requirements.txt || true' // Install dependencies if required
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'source ${PYTHON_ENV}/bin/activate && python -m pytest test_BasicFunctions.py' // Run tests
                }
            }
        }
    }
}
