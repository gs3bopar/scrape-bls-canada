# scrape-bls-canada

## This command will run scrape.py and write its output to output.txt. If output.txt already exists, it will be overwritten

`python scrape.py > output.txt`

## If you want to append to the file instead of overwriting it, use >>:

`python scrape.py >> output.txt`

## Notes:

1. Make sure you are using the correct version of Python. Your command might look like `python3.9 scrape.py`.
2. Make sure you are using the correct version of `chrome_driver_binary`, such as `chromedriver_linux64` for AWS Linux or `chromedriver` for macOS.
3. Update the "APPLICANT DETAILS" section with your own details.

## Comment the following code lines to use GUI

# Maybe needed in some environments where GUI is not available

`options.add_argument('--headless')  # Run Chrome in headless mode`
`options.add_argument('--disable-gpu')  # Disable GPU acceleration`

# Other optional configurations

`options.add_argument('--no-sandbox')  # May be needed in some environments`
`options.add_argument('--disable-dev-shm-usage')  # May be needed in some environments`

# Steps to run on AWS Linux

1. Start an EC2 instance (t2.nano) with AWS Amazon Linux 2.
2. Connect to the instance.
3. Install Git: `sudo yum install git`.
4. Install Python 3.9: `sudo yum install python3.9`.
5. Install pip: `sudo yum install pip`.
6. Install Selenium: `sudo pip3.9 install selenium`.
7. Install libX11: `sudo yum install -y libX11`.
8. Download and install Google Chrome: 
  - `cd /tmp`
  - `wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm`
  - `sudo yum install ./google-chrome-stable_current_x86_64.rpm`
  - `sudo ln -s /usr/bin/google-chrome-stable /usr/bin/chromium`.
9. Start a named session: `screen -S bls-scrape`.
10. Run your Python program.
11. To detach from the screen: `Ctrl+a d`.
12. To attach to the screen again: `screen -r bls-scrape`.
