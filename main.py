import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def send_connection_requests(username, password, start_page, end_page, keyword):
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    time.sleep(2)
    

    # Log in to LinkedIn
   
    username_field = driver.find_element(By.XPATH, "//input[@name='session_key']")
    password_field = driver.find_element(By.XPATH, "//input[@name='session_password']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(2)

    # Add contacts based on keyword and page number

    connection_count = 0
    for page in range(int(start_page), int(end_page) + 1):
        search_url = f"https://www.linkedin.com/search/results/people/?keywords={keyword}&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}"
        driver.get(search_url)
        time.sleep(2)

        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();", send_button)
            close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(2)
            connection_count += 1
    # Close the WebDriver
    driver.quit()
    return connection_count


def submit():
    email = email_entry.get()
    password = password_entry.get()
    start_page = start_page_entry.get()
    end_page = end_page_entry.get()
    keyword = keyword_entry.get()
    
    send_connection_requests(email, password, start_page, end_page, keyword)

    messagebox.showinfo("Submission", "Connection requests sent successfully.")

# Create main window
root = tk.Tk()
root.title("LinkedIn Connect Automation")
root.geometry("400x320")

# Configure style
style = ttk.Style()
#style.configure('TButton', background='#20bebe', foreground='white')
style.configure('TLabel', background='#F0F0F0', foreground='#333333')

# Email
email_label = ttk.Label(root, text="Email:")
email_label.grid(row=1, column=1, padx=15, pady=15, sticky="e")
email_entry = ttk.Entry(root, width=40)
email_entry.grid(row=1, column=2,columnspan=3, padx=15, pady=15)

# Password
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=2, column=1, padx=5, pady=5, sticky="e")
password_entry = ttk.Entry(root, show="*", width=40)
password_entry.grid(row=2, column=2,columnspan=3, padx=15, pady=10)

# Start Page
start_page_label = ttk.Label(root, text="Start Page:")
start_page_label.grid(row=3, column=1, pady=10, sticky="e")
start_page_entry = ttk.Entry(root, width=10)
start_page_entry.grid(row=3, column=2, pady=10)

# End Page
end_page_label = ttk.Label(root, text="End Page:")
end_page_label.grid(row=3, column=3, padx=10, pady=10, sticky="e")
end_page_entry = ttk.Entry(root, width=10)
end_page_entry.grid(row=3, column=4,  pady=10)

# Keyword
keyword_label = ttk.Label(root, text="Keyword:")
keyword_label.grid(row=5, column=1, padx=5, pady=10, sticky="e")
keyword_entry = ttk.Entry(root, width=40)
keyword_entry.grid(row=5, column=2, columnspan=3,padx=5, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Connect",bg="#20bebe", fg="white",height=2, width=10, command=submit)
submit_button.grid(row=6, column=2, columnspan=3, pady=10)

dev_label = ttk.Label(root, text="Made with ❤ by Satyendra", foreground='purple', font=('Georgia', 10))


dev_label.grid(row=16, column=2, columnspan=4, pady=40, sticky="n")

# Run the main event loop
root.mainloop()