# Cookie-Clicker-Bot
This script, cookie_clicker_bot.py, automates the "Cookie Clicker" game by clicking the main cookie a user-defined number of times and purchasing upgrades as they become available. It uses Selenium to enhance gameplay efficiency, allowing for rapid cookie production with minimal effort.

How things work: 
1- Initialization: The script begins by setting up the Chrome WebDriver using Selenium and navigating to the "Cookie Clicker" game website.

2- User Input: The user is prompted to enter the number of times they want the script to click on the main cookie.

3- Loading and Setup: The script waits for the webpage to load and then clicks on the necessary buttons to start the game and select the language.

4- Cookie Clicking: Using a loop, the script clicks on the main cookie the specified number of times, rapidly generating cookies.

5- Checking for Upgrades: As cookies accumulate, the script checks periodically for any available upgrades or items to purchase, enhancing cookie production efficiency.

6- Completion: After completing the specified number of clicks, the script stops, and the browser is closed. This allows users to automate gameplay, maximizing their cookie production effortlessly.
