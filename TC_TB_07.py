import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# setup logging
logging.basicConfig(
    filename="logs/TC_TB_007.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting Browser Session...")

driver = webdriver.Chrome()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 20)

# 1. Navigate to the ticket booking page
driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")
logging.info("URL Open Successfully.")

# 2. Click on the "Book Now" button.
try:
    book_now_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='calculateBooking()']")))
    book_now_button.click()
    logging.info("Click on Book Now button successfully.")

except Exception as e:
    logging.info("Element 'Book now' button not found with Explicit wait.")

# Check for Ticket ERROR
expected_ticket_error_message = "Please enter a number between 1 and 10."
actual_ticket_error_message_element =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ticketError")))
actual_ticket_error_message = actual_ticket_error_message_element.text

if expected_ticket_error_message == actual_ticket_error_message:
    logging.info("Test Passed. Expected Ticket Error match with Actual Ticket Error.")
else:
    logging.info("Test Failed. Expected Ticket Error does not match with Actual Ticket Error.")


logging.info("Script Complete.")
driver.quit()
logging.info("End Browser Session...")