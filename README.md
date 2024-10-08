# Blum Collector Bot

A Python automation script designed to interact with the Telegram Desktop application. This bot automates mouse clicks based on color detection within the Telegram Desktop window, making it ideal for repetitive tasks.

## Features

- **Pixel Color Detection**: Detects specific pixel colors to trigger actions.
- **Mouse Automation**: Performs mouse clicks based on detected pixel colors.
- **Pause/Resume Functionality**: Pause or resume the bot using the spacebar on the keyboard.

## Setup

To run this script, follow these steps:

1. **Create a Folder**:
   - Create a folder on your local device.

2. **Clone the Repository**:
   - Clone the repository into the folder you created:
     ```bash
     git clone https://github.com/safi-ullah-031/blum-collector-bot.git
     ```

3. **Create a Virtual Environment**:
   - Navigate to the cloned folder and create a virtual environment:
     ```bash
     python -m venv myenv
     ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

5. **Install Dependencies**:
   - Ensure you have the required libraries installed by running:
     ```bash
     pip install -r requirements.txt
     ```

6. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python main.py
     ```
   - Follow the prompts to input the window title (e.g., "TelegramDesktop"). The bot will start automating clicks based on pixel color detection.

7. **Pause/Resume**:
   - Press the spacebar to pause or resume the bot's operation.

## Accuracy

The bot has been tested and is approximately 98% accurate in detecting the specified pixel colors and performing the required actions.

## Notes

- Ensure that the Telegram Desktop application is open and the desired bot window is visible for accurate detection.
- This script is designed to work with the Telegram Desktop application, not the web version.

## Support

For support or questions, feel free to contact me at [GitHub](https://github.com/safi-ullah-031).

## Donate

If you find this project helpful, consider supporting us by donating TON:
`UQDZcf_U8zGrOJgjNt9zSnsJjJmAgYgrWp6usxzvhgGyYger`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

