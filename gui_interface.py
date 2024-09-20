import tkinter as tk
from tkinter import messagebox, simpledialog
from threading import Thread
import asyncio
from telegram_functions import search_videos
import os
import json
from telethon.sync import TelegramClient

CONFIG_FILE = "config.json"
api_id=''
api_hash=''
phone_number=''
client = ''




# Use a global event loop
loop = asyncio.get_event_loop()

def start_search():
    chat_id = chat_id_entry.get()
    word1 = word1_entry.get()
    word2 = word2_entry.get()
    forward_to_saved = forward_to_saved_var.get()
    limit = limit_entry.get()
    limit = int(limit) if limit.isdigit() else None
    #phone_number = phone_entry.get()

    def search_videos_thread():
        try:
            print("Starting video search...")
            # Run the search in the existing event loop
            video_messages = loop.run_until_complete(search_videos(client, phone_number, chat_id, word1, word2, limit, forward_to_saved))
            print("Video search completed.")
            update_gui_with_results(video_messages)
        except Exception as e:
            print(f"Error during search: {e}")
            update_gui_with_results([])

    def update_gui_with_results(video_messages):
        try:
            if video_messages:
                if forward_to_saved:
                    messagebox.showinfo("Success", "Videos have been forwarded to your saved messages.")
                else:
                    result_text = "\n".join([f"Found video: {file_name}" for _, file_name in video_messages])
                    messagebox.showinfo("Results", result_text)
            else:
                messagebox.showinfo("No Results", "No videos found matching the criteria.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"Error in update_gui_with_results: {e}")

    Thread(target=search_videos_thread).start()

def authenticate():
    global api_id, api_hash, client, phone_number
    print(phone_number)
    if api_id == "" or api_hash == "" or phone_number == "":
        messagebox.showerror("Error", "Please Fill your Credentials Correctly")
    elif not api_id.is_integer():
        messagebox.showerror("Error", "API ID must be a valid integer.")
    else:
        try:
            print("Authenticating...")
            client = TelegramClient('session_name', api_id, api_hash)
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(phone_number)
                otp = simpledialog.askstring("OTP Required", "Enter the OTP sent to your phone:")
                client.sign_in(phone_number, otp)

            auth_button.config(state=tk.DISABLED)
            search_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Authentication successful.")
            print("Authentication successful.")
        except Exception as e:
            messagebox.showerror("Error", f"Authentication failed: {e}")
            print(f"Error in authenticate: {e}")



def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

def set_config():
    # Assuming load_config is defined elsewhere to return a dictionary with the configuration
    config = load_config()
    global api_id, api_hash, phone_number

    # Initialize StringVar with values from config
    #api_id = tk.StringVar(value=config.get("API-ID", ""))
    api_id_var = tk.StringVar(value=config.get("API-ID", ""))
    api_hash_var = tk.StringVar(value=config.get("API-Hash", ""))
    phone_entry_var = tk.StringVar(value=config.get("Phone-Number", ""))

    # Create entries with StringVars
    phone_entry_entry = tk.Entry(root, textvariable=phone_entry_var)
    

    # Layout the entries on the window (this part may vary depending on your GUI layout)
    '''
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, phone_entry_entry.get())'''

   # Make the variables global to access them outside the function

    api_id = api_id_var.get()
    api_hash = api_hash_var.get()
    phone_number = phone_entry_entry.get()

    if not api_id.isdigit():
        print("API ID is empty. Please enter a valid API ID.")
        return  # Prevent further execution if the API ID is invalid
    else:
        try:
            # Attempt to convert to integer
            api_id = int(api_id_var.get())
            api_hash = api_hash_var.get()
            phone_number = phone_entry_entry.get()
        except ValueError:
            print(f"Invalid API ID: {api_id_var.get()}. Please enter a valid integer.")
            return  # Prevent further execution if the API ID is not a valid integer
        


        # Print for verification (optional)
        print(f"API ID: {api_id}")
        print(f"API Hash: {api_hash}")
        print(f"Phone Number: {phone_number}")


    return

def open_settings():
    config = load_config()
    global api_id, api_hash, phone_number

    # Create a new window for settings
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    
    # Ensure settings screen stays on top
    settings_window.lift()
    settings_window.attributes('-topmost', True)

    

    api_id = tk.StringVar(value=config.get("API-ID", ""))
    api_hash = tk.StringVar(value=config.get("API-Hash", ""))
    phone_number = tk.StringVar(value=config.get("Phone-Number", ""))

    def save_settings():
        global api_id, api_hash, phone_number
        config["API-ID"] = api_id.get()
        config["API-Hash"] = api_hash.get()
        config["Phone-Number"] = phone_number.get()

        api_id = int(api_id.get())
        api_hash = api_hash.get()
        phone_number = phone_number.get()
        
        
        save_config(config)
        messagebox.showinfo("Settings", "Settings saved successfully!")
        settings_window.destroy()

    tk.Label(settings_window, text="API-ID:").pack(pady=5)
    tk.Entry(settings_window, textvariable=api_id, width=10).pack(pady=5)

    tk.Label(settings_window, text="API-Hash:").pack(pady=5)
    tk.Entry(settings_window, textvariable=api_hash, width=10).pack(pady=5)

    tk.Label(settings_window, text="Phone-Number:").pack(pady=5)
    tk.Entry(settings_window, textvariable=phone_number, width=15).pack(pady=5)
    
    tk.Button(settings_window, text="Save", command=save_settings).pack(pady=20)    

root = tk.Tk()
root.title("Telegram Video Search")

tk.Label(root, text="Chat Username:").grid(row=0, column=0, padx=10, pady=5)
chat_id_entry = tk.Entry(root)
chat_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="First Word:").grid(row=1, column=0, padx=10, pady=5)
word1_entry = tk.Entry(root)
word1_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Second Word:").grid(row=2, column=0, padx=10, pady=5)
word2_entry = tk.Entry(root)
word2_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Limit (optional):").grid(row=3, column=0, padx=10, pady=5)
limit_entry = tk.Entry(root)
limit_entry.grid(row=3, column=1, padx=10, pady=5)

forward_to_saved_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Forward to Saved Messages", variable=forward_to_saved_var).grid(row=4, columnspan=2, pady=10)



auth_button = tk.Button(root, text="Authenticate", command=authenticate)
auth_button.grid(row=6, columnspan=2, pady=10)

#settings button
settings_Button = tk.Button(root, text="Settings", command=open_settings)
settings_Button.grid(row=8, columnspan=2, pady=10)

search_button = tk.Button(root, text="Start Search", state=tk.DISABLED, command=start_search)
search_button.grid(row=7, columnspan=2, pady=10)

load_and_set_config = set_config()

root.mainloop()
