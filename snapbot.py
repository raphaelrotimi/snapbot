import asyncio
import random
import os
from dotenv import load_dotenv
from playwright.async_api import async_playwright
import playwright_stealth

# --- SECURE CREDENTIALS ---
load_dotenv()
USER = os.getenv("SNAP_USER")
PASS = os.getenv("SNAP_PASS")
PROXY = None 

SESSION_FILE = "session_state.json"

# This folder will store your browser profile so you only have to log in ONCE
USER_DATA_DIR = "/home/ghost/snap_profile"

async def apply_stealth(page):
    try:
        playwright_stealth.stealth_async(page)
    except:
        try:
            playwright_stealth.stealth(page)
        except:
            pass

async def add_users(context, target_list):
    page = await context.new_page()
    await apply_stealth(page)
    
    for username in target_list:
        username = username.strip()
        if not username: continue
        try:
            print(f"[*] Processing target: {username}")
            await page.goto(f"https://web.snapchat.com/search?q={username}", timeout=60000)
            await asyncio.sleep(random.uniform(5, 10))
            
            add_button = page.locator('button:has-text("Add")').first
            if await add_button.is_visible():
                await add_button.click()
                print(f"[+] Successfully added: {username}")
            else:
                print(f"[-] Could not add {username}")
                
            wait_time = random.uniform(40, 100)
            print(f"Sleeping for {wait_time:.2f}s...")
            await asyncio.sleep(wait_time)
        except Exception as e:
            print(f"[!] Error processing {username}: {e}")

async def main():
    async with async_playwright() as p:
        # Launching with a persistent context makes the bot look like a real user
        # headless=False is REQUIRED for the first login to solve CAPTCHAs/2FA
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False, 
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            proxy={"server": PROXY} if PROXY else None
        )
        
        page = context.pages[0] # Use the automatically opened page
        await apply_stealth(page)
        
        # Check if we are already logged in
        await page.goto("https://web.snapchat.com")
        await asyncio.sleep(5)
        
        if "login" in page.url or await page.locator('text=Log In').is_visible():
            print("[*] Not logged in. Navigating to login page...")
            await page.goto("https://accounts.snapchat.com/login")
            await asyncio.sleep(5)
            
            try:
                print("[*] Attempting to fill credentials...")
                # Using a more flexible selector in case the 'name' attribute changed
                await page.fill('input[type="text"], input[name="username"]', USER, timeout=10000)
                await page.fill('input[type="password"], input[name="password"]', PASS, timeout=10000)
                await page.click('button[type="submit"]')
                
                print("[!] LOGIN TRIGGERED. Please look at the browser window!")
                print("[!] If there is a CAPTCHA or 2FA, solve it MANUALLY now.")
                print("[*] Waiting for you to reach the home page...")
                
                # Wait up to 5 minutes for you to manually solve any puzzles
                await page.wait_for_url("**/home**", timeout=300000) 
                print("[+] Login successful!")
            except Exception as e:
                print(f"[!] Auto-fill failed: {e}")
                print("[!] MANUAL ACTION REQUIRED: Please log in manually in the browser window that opened.")
                print("[*] The bot will continue once you reach the home page...")
                await page.wait_for_url("**/home**", timeout=300000)
        else:
            print("[+] Already logged in via profile cookies!")

        try:
            with open("targets.txt", "r") as f:
                targets = f.readlines()
        except FileNotFoundError:
            print("[!] targets.txt not found.")
            await context.close()
            return

        await add_users(context, targets)
        await context.close()
        print("[*] Operation complete.")

if __name__ == "__main__":
    asyncio.run(main())
