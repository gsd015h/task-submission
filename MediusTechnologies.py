from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pathlib import Path
from PIL import Image




person_details = {"Full Name" : "John Smith", 
                  "Contact Number" : 7738854976, 
                  "Email ID" : "john.smith@gmail.com", 
                  "Full Address" : "Scholiverse Educare Pvt. Ltd. 901A/B, Iris Tech Park, Sector 48, Gurugram, Haryana, India - 122018",
                  "Pin Code" : 122018,
                  "Date of Birth" : "02/25/1995",
                  "Gender" : "Male", 
                  "Type this code" : "GNFPYC"
                  }


# Function to fill the google form 

def main():
    Full_Name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Full_Name.clear()
    Full_Name.send_keys(person_details["Full Name"])
    time.sleep(0.5)
    Contact_Number = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Contact_Number.clear()
    Contact_Number.send_keys(person_details["Contact Number"])
    time.sleep(0.5)
    Email_ID = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Email_ID.clear()
    Email_ID.send_keys(person_details["Email ID"])
    time.sleep(0.5)
    Full_Address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    Full_Address.clear()
    Full_Address.send_keys(person_details["Full Address"])
    time.sleep(0.5)
    Pin_Code = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Pin_Code.clear()
    Pin_Code.send_keys(person_details["Pin Code"])
    time.sleep(0.5)
    Date_of_Birth = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    Date_of_Birth.clear()
    Date_of_Birth.send_keys(person_details["Date of Birth"])
    time.sleep(0.5)
    Gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Gender.clear()
    Gender.send_keys(person_details["Gender"])
    time.sleep(0.5)
    Code = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Code.clear()
    Code.send_keys(person_details["Type this code"])
    time.sleep(0.5)
 
    # After fill the form take Screenshot call screen_short() function
    screen_short()
    time.sleep(2)
    
# Function to get the screenshot of the form

def screen_short():
    # Get the full height of the page
    full_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    viewport_width = driver.execute_script("return window.innerWidth")

    # Create a list to store screenshot paths
    screenshot_paths = []

    # Scroll and capture screenshots
    scroll_position = 0
    while scroll_position < full_height:
        # Scroll to the current position
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(1)  # Allow time for rendering

        # Capture the current viewport screenshot
        screenshot_path = f"screenshot_{scroll_position}.png"
        driver.save_screenshot(screenshot_path)
        screenshot_paths.append(screenshot_path)

        # Increment scroll position
        scroll_position += viewport_height

    # Stitch the screenshots together
    images = [Image.open(path) for path in screenshot_paths]
    total_width, _ = images[0].size

    # Create a blank canvas for the full image
    stitched_image = Image.new("RGB", (total_width, full_height))

    # Paste each image into the canvas
    current_height = 0
    for img in images:
        stitched_image.paste(img, (0, current_height))
        current_height += img.height

    # Save the final stitched image
    stitched_image_path = "full_page_screenshot_chrome.png"
    stitched_image.save(stitched_image_path)
    print(f"Full-page screenshot saved at: {stitched_image_path}")

    # Clean up intermediate screenshots
    for path in screenshot_paths:
        import os
        os.remove(path)

    # submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    # time.sleep(2)
    # submit_button.click()




if __name__ == "__main__":
    driver = webdriver.Chrome()
    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
    driver.get(form_url)
        
    # Wait for the form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'form'))
    )

    main()
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    time.sleep(2)
    submit_button.click()

    driver.close()

