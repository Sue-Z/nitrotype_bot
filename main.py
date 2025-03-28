from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.nitrotype.com/race")
    
    to_type = ""
    page.wait_for_selector(".dash-letter", timeout=10000)
    letters = page.locator(".dash-letter").all()
    for letter in letters:
        to_type += letter.inner_text()
    to_type = to_type.replace("\xa0", " ")

    # Wait for .dashShield to appear then go away (which is when race starts)
    page.locator(".dashShield").wait_for(timeout=10000)
    page.locator(".dashShield").wait_for(state="detached", timeout=10000)
    # If delay is not set, it seems to actually throttle it's own speed 
    page.keyboard.type(to_type, delay=1)
    
    # Stops playwright from closing window once with block is exited
    input("Press enter to terminate: ")