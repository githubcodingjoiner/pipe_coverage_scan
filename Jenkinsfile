pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Program Files\\Python313;C:\\Program Files\\Python313\\Scripts"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Coverage Installation') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip show coverage
                '''
            }
        }

        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Running tests with coverage..."
                coverage run --source=. test.py
                coverage xml -o coverage.xml
                if exist "coverage.xml" (
                    echo "Coverage report generated successfully."
                ) else (
                    echo "Error: Coverage report not found!"
                    exit /b 1
                )
                '''
            }
        }

        stage('Ensure Correct Working Directory') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Current working directory: %cd%"
                dir
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonarqube-token') // Accessing the SonarQube token
            }
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=coverage_proj1 ^
                              -Dsonar.projectName=coverage_proj1 ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.login=%SONAR_TOKEN% ^
                              -Dsonar.projectVersion=1.0.0
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
