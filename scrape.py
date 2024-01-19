from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException
import pathlib

from datetime import datetime
from time import sleep
import random

success_in_finding_activeClass = False

def tryToBookApointment():
  global success_in_finding_activeClass
  # open chrome window
  current_path = str(pathlib.Path(__file__).parent.resolve())
  chrome_driver_binary = current_path + "/chromedriver"
  service = Service(executable_path=chrome_driver_binary)
  options = webdriver.ChromeOptions()
  #options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

  # Maybe needed in some environments where GUI is not available
  options.add_argument('--headless')  # Run Chrome in headless mode
  options.add_argument('--disable-gpu')  # Disable GPU acceleration

  # Other optional configurations
  options.add_argument('--no-sandbox')  # May be needed in some environments
  options.add_argument('--disable-dev-shm-usage')  # May be needed in some environments

  driver = webdriver.Chrome(service=service, options=options)

  # open url source
  driver.get("https://www.blsindia-canada.com/appointmentbls/appointment.php")

  # sleep here
  sleep(random.uniform(4.02,8.05))

  #input center location and service type
  enterCenterLocation = driver.find_element("id", "location")
  enterCenterLocation.send_keys("Toronto")

  # sleep here
  sleep(random.uniform(2.01,4.09))
  
  enterServiceType = driver.find_element("id", "service_type")
  enterServiceType.send_keys("Passport")

  # sleep here
  sleep(random.uniform(1.03,3.06))

  # perform on click on Appointment date
  driver.find_element("id", "app_date").click()

  # sleep here
  sleep(random.uniform(4.02,8.05))

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
        sleep(random.uniform(2.01,3.03))

        # perform on click on Appointment date
        enterAppointmentSlot = driver.find_element("id", "app_slot")
        drop = Select(enterAppointmentSlot)
        # Select by index
        drop.select_by_index(1)

        # sleep here
        sleep(random.uniform(3.01,4.03))

        driver.find_element("id", "name").send_keys("Gurkaran Singh Boparai")
        sleep(random.uniform(1.04,2.08))
        driver.find_element("id", "phone").send_keys("5197814392")
        sleep(random.uniform(2.0,3.08))
        driver.find_element("id", "passport_no").send_keys("M0147445")
        sleep(random.uniform(1.5,3.1))
        driver.find_element("id", "email").send_keys("gurkaransingh10@gmail.com")
        sleep(random.uniform(0.8,2.02))
        driver.find_element("id", "service").send_keys("I need to renew my passport. Thankyou!")
        sleep(random.uniform(2.34,4.32))
        
        success_in_finding_activeClass = True
        break
      except NoSuchElementException:
        active_td = None

  if (success_in_finding_activeClass == False):
    print("No Appointment available.")
  else :
    print("Your Appointment is booked")


print("Starting to book appointment")
times = 0
while success_in_finding_activeClass == False:
  times += 1
  print("Attempt #", times)
  print("Current date and time: ", datetime.now())
  tryToBookApointment()
  if success_in_finding_activeClass == False:
    # sleep here
    trying_in = random.uniform(150.13,1000.99)
    print("Trying again in", trying_in / 60, "minutes")
    sleep(trying_in)
    times += 1
  else:
    print("Finished!")
    break
  