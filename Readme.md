# Telegram Video Search Tool

A Python tool for searching and downloading videos from Telegram channels using the Telethon library. This tool provides a simple graphical user interface (GUI) for ease of use.

## Features

- Search for videos in specified Telegram channels.
- Download videos directly to your local machine.
- Simple and intuitive GUI using Tkinter.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configure the Telegram Client:**

   - Create a file named `config.json` in the project directory with the following structure:

     ```json
     {
       "api_id": "your_api_id",
       "api_hash": "your_api_hash",
       "phone_number": "your_phone_number"
     }
     ```

   - Replace `"your_api_id"`, `"your_api_hash"`, and `"your_phone_number"` with your actual Telegram API credentials.

2. **Run the Application:**

    ```bash
    python main.py
    ```

3. **Use the GUI to search and download videos:**

   - Follow the instructions provided in the GUI to search for videos and specify download locations.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, feel free to open an issue on GitHub or contact [your-email@example.com](mailto:your-email@example.com).

