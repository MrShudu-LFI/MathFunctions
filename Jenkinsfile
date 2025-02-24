pipeline{
    agent any
    environment{
        GIT_CREDENTIALS_ID = '1'
        GIT_REPO = 'git@github.com:MrShudu-LFI/MathFunctions.git'
        BRANCH = 'master'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: "${BRANCH}", credentialsId: "${GIT_CREDENTIALS_ID}", url: "${GIT_REPO}"
                }
            }
        }

        stage('Build'){
            steps {
                git branch:
            }
        }

    }
}