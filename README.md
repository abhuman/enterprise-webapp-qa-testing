# Enterprise Web Application – Quality Assurance & Testing

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Chrome browser (latest version)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/abhuman/enterprise-webapp-qa-testing.git
cd enterprise-webapp-qa-testing
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
# Copy the template
cp .env.example .env

# Edit .env file with your actual test credentials and URLs
```

## 📋 Running Tests

### Run all tests
```bash
pytest
```

### Run with specific markers
```bash
# Smoke tests only
pytest -m smoke

# Login tests only
pytest -m login

# Negative test cases
pytest -m negative

# Regression suite
pytest -m regression
```

### Run with HTML report
```bash
pytest --html=reports/test_report.html --self-contained-html
```

### Run with coverage
```bash
pytest --cov=. --cov-report=html
```

### Run specific test file
```bash
pytest login_test.py
```

### Run in parallel (faster execution)
```bash
pytest -n auto
```

## 🏗️ Project Structure

```
enterprise-webapp-qa-testing/
├── .env.example              # Environment variables template
├── .gitignore               # Git ignore rules
├── conftest.py              # Pytest fixtures and configuration
├── pytest.ini               # Pytest settings
├── requirements.txt         # Python dependencies
├── login_test.py           # Login functionality tests
├── README.md               # This file
├── LICENSE                 # MIT License
├── Test_Plan.md           # Test planning document
├── Test_Scenarios.md      # Test scenarios
├── Login_Test_Cases.md    # Login test cases documentation
├── Test_Data.md           # Test data specifications
├── Bug_Report.md          # Bug report template
└── Test_Summary_Report.md # Test execution summary
```

## 🔧 Configuration

### Environment Variables (.env)
Configure the following in your `.env` file:

```env
# Application URLs
BASE_URL=https://your-app.com
LOGIN_URL=https://your-app.com/login
DASHBOARD_URL=https://your-app.com/dashboard

# Test Credentials
VALID_USERNAME=your_test_user
VALID_PASSWORD=your_test_password

# Browser Settings
BROWSER=chrome
HEADLESS=False

# Timeouts (in seconds)
IMPLICIT_WAIT=10
EXPLICIT_WAIT=15
PAGE_LOAD_TIMEOUT=30
```

## 📊 Test Reports

After running tests, reports are generated in:
- **HTML Report**: `reports/test_report.html`
- **Coverage Report**: `reports/coverage/index.html`
- **Screenshots** (on failure): `screenshots/`
- **Logs**: `test_execution.log`

## 🎯 Key Features

### Automation Framework
- ✅ **Pytest-based** test framework
- ✅ **Page Object Model** ready structure
- ✅ **Fixtures** for driver and configuration management
- ✅ **WebDriverManager** for automatic ChromeDriver setup
- ✅ **Environment-based** configuration
- ✅ **Automatic screenshots** on test failure
- ✅ **Comprehensive logging** for debugging
- ✅ **HTML & Coverage reports**
- ✅ **Parallel execution** support
- ✅ **Custom pytest markers** for test categorization

### Security
- ✅ No hardcoded credentials
- ✅ Environment variable management
- ✅ `.env` file in `.gitignore`

### Code Quality
- ✅ Explicit waits (no time.sleep)
- ✅ Proper error handling
- ✅ Logging for all test actions
- ✅ Clear assertions with error messages

## 🛠️ Development

### Adding New Tests
1. Create test file following naming convention: `test_*.py`
2. Use pytest fixtures from `conftest.py`
3. Add appropriate markers: `@pytest.mark.smoke`, `@pytest.mark.regression`
4. Follow existing test structure

### Custom Markers
Available markers in `pytest.ini`:
- `@pytest.mark.smoke` - Critical functionality tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.login` - Login tests
- `@pytest.mark.dashboard` - Dashboard tests
- `@pytest.mark.ui` - UI validation tests
- `@pytest.mark.negative` - Negative scenarios

## 📝 Documentation

This repository includes comprehensive QA documentation:
- **Test Plan**: Overall testing strategy and approach
- **Test Scenarios**: High-level test scenarios
- **Test Cases**: Detailed test case specifications
- **Test Data**: Test data requirements
- **Bug Reports**: Defect documentation template
- **Test Summary**: Execution results and metrics

## 🤝 Contributing

This is a portfolio project. For suggestions or improvements, please open an issue.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Abir Roy**
- GitHub: [@abhuman](https://github.com/abhuman)
- Role: Software Tester / QA Engineer

## 🙏 Acknowledgments

- Built with Selenium and Pytest
- Follows industry best practices for test automation
- Demonstrates professional QA engineering skills

---

**Note**: This repository showcases QA automation skills and best practices. Application details are intentionally generic to maintain client confidentiality.

## Role: Software Tester / QA Engineer

This repository documents my hands-on Quality Assurance work performed on an enterprise-grade web application in a simulated client environment.

## Application Overview
A role-based, client-facing web application used for authentication, dashboard access, form submissions, and data validation.

> Note: Application name and business details are intentionally omitted to maintain confidentiality.

## QA Responsibilities
- Analyzed functional requirements and acceptance criteria
- Designed test plans, test cases, and test scenarios
- Executed manual, front-end, functional, and regression testing
- Logged defects with clear reproduction steps and severity
- Prepared QA reports and validated fixes before release
- Supported automation testing for regression scenarios

## Testing Scope
- Login & Authentication
- Dashboard & Navigation
- Form Validation & Error Handling
- UI & Front-End Validation

## Tools & Technologies
- Manual Testing
- Selenium (Python) – Automation Support
- HTML, CSS (Front-End Validation)
- REST APIs (Basic Validation)
- Git & GitHub

## Deliverables
- Test Plan
- Test Scenarios
- Test Cases
- Test Data
- Bug Reports
- Test Summary Report
