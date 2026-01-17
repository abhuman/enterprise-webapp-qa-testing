"""Pytest configuration and fixtures for test automation framework."""

import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_execution.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def test_config():
    """Load test configuration from environment variables."""
    config = {
        'base_url': os.getenv('BASE_URL', 'https://example.com'),
        'login_url': os.getenv('LOGIN_URL', 'https://example.com/login'),
        'dashboard_url': os.getenv('DASHBOARD_URL', 'https://example.com/dashboard'),
        'browser': os.getenv('BROWSER', 'chrome'),
        'headless': os.getenv('HEADLESS', 'False').lower() == 'true',
        'implicit_wait': int(os.getenv('IMPLICIT_WAIT', '10')),
        'explicit_wait': int(os.getenv('EXPLICIT_WAIT', '15')),
        'page_load_timeout': int(os.getenv('PAGE_LOAD_TIMEOUT', '30')),
        'report_dir': os.getenv('REPORT_DIR', 'reports'),
        'screenshot_dir': os.getenv('SCREENSHOT_DIR', 'screenshots')
    }
    logger.info(f"Test configuration loaded: {config}")
    return config


@pytest.fixture(scope="function")
def driver(test_config):
    """Initialize and provide WebDriver instance."""
    logger.info("Initializing WebDriver")
    
    # Configure Chrome options
    chrome_options = Options()
    
    if test_config['headless']:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Initialize driver with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Set timeouts
    driver.implicitly_wait(test_config['implicit_wait'])
    driver.set_page_load_timeout(test_config['page_load_timeout'])
    
    logger.info("WebDriver initialized successfully")
    
    yield driver
    
    # Teardown
    logger.info("Closing WebDriver")
    driver.quit()


@pytest.fixture(scope="function")
def test_credentials():
    """Provide test credentials from environment."""
    return {
        'valid': {
            'username': os.getenv('VALID_USERNAME', 'test_user'),
            'password': os.getenv('VALID_PASSWORD', 'Test@123')
        },
        'invalid': {
            'username': os.getenv('INVALID_USERNAME', 'wrong_user'),
            'password': os.getenv('INVALID_PASSWORD', 'wrong@123')
        }
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get driver from test item
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            
            # Create screenshots directory if not exists
            screenshot_dir = os.getenv('SCREENSHOT_DIR', 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Generate screenshot filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            
            # Capture screenshot
            try:
                driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot saved: {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {str(e)}")


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "smoke: Smoke test suite")
    config.addinivalue_line("markers", "regression: Regression test suite")
    config.addinivalue_line("markers", "login: Login functionality tests")
    config.addinivalue_line("markers", "dashboard: Dashboard functionality tests")
    config.addinivalue_line("markers", "ui: UI validation tests")
    config.addinivalue_line("markers", "negative: Negative test cases")
