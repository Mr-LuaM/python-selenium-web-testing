from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url = "https://www.saucedemo.com/"


def capture_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")
    print(f"Screenshot captured for step: {step_name}")


def test_login():
    driver.get(base_url)
    print("Navigated to Sauce Demo website")
    time.sleep(2)

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    print("Entered valid login credentials")
    time.sleep(2)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Clicked login button")
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("Login successful")
    capture_screenshot("login_success")


def test_invalid_login():
    driver.get(base_url)
    print("Navigated to Sauce Demo website")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("invalid_user")
    password.send_keys("wrong_password")
    print("Entered invalid login credentials")
    time.sleep(2)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Clicked login button")
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error_message, "Invalid login test failed!"
    print("Invalid login test passed")
    capture_screenshot("invalid_login")


def test_sort_products():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("Inventory page loaded successfully")
    time.sleep(2)

    sort_options = {
        "Name (A to Z)": "//*[@id='header_container']/div[2]/div/span/select/option[1]",
        "Name (Z to A)": "//*[@id='header_container']/div[2]/div/span/select/option[2]",
        "Price (low to high)": "//*[@id='header_container']/div[2]/div/span/select/option[3]",
        "Price (high to low)": "//*[@id='header_container']/div[2]/div/span/select/option[4]",
    }

    for sort_name, xpath in sort_options.items():
        sort_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
        )
        sort_dropdown.click()
        print("Dropdown expanded")
        time.sleep(2)

        sort_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        sort_option.click()
        print(f"Selected '{sort_name}' option")
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "inventory_item_price"),
                "$"
            )
        )
        print(f"Sorting applied successfully for '{sort_name}'")

        if "Name" in sort_name:
            product_names = [
                item.text
                for item in driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            ]
            print(f"Extracted product names for '{sort_name}':", product_names)
            if "A to Z" in sort_name:
                assert product_names == sorted(product_names), f"Products are not sorted by {sort_name}!"
            else:
                assert product_names == sorted(product_names, reverse=True), f"Products are not sorted by {sort_name}!"
        elif "Price" in sort_name:
            prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            price_values = [float(price.text.replace("$", "")) for price in prices]
            print(f"Extracted prices for '{sort_name}':", price_values)
            if "low to high" in sort_name:
                assert price_values == sorted(price_values), f"Products are not sorted by {sort_name}!"
            else:
                assert price_values == sorted(price_values, reverse=True), f"Products are not sorted by {sort_name}!"

        print(f"Sorting validation passed for '{sort_name}'")
        capture_screenshot(f"sorted_{sort_name.replace(' ', '_')}")
        time.sleep(2)

def test_add_products_to_cart():
    time.sleep(2)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
    )
    add_button.click()
    print("Added first product to cart")
    time.sleep(2)

    second_add_button = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")[1]
    second_add_button.click()
    print("Added second product to cart")
    time.sleep(2)
    capture_screenshot("cart_products_added")


def test_validate_cart():
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    print("Opened cart")
    time.sleep(2)

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    print(f"Number of items in cart: {len(cart_items)}")
    assert len(cart_items) == 2, "Cart validation failed!"
    time.sleep(2)
    capture_screenshot("cart_validation")


def test_remove_product_from_cart():
    remove_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")
    remove_button.click()
    print("Removed product from cart")
    time.sleep(2)

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, "Cart validation failed after removal!"
    print("Cart validation passed after product removal")
    capture_screenshot("product_removed")


def test_checkout():
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    print("Proceeded to checkout")
    time.sleep(2)

    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")
    first_name.send_keys("Mark")
    last_name.send_keys("Lua")
    postal_code.send_keys("12345")
    print("Entered checkout information")
    time.sleep(2)

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    print("Proceeded to next checkout step")
    time.sleep(2)

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    print("Order completed successfully!")
    capture_screenshot("order_completed")
    time.sleep(2)


def test_responsive_design():
    resolutions = [
        (1920, 1080),  
        (768, 1024),   
        (375, 667)     
    ]

    for width, height in resolutions:
        driver.set_window_size(width, height)
        print(f"Testing at resolution: {width}x{height}")
        time.sleep(3)
        capture_screenshot(f"resolution_{width}x{height}")


try:
    print("Starting tests...")
    driver.maximize_window()
    test_invalid_login()
    test_login()
    test_sort_products()
    test_add_products_to_cart()
    test_validate_cart()
    test_remove_product_from_cart()
    test_checkout()
    test_responsive_design()
finally:
    print("Closing browser...")
    driver.quit()
