import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.screenshot import take_screenshot
from utils.logger import get_logger

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce")
])

def test_shopping_flow(setup, username, password):
    driver = setup
    log = get_logger()

    try:
        log.info("Test started")

        # LOGIN
        login = LoginPage(driver)
        login.login(username, password)
        log.info("Logged in")
        time.sleep(2)

        # ASSERT login success (URL check)
        assert "inventory" in driver.current_url
        log.info("Login assertion passed")

        # ADD TO CART
        inventory = InventoryPage(driver)
        inventory.add_item_to_cart()
        log.info("Item added")
        time.sleep(2)

        # GO TO CART
        inventory.go_to_cart()
        log.info("Navigated to cart")
        time.sleep(2)

        # ASSERT item in cart
        assert "cart" in driver.current_url
        log.info("Cart assertion passed")

        # SCREENSHOT
        take_screenshot(driver, "cart_page")

        # LOGOUT
        inventory.logout()
        log.info("Logged out")
        time.sleep(2)

        # ASSERT logout
        assert "saucedemo" in driver.current_url
        log.info("Logout assertion passed")

    except Exception as e:
        take_screenshot(driver, "failure")
        log.error(f"Test failed: {e}")
        raise