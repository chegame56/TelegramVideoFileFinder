# Telegram Video File Finder

Welcome to the **Telegram Video File Finder**! This is a simple Python tool with a GUI that helps you forward video files from Telegram groups and channels to your **Saved Messages**. I’m a **newbie** in programming, so this project is still in its early stages and may have room for improvements.

I’d love to hear any suggestions or ideas you may have. Feel free to **fork** this repository, add features, and submit pull requests! Help me learn and make this tool better for everyone.

## Table of Contents
- [Features](#features)
- [Getting Telegram API Credentials](#getting-telegram-api-credentials)
- [Requirements](#requirements)
- [Usage](#usage)
- [Downloadable Executable](#downloadable-executable)
- [Contributions Welcome!](#contributions-welcome)
- [License](#license)

## Features
![image](https://github.com/user-attachments/assets/8cf56058-045b-4214-9041-a93ca96cfa2b)
![image](https://github.com/user-attachments/assets/1d9577e3-c416-470b-b447-1f6051812084)


- Forward video files from Telegram channels to your **Saved Messages**.
- Simple and intuitive GUI interface.
- Based on **Python** and **Telethon**.

*Note: This tool currently does not download videos; it only forwards them to your Saved Messages. However, I am working on developing a feature to download forwarded files directly into local storage.*

## Getting Telegram API Credentials

To use the Telegram Video File Finder, you’ll need to set up a Telegram API account to obtain your **API_ID** and **API_HASH**. Follow these detailed steps:

1. **Visit the Telegram API Site**  
   Go to [my.telegram.org](https://my.telegram.org/auth).

2. **Log In**  
   - Click on **Log In**.  
   - Enter your phone number in the international format (e.g., +1234567890).  
   - Click on **Next**.  
   - You will receive a confirmation code via Telegram. Enter this code to verify your login.

3. **Navigate to API Development Tools**  
   Once logged in, you will see the main dashboard.  
   - Click on **API development tools** in the menu.

4. **Create a New Application**  
   - In the API development tools section, you’ll find a form to create a new application.  
   - Fill in the **App title** (e.g., "Telegram Video Finder").  
   - For **Short name**, enter a simple, memorable name (e.g., "TVF").  
   - Select **Platform** (you can choose any option; it doesn’t impact your use of the API).  
   - Click **Create application**.

5. **Get Your API Credentials**  
   After creating the application, you will see your **API_ID** and **API_HASH** displayed on the screen.  
   - **API_ID**: This is a numeric value you'll need for the tool.  
   - **API_HASH**: This is a string value that acts as a password.

6. **Store Your Credentials Safely**  
   Make sure to keep your **API_ID** and **API_HASH** private.  
   - Avoid sharing them publicly to ensure the security of your Telegram account.

7. **Use Your Credentials**  
   You can now use your **API_ID** and **API_HASH** in the Telegram Video File Finder tool to access the Telegram API.

## Requirements
- Python 3.x
- Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Run the GUI tool:
   ```bash
   python gui_interface.py
   ```
2. Enter your **API credentials** (API_ID and API_HASH) and the Telegram group/channel details.
3. Select the videos you want to forward.
4. Click the forward button to send them to your Saved Messages.

*Example*: If you want to forward a video from the “Example Group,” just enter the group details and select the video file from the interface.

## Downloadable Executable

For users who are not developers, I've created a downloadable executable file (.exe) that you can easily run without needing to set up Python or install dependencies. 

### How to Use the Executable

1. **Download the Executable**  
   You can download the latest version of the executable from the [Releases](https://github.com/chegame56/TelegramVideoFileFinder/releases) section of this repository.

2. **Run the Executable**  
   Simply double-click the downloaded file to run the Telegram Video File Finder.

3. **Enter Your API Credentials**  
   Just like in the Python version, enter your **API_ID** and **API_HASH** when prompted, along with the Telegram group/channel details.

4. **Select and Forward Videos**  
   Choose the videos you want to forward and click the forward button to send them to your Saved Messages.

### Note for Non-Developers
If you encounter any issues while using the executable or have questions, feel free to reach out or open an issue in the repository. Your feedback is invaluable!

## Contributions Welcome!
I’m still learning, so any contributions, feedback, or feature requests are greatly appreciated. Please feel free to open an issue or submit a pull request.

## License
This project is licensed under the **MIT License**.
