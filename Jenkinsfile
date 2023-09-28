pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from version control (e.g., Git)
                checkout scm
            }
        }

        stage('Create Deployment Package') {
            steps {
                // Create a zip file of your application in the Jenkins workspace
                sh 'zip -r myapp.zip *'
            }
        }

        stage('Deploy to Elastic Beanstalk') {
            steps {
                script {
                    def elasticBeanstalkDeploy = [
                        credentialsId: 'aws cred', // AWS credentials ID configured in Jenkins
                        region: 'us-east-1', // AWS region where your Elastic Beanstalk environment is located
                        applicationName: 'python-analyzer', // Elastic Beanstalk application name
                        environmentName: 'Python-analyzer-env', // Elastic Beanstalk environment name
                        versionLabel: 'YourVersionLabel', // Unique version label for your deployment
                        description: 'Deployment from Jenkins',
                        sourceBundle: [s3Bucket: '', // Leave this empty since you're not using S3
                                      s3Key: 'myapp.zip'], // Provide the name of the zip file created in the previous stage
                        createApplicationVersion: true // Set to true to create a new application version
                    ]

                    elasticBeanstalk(deploy: elasticBeanstalkDeploy)
                }
            }
        }
    }
}
