# 🐳 Docker Guide for Budget Shop

This guide covers how to use Docker with the Budget Shop project for both development and production environments.

## 📋 Prerequisites

- Docker installed on your system
- Docker Compose installed
- At least 4GB of available RAM
- At least 2GB of available disk space

## 🏗️ Project Structure

```
budget-shop/
├── backend/
│   ├── Dockerfile          # Production backend image
│   ├── Dockerfile.dev      # Development backend image
│   ├── .dockerignore       # Backend Docker ignore rules
│   └── ...
├── frontend/
│   ├── Dockerfile          # Production frontend image
│   ├── Dockerfile.dev      # Development frontend image
│   ├── .dockerignore       # Frontend Docker ignore rules
│   ├── nginx.conf          # Nginx configuration
│   └── ...
├── docker-compose.yml      # Production services
├── docker-compose.dev.yml  # Development services
└── Taskfile.yml            # Task runner with Docker commands
```

## 🚀 Quick Start

### Development Environment

```bash
# Build and start development services
task docker:build:dev
task docker:up:dev

# Your services will be available at:
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
```

### Production Environment

```bash
# Build and start production services
task docker:build
task docker:up

# Your services will be available at:
# Frontend: http://localhost:80
# Backend: http://localhost:8000
```

## 🔧 Docker Commands

### Using Task (Recommended)

```bash
# Development
task docker:build:dev    # Build development images
task docker:up:dev       # Start development services
task docker:logs:dev     # View development logs
task docker:down         # Stop all services

# Production
task docker:build        # Build production images
task docker:up           # Start production services
task docker:logs         # View production logs
task docker:down         # Stop all services

# Utility
task docker:clean        # Clean up all Docker resources
```

### Using Docker Compose Directly

```bash
# Development
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d
docker-compose -f docker-compose.dev.yml logs -f
docker-compose -f docker-compose.dev.yml down

# Production
docker-compose build
docker-compose up -d
docker-compose logs -f
docker-compose down
```

## 🏭 Service Details

### Backend Service

**Development:**
- **Image**: `budget-shop-backend-dev`
- **Port**: 8000
- **Features**: Hot reload, development dependencies, volume mounting
- **Command**: `uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000`

**Production:**
- **Image**: `budget-shop-backend`
- **Port**: 8000
- **Features**: Optimized, production dependencies, health checks
- **Command**: `uv run uvicorn main:app --host 0.0.0.0 --port 8000`

### Frontend Service

**Development:**
- **Image**: `budget-shop-frontend-dev`
- **Port**: 5173
- **Features**: Hot reload, development mode, volume mounting
- **Command**: `npm run dev -- --host 0.0.0.0`

**Production:**
- **Image**: `budget-shop-frontend`
- **Port**: 80
- **Features**: Nginx server, optimized build, API proxy
- **Command**: `nginx -g 'daemon off;'`

## 🌐 Networking

### Production Network
- **Network**: `budget-shop-network`
- **Frontend**: Accessible on port 80
- **Backend**: Accessible on port 8000
- **Internal Communication**: Services communicate via service names

### Development Network
- **Network**: `budget-shop-dev-network`
- **Frontend**: Accessible on port 5173
- **Backend**: Accessible on port 8000
- **Hot Reload**: Volume mounting enables live code changes

## 📊 Health Checks

### Backend Health Check
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

### Frontend Health Check
```yaml
healthcheck:
  test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:80/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

## 🔒 Security Features

### Backend Security
- Non-root user (`app`)
- Minimal base image (Python slim)
- No unnecessary system packages
- Environment variable isolation

### Frontend Security
- Security headers in Nginx
- Content Security Policy
- XSS protection
- Frame options

## 📁 Volume Mounting

### Development Volumes
```yaml
volumes:
  - ./backend:/app              # Backend source code
  - /app/.venv                  # Backend virtual environment
  - ./frontend:/app             # Frontend source code
  - /app/node_modules           # Frontend dependencies
```

### Production Volumes
```yaml
volumes:
  - ./backend:/app              # Backend source code
  - /app/.venv                  # Backend virtual environment
```

## 🚨 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Check what's using the port
lsof -i :8000
lsof -i :80
lsof -i :5173

# Stop conflicting services or change ports in docker-compose files
```

#### Build Failures
```bash
# Clean up and rebuild
task docker:clean
task docker:build:dev

# Check Docker logs
docker-compose -f docker-compose.dev.yml logs
```

#### Service Won't Start
```bash
# Check service status
docker-compose ps

# View service logs
docker-compose logs [service-name]

# Check health status
docker-compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

#### Memory Issues
```bash
# Check Docker resource usage
docker stats

# Increase Docker memory limit in Docker Desktop settings
# Recommended: 4GB+ RAM, 2GB+ swap
```

### Debug Commands

```bash
# Enter running container
docker exec -it budget-shop-backend-dev bash
docker exec -it budget-shop-frontend-dev sh

# View container details
docker inspect budget-shop-backend-dev

# Check container logs
docker logs budget-shop-backend-dev

# Monitor resource usage
docker stats budget-shop-backend-dev budget-shop-frontend-dev
```

## 🔄 Development Workflow

### 1. Start Development Environment
```bash
task docker:up:dev
```

### 2. Make Code Changes
- Edit files in your local directory
- Changes are automatically reflected due to volume mounting

### 3. View Logs
```bash
task docker:logs:dev
```

### 4. Stop Services
```bash
task docker:down
```

### 5. Rebuild After Dependency Changes
```bash
task docker:build:dev
task docker:up:dev
```

## 🚀 Production Deployment

### 1. Build Production Images
```bash
task docker:build
```

### 2. Start Production Services
```bash
task docker:up
```

### 3. Monitor Services
```bash
task docker:logs
```

### 4. Scale Services (if needed)
```bash
docker-compose up -d --scale backend=3
```

## 📈 Performance Optimization

### Backend Optimization
- Multi-stage builds
- Minimal base images
- Dependency caching
- Health checks for load balancers

### Frontend Optimization
- Nginx with gzip compression
- Static file caching
- Optimized build process
- CDN-ready configuration

## 🔧 Customization

### Environment Variables
Create `.env` files for custom configurations:

```bash
# .env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info
```

### Port Configuration
Modify ports in docker-compose files:

```yaml
ports:
  - "3000:8000"  # Map host port 3000 to container port 8000
```

### Volume Paths
Customize volume mounting paths:

```yaml
volumes:
  - /custom/path:/app  # Mount custom host path
```

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Docker Guide](https://fastapi.tiangolo.com/deployment/docker/)
- [React Docker Guide](https://create-react-app.dev/docs/deployment/)

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. View service logs: `task docker:logs:dev`
3. Check Docker system status: `docker system df`
4. Clean up and rebuild: `task docker:clean && task docker:build:dev` 