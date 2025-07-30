#!/bin/bash

# Deployment Script

set -e  # Exit on error

ENVIRONMENT=${1:-staging}

if [ "$ENVIRONMENT" != "staging" ] && [ "$ENVIRONMENT" != "production" ]; then
    echo "Usage: ./deploy.sh [staging|production]"
    exit 1
fi

echo "🚀 Deploying to $ENVIRONMENT..."

# Run tests first
echo "🧪 Running tests..."
./scripts/run-tests.sh

# Build Docker images
echo "
📦 Building Docker images..."
docker-compose -f docker-compose.prod.yml build

# Deploy based on environment
if [ "$ENVIRONMENT" = "production" ]; then
    echo "
🌍 Deploying to production..."
    
    # Tag images
    docker tag project-backend:latest your-registry/project-backend:latest
    docker tag project-frontend:latest your-registry/project-frontend:latest
    
    # Push to registry
    docker push your-registry/project-backend:latest
    docker push your-registry/project-frontend:latest
    
    # Update services (example for AWS ECS)
    # aws ecs update-service --cluster production --service backend --force-new-deployment
    # aws ecs update-service --cluster production --service frontend --force-new-deployment
    
    echo "✅ Production deployment complete!"
else
    echo "
🧪 Deploying to staging..."
    
    # Staging deployment logic here
    docker-compose -f docker-compose.prod.yml up -d
    
    echo "✅ Staging deployment complete!"
fi

echo "
🎉 Deployment successful!"