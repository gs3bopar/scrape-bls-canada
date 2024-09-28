import pathlib
import random
import time
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

success_in_finding_activeClass = False


# Function to handle popup
def handle_popup(driver, timeout=5):
    try:
        # Wait for the popup to be present
        popup = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bloggerform"))
        )

        # Check if the popup is displayed
        if popup.is_displayed():
            close_button = popup.find_element(By.CLASS_NAME, "cl")
            close_button.click()
            print("Popup was found and closed.")
            return True
        else:
            print("Popup was found but not displayed.")
            return False
    except TimeoutException:
        print("No popup appeared within the timeout period.")
        return False
    except NoSuchElementException:
        print("Popup or close button not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while handling popup: {e}")
        return False


def retry_on_exception(func, max_attempts=2, delay=5):
    for attempt in range(max_attempts):
        try:
            return func()
        except WebDriverException as e:
            if attempt == max_attempts - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Increase delay for next attempt


def tryToBookApointment(location):
    try:
        global success_in_finding_activeClass
        # open chrome window
        current_path = str(pathlib.Path(__file__).parent.resolve())
        chrome_driver_binary = current_path + "/chromedriver_linux64"
        service = Service(executable_path=chrome_driver_binary)
        options = webdriver.ChromeOptions()
        # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        # Maybe needed in some environments where GUI is not available
        options.add_argument("--headless")  # Run Chrome in headless mode
        options.add_argument("--disable-gpu")  # Disable GPU acceleration

        # Other optional configurations
        options.add_argument("--no-sandbox")  # May be needed in some environments
        options.add_argument(
            "--disable-dev-shm-usage"
        )  # May be needed in some environments

        driver = webdriver.Chrome(service=service, options=options)

        # open url source
        driver.get("https://www.blsindia-canada.com/appointmentbls/appointment.php")

        # sleep here
        sleep(random.uniform(4.02, 8.05))

        # input center location and service type
        enterCenterLocation = driver.find_element("id", "location")
        enterCenterLocation.send_keys(location)

        # sleep here
        sleep(random.uniform(2.01, 4.09))

        # Close the popup if it appears
        handle_popup(driver)

        enterServiceType = driver.find_element("id", "service_type")
        enterServiceType.send_keys("Passport")

        # sleep here
        sleep(random.uniform(1.03, 3.06))

        # perform on click on Appointment date
        driver.find_element("id", "app_date").click()

        # sleep here
        sleep(random.uniform(4.02, 8.05))

        # Find the table with class "table-condensed" within the datepicker div
        table_element = driver.find_element(By.CLASS_NAME, "table-condensed")
        # print("Found table_element div:", table_element.text)

        tbody_element = table_element.find_elements(By.TAG_NAME, "tbody")
        # print("Found tbody_element:", tbody_element)

        # Iterate through each row and check for <td> with class "activeClass"
        for tr in tbody_element:
            if success_in_finding_activeClass:
                break
            td_rows = tr.find_elements(By.TAG_NAME, "td")
            for td in td_rows:
                try:
                    active_td = td.find_element(By.XPATH, "//td[@title='Book']")
                    # Try to book an appointment
                    # print("Found activeClass in this row:", active_td.text)
                    active_td.click()

                    # sleep here
                    sleep(random.uniform(2.01, 3.03))

                    # Close the popup if it appears
                    handle_popup(driver)

                    # sleep here
                    sleep(random.uniform(1.56, 2.63))

                    # perform on click on Appointment date
                    enterAppointmentSlot = driver.find_element("id", "app_slot")
                    drop = Select(enterAppointmentSlot)
                    # Select by index
                    drop.select_by_index(1)

                    # sleep here
                    sleep(random.uniform(3.01, 4.03))

                    # APPLICANT DETAILS
                    driver.find_element("id", "name").send_keys("")
                    sleep(random.uniform(1.04, 2.08))
                    driver.find_element("id", "phone").send_keys("")
                    sleep(random.uniform(2.0, 3.08))
                    driver.find_element("id", "passport_no").send_keys("")
                    sleep(random.uniform(1.5, 3.1))
                    driver.find_element("id", "email").send_keys("")
                    sleep(random.uniform(0.8, 2.02))
                    driver.find_element("id", "service").send_keys("")
                    sleep(random.uniform(2.34, 4.32))

                    driver.find_element(By.XPATH, "//input[@type='submit']").click()

                    sleep(random.uniform(7.50, 8.11))

                    # On success fetch following details and print them to screen
                    # Applicant Name
                    # Reference Number
                    # Passport Number
                    # Appointment date & time
                    # Application Type
                    # Find the table which shows Applicant Details within the datepicker div
                    table_element_applicant = driver.find_element(
                        By.CLASS_NAME, "borderAll table"
                    )
                    print("Details: ", table_element_applicant.text)

                    sleep(random.uniform(2.43, 3.11))

                    link = driver.find_elements(
                        By.XPATH, "//a[@class='btn secondry-btn']"
                    )[1]
                    # Click the link
                    link.click()

                    # Need to sleep here as email is sent and might take time to receive
                    sleep(random.uniform(4.67, 5.78))

                    success_in_finding_activeClass = True
                    break
                except NoSuchElementException:
                    active_td = None

        if success_in_finding_activeClass == False:
            print("No Appointment available.")
        else:
            print("Your Appointment is booked")

    except Exception as e:
        print("Error: ", e)
        print("Failed to book appointment, will try again!")


print("Starting to book appointment")
times = 0
locations = ["Brampton", "Mississauga", "Toronto"]
while success_in_finding_activeClass == False:
    times += 1
    print("Attempt #", times)
    print("Current date and time: ", datetime.now())
    randomLocation = random.choice(locations)
    print("Trying to book appointment at: ", randomLocation)
    retry_on_exception(lambda: tryToBookApointment(randomLocation))
    if success_in_finding_activeClass == False:
        # sleep here
        trying_in = random.uniform(91.13, 496.99)
        print("Trying again in", trying_in / 60, "minutes")
        sleep(trying_in)
    else:
        print("Finished!")
        break
