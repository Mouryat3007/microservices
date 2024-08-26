pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'  // Jenkins credential ID for Docker Hub
        DOCKER_REGISTRY = 'your_dockerhub_username'
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig-credentials' // Jenkins credential ID for Kubernetes config
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from your version control
                    checkout scm
                }
            }
        }

        stage('Build and Test User Service') {
            steps {
                dir('user-service') {
                    script {
                        // Install dependencies and run tests
                        sh 'pip install -r requirements.txt'
                        // Assuming you have tests, you would run them here
                        // sh 'pytest'
                    }
                }
            }
        }

        stage('Build and Test Product Service') {
            steps {
                dir('product-service') {
                    script {
                        // Install dependencies and run tests
                        sh 'pip install -r requirements.txt'
                        // Assuming you have tests, you would run them here
                        // sh 'pytest'
                    }
                }
            }
        }

        stage('Build and Test Order Service') {
            steps {
                dir('order-service') {
                    script {
                        // Install dependencies and run tests
                        sh 'pip install -r requirements.txt'
                        // Assuming you have tests, you would run them here
                        // sh 'pytest'
                    }
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for each service
                    sh "docker build -t ${DOCKER_REGISTRY}/user-service:latest ./user-service"
                    sh "docker build -t ${DOCKER_REGISTRY}/product-service:latest ./product-service"
                    sh "docker build -t ${DOCKER_REGISTRY}/order-service:latest ./order-service"
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    }
                    // Push Docker images
                    sh "docker push ${DOCKER_REGISTRY}/user-service:latest"
                    sh "docker push ${DOCKER_REGISTRY}/product-service:latest"
                    sh "docker push ${DOCKER_REGISTRY}/order-service:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([file(credentialsId: KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG')]) {
                        // Apply Kubernetes manifests
                        sh "kubectl apply -f k8s/user-service-deployment.yml --kubeconfig=$KUBECONFIG"
                        sh "kubectl apply -f k8s/product-service-deployment.yml --kubeconfig=$KUBECONFIG"
                        sh "kubectl apply -f k8s/order-service-deployment.yml --kubeconfig=$KUBECONFIG"
                    }
                }
            }
        }

    }

    post {
        always {
            script {
                // Clean up any Docker images created during the pipeline
                sh "docker rmi ${DOCKER_REGISTRY}/user-service:latest || true"
                sh "docker rmi ${DOCKER_REGISTRY}/product-service:latest || true"
                sh "docker rmi ${DOCKER_REGISTRY}/order-service:latest || true"
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
