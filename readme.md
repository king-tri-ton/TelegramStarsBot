# TelegramStarsBot

**TelegramStarsBot** is a Telegram bot that allows users to purchase images using Telegram Stars (XTR), an internal currency. This bot demonstrates how to integrate Telegram’s internal currency into a bot and handle payments.

## Project Structure

- **bot.py**: The main file containing the bot's logic.
- **config.py**: Configuration file for storing environment variables.
- **database.py**: Module for interacting with the SQLite database.
- **.env**: File for storing environment variables (should be added to `.gitignore`).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/king-tri-ton/TelegramStarsBot
    cd TelegramStarsBot
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Rename `exmpl.env` to `.env` and add the following lines:

    ```env
    TOKEN='your_bot_token'
    DATABASE='payments.db'
    ```

## Usage

1. **Run the bot:**

    Execute the command:

    ```bash
    python bot.py
    ```

2. **Functionality:**

    - `/start`: Sends a welcome message with a button to purchase an image.
    - **"Buy Image" Button**: Sends an invoice to the user for payment.
    - **Successful Payment Handling**: After a successful payment, the bot sends the image and saves payment information to the database.
    - `/paysupport`: Informs users about the no-refund policy and provides support contact information for any questions.

## Files

- **bot.py**: Contains the core bot code, including command and payment handlers.
- **config.py**: Loads environment variables and provides them for use in other modules.
- **database.py**: Contains functions for initializing the database and saving payment information.
- **.env**: Secret data (should be created).

## Notes

- Make sure to add the `.env` file to `.gitignore` to avoid accidentally publishing sensitive information.

## License

This project is provided "as is," with no warranties. You are free to use and modify it as you see fit.