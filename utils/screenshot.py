import os

def take_screenshot(driver, name):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    driver.save_screenshot(f"{folder}/{name}.png")