# 📝 Meeting Minutes Generator
This Python application automates the process of generating meeting minutes from an audio recording. It uses the Whisper library for transcription and the OpenAI GPT models for summarizing content, then outputs the result in a Word document.

## Key Features
- **Audio File Check**: Ensures the presence of an MP3 audio file before processing.
- **Audio Transcription**: Uses Whisper to accurately transcribe audio.
- **Customizable Summary Generation**: Leverages OpenAI’s GPT models to generate summaries, with the ability to customize the summary prompt based on user preferences.
- **Document Output**: Automatically saves the summary in a Word document format.

## Prerequisites
- Python 3.8 or higher
- Required packages: `whisper`, `openai`, `python-docx`

## Setup

### 1. Clone the Repository
To get started, clone the repository to your local machine using the command line:

   ```bash
   git clone https://github.com/Op27/meeting_minutes_generator.git
   ```

This will create a directory named `meeting_minutes_generator` which contains all the project files.

### 2. Navigate to the Project Directory
After cloning, move into the project directory with:

   ```bash
   cd meeting_minutes_generator
   ```

### 3. Install Dependencies
Install the necessary Python libraries using pip:

   ```bash
   pip install whisper openai python-docx
   ```

## Usage
### Setting Up the Environment
- Place your MP3 audio file in the root directory of the project.
- Set your OpenAI API key in the script.
- Update the `prompt.txt` file to define the design and style of your meeting minutes. This customization allows the summary generation to align with specific formatting or thematic preferences.

### Running the Application
Execute the script by running:

   ```bash
   python main.py
   ```

### Customizing the Summary Prompt
The application allows for customization of the summary prompt to cater to specific user needs. This feature enables users to influence the style and focus of the generated summaries, making the tool adaptable for different types of meetings.

## License
This project is open-sourced under the MIT License. You can view the full license text [here](https://opensource.org/licenses/MIT).

## Contribution
Contributions are welcome! If you'd like to improve the application or suggest features:
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes.
4. Submit a pull request.
