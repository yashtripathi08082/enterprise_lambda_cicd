# Enterprise Lambda CI/CD

This project demonstrates an enterprise-level CI/CD pipeline for AWS Lambda using GitHub Actions.

enterprise-cicd/
│
├── app/
│   ├── __init__.py
│   ├── lambda_handler.py
│   ├── service.py
│   └── utils.py
│
├── tests/
│   └── test_lambda.py
│
├── scripts/
│   ├── build.sh
│   ├── package.sh
│   └── deploy.sh
│
├── requirements.txt
├── pytest.ini
├── .gitignore
├── README.md
│
└── .github/
    └── workflows/
        ├── ci.yml
        ├── deploy-dev.yml
        └── deploy-prod.yml


Phase 1: Create the project structure and Git branches.
Phase 2: Build a dedicated CI pipeline (tests, linting, packaging).
Phase 3: Deploy automatically to a Dev Lambda.
Phase 4: Add GitHub Environments with manual approval before production.
Phase 5: Replace access keys with OIDC + IAM Roles.
Phase 6: Add caching, artifacts, release versioning, and rollback.