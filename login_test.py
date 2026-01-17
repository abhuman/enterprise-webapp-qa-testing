"""Login functionality test cases."""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver, test_config, test_credentials):
    """Test successful login with valid credentials."""
    logger.info("Starting test_valid_login")
    
    # Navigate to login page
    driver.get(test_config['login_url'])
    logger.info(f"Navigated to: {test_config['login_url']}")
    
    # Wait for page to load and find username field
    username_field = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Enter credentials
    username = test_credentials['valid']['username']
    password = test_credentials['valid']['password']
    
    logger.info(f"Entering username: {username}")
    username_field.send_keys(username)
    
    password_field = driver.find_element(By.ID, "password")
    logger.info("Entering password")
    password_field.send_keys(password)
    
    # Click login button
    login_button = driver.find_element(By.ID, "loginBtn")
    logger.info("Clicking login button")
    login_button.click()
    
    # Wait for dashboard to load
    WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.title_contains("Dashboard")
    )
    
    # Assertions
    assert "Dashboard" in driver.title, "Login failed - Dashboard not loaded"
    logger.info("Login successful - Dashboard loaded")
    
    # Verify URL changed to dashboard
    assert "dashboard" in driver.current_url.lower(), "URL did not change to dashboard"
    logger.info("Test passed: test_valid_login")


@pytest.mark.login
@pytest.mark.negative
def test_invalid_username(driver, test_config, test_credentials):
    """Test login with invalid username."""
    logger.info("Starting test_invalid_username")
    
    driver.get(test_config['login_url'])
    
    # Wait for username field
    username_field = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Enter invalid credentials
    invalid_username = test_credentials['invalid']['username']
    valid_password = test_credentials['valid']['password']
    
    username_field.send_keys(invalid_username)
    driver.find_element(By.ID, "password").send_keys(valid_password)
    driver.find_element(By.ID, "loginBtn").click()
    
    # Wait for error message
    error_message = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
    )
    
    # Assertions
    assert error_message.is_displayed(), "Error message not displayed"
    assert "invalid" in error_message.text.lower() or "incorrect" in error_message.text.lower()
    logger.info("Test passed: test_invalid_username")


@pytest.mark.login
@pytest.mark.negative
def test_invalid_password(driver, test_config, test_credentials):
    """Test login with invalid password."""
    logger.info("Starting test_invalid_password")
    
    driver.get(test_config['login_url'])
    
    # Wait for username field
    username_field = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # Enter credentials with invalid password
    valid_username = test_credentials['valid']['username']
    invalid_password = test_credentials['invalid']['password']
    
    username_field.send_keys(valid_username)
    driver.find_element(By.ID, "password").send_keys(invalid_password)
    driver.find_element(By.ID, "loginBtn").click()
    
    # Wait for error message
    error_message = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
    )
    
    # Assertions
    assert error_message.is_displayed(), "Error message not displayed"
    logger.info("Test passed: test_invalid_password")


@pytest.mark.login
@pytest.mark.negative
def test_empty_credentials(driver, test_config):
    """Test login with empty username and password."""
    logger.info("Starting test_empty_credentials")
    
    driver.get(test_config['login_url'])
    
    # Wait for login button and click without entering credentials
    login_button = WebDriverWait(driver, test_config['explicit_wait']).until(
        EC.element_to_be_clickable((By.ID, "loginBtn"))
    )
    login_button.click()
    
    # Check for validation message or that we're still on login page
    WebDriverWait(driver, 5).until(
        EC.url_contains("login")
    )
    
    assert "login" in driver.current_url.lower(), "Should remain on login page"
    logger.info("Test passed: test_empty_credentials")
