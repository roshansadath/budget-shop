# Budget Shop

A full-stack web application for budget management and shopping.

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.13+ (for backend)
- uv (for backend dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd budget-shop
   ```

2. **Setup the complete project (including Git hooks)**
   ```bash
   task setup:complete
   ```
OR WHAT

3. **Or setup step by step:**
   ```bash
   task install              # Install dependencies
   task setup:hooks          # Setup Git hooks
   task lint:fix             # Fix code formatting
   task type-check           # Verify types
   ```

## 🏗️ Project Structure

```
budget-shop/
├── frontend/                 # React + TypeScript frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── features/        # Feature-based modules
│   │   ├── pages/          # Page components
│   │   ├── app/            # App configuration
│   │   ├── services/       # API services
│   │   ├── utils/          # Utility functions
│   │   ├── hooks/          # Custom React hooks
│   │   ├── types/          # TypeScript type definitions
│   │   ├── styles/         # CSS/SCSS files
│   │   └── assets/         # Static assets
│   ├── package.json
│   └── tsconfig.json
├── backend/                  # FastAPI backend
│   ├── api/                 # API endpoints
│   ├── models/              # Data models
│   ├── db/                  # Database configuration
│   ├── services/            # Business logic
│   ├── utils/               # Utility functions
│   ├── core/                # Core configuration
│   ├── tests/               # Test files
│   ├── pyproject.toml       # Project configuration
│   └── uv.lock              # Dependency lock file
└── .github/                  # GitHub configuration
    ├── workflows/           # CI/CD pipelines
    ├── ISSUE_TEMPLATE/      # Issue templates
    └── pull_request_template.md
└── .githooks/               # Git hooks for branch protection
    └── pre-push            # Prevents direct pushes to protected branches

## 🌿 Branching Strategy

### Protected Branches
- `main` - Production-ready code (requires PR)
- `develop` - Development integration branch (requires PR)

### Development Workflow
1. **Create feature branch** from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and commit**:
   ```bash
   git add .
   git commit -m "feat(frontend): add budget tracking component"
   ```

3. **Push to feature branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create pull request** to merge into `develop`

5. **After review and approval**, merge via GitHub

### ⚠️ Important Notes
- **Direct pushes to `main` and `develop` are blocked by Git hooks**
- All changes must go through pull requests
- Ensure CI checks pass before merging
- Use conventional commit messages (see Contributing section)

## 🚀 Development

### Frontend Development

```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
npm run type-check   # Run TypeScript check
npm run format       # Format with Prettier
```

### Backend Development

```bash
cd backend
uv run uvicorn main:app --reload  # Start development server
uv run flake8 .                    # Run Flake8 linting
uv run black .                     # Format with Black
uv run mypy .                      # Type checking with mypy
uv run pytest                      # Run tests
```

### Combined Development

```bash
# Using Task (recommended)
task dev            # Start both frontend and backend
task dev:frontend   # Start only frontend
task dev:backend    # Start only backend

# Setup Git hooks (one-time setup)
task setup:hooks    # Configure branch protection hooks

# Using npm scripts
npm run dev         # Start frontend
# In another terminal:
cd backend && uv run uvicorn main:app --reload
```

## 🐳 Docker Development

### Using Docker for Development

```bash
# Build and start development services
task docker:build:dev
task docker:up:dev

# View development logs
task docker:logs:dev

# Stop development services
task docker:down
```

### Using Docker for Production

```bash
# Build and start production services
task docker:build
task docker:up

# View production logs
task docker:logs

# Stop production services
task docker:down
```

### Docker Commands

```bash
# Build images
task docker:build        # Production
task docker:build:dev    # Development

# Start services
task docker:up           # Production
task docker:up:dev       # Development

# Stop services
task docker:down

# View logs
task docker:logs         # Production
task docker:logs:dev     # Development

# Clean up
task docker:clean
```

## 🧪 Testing

### Test Git Hooks

To verify your hooks are working:

```bash
# Try to push to develop (should be blocked)
git checkout develop
git push origin develop

# You should see an error message and the push should be blocked
```

### Frontend Testing

### Frontend Testing
```bash
cd frontend
npm test            # Run tests
npm run test:watch  # Run tests in watch mode
```

### Backend Testing
```bash
cd backend
uv run pytest              # Run tests
uv run pytest --cov=.      # Run tests with coverage
```

## 🔧 Code Quality

### Linting & Formatting

**Frontend:**
- ESLint for JavaScript/TypeScript linting
- Prettier for code formatting
- TypeScript for type checking

**Backend:**
- Flake8 for Python linting
- Black for code formatting
- mypy for type checking

### Running Quality Checks

```bash
# Frontend
task frontend:lint
task frontend:format
task frontend:type-check

# Backend
task backend:lint
task backend:format
task backend:type-check

# Both
task lint
task format
task type-check
```

## 🚀 CI/CD

The project uses GitHub Actions for continuous integration:

- **Frontend**: ESLint, TypeScript, Prettier checks
- **Backend**: Flake8, Black, mypy checks
- **Automated**: Runs on push to main/develop and pull requests

## 📝 Contributing

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
**Scope:** `frontend`, `backend`, `api`, `ui`, etc.

### Pull Request Process

1. Create a feature branch from `develop`
2. Make your changes
3. Run quality checks: `task lint && task type-check`
4. Submit a pull request
5. Ensure CI checks pass
6. Get code review approval

## 📚 Available Tasks

Run `task --list-all` to see all available tasks:

- **Setup**: `setup:complete`, `setup:hooks`, `install`
- **Development**: `dev`, `dev:frontend`, `dev:backend`
- **Quality**: `lint`, `format`, `type-check`
- **Testing**: `test`, `test:cov`
- **Build**: `build`
- **Cleanup**: `clean`, `clean:all`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
