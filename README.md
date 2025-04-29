# Bitcoin Analyzer

## Acknowledgment
This is my very first project through which I have taken the initial step toward transitioning from classical machine learning to large language models. I would like to thank the following individuals and organisations that made this project possible. 
* Rahul Bhandari for giving me the a-ha! moment with his Bitcoin-analyzer-with-prompts project (`https://github.com/rahul-0000-code/`) by showing me how to turn my hazy feeling about the possibility of creating a Python program only with prompt engineering techniques into a practical viability. 
* Groq for providing me free access to their API key and thereby allowing me to gain hands-on experience in making API calls without having to constantly worry about token limits.

## Abstract
The project showcases how well-crafted prompting is sufficient to build a Web app that analyses real-time historical Bitcoin prices and advises you whether or not to buy, with no need to build an Agent with heavy programming.

## Development Notes
* Streamlit made the building of a Web app simple. I could ready a Web app interface with a few lines of fairly intuitive code. 
* This is the first project in which I pulled live data using an API key. I was pleasantly surpised how uncomplicated it was. 

## Challenges
Finding a free API key was the part that took the longest while working in this project. The data on Bitcoin prices is being pulled from Coin Paprika using a free API. While I wished I could receive a 7-day backlog to date, I could only get two figures from the last 24-hour period, which was extremely liming. Increasing the volume of data that can be fed into the model will obviously improve the quality of its output. The purpose of the project, however, was to serve as a proof of concept demonstrating that prompt engineering can go a long way — and it succeeded.

# Installation
To run bitcoin_analyzer.py, do the following:

### Step 1. Place the files in a folder. 
1. Place the `.py` file in a local folder (e.g. `C:\temp\bitcoin_analyzer`).
2. Create a file called `.env` and place the GROQ API key in the following format:
	`GROQ_API_KEY = <groq_api_key>`
3. Place the `.env` file in the same local folder. 

### Step 2. Install Python. 
1. In Windows, open the Command Prompt window.
2. Make sure Python is installed. In the Command Prompt window, type:
	`python --version`
If you get an error or "Python is not recognized", you need to install Python:
	1. Go to `https://www.python.org/downloads/`.
	2. Download the latest Python installer for Windows
	3. Run the installer and make sure to check `Add Python to PATH` during installation

### Step 3. Set up a virtual environment. 
This keeps your project dependencies isolated:
1. In the Command Prompt window, go to the script folder. Type:<br>
	`cd C:\<path to your script folder>`
2. In the Command Prompt, create a Python virtual environment named `bitcoin_env`.<br>
	`python -m venv bitcoin_env`
3. In the Command Prompt, activate the Python virtual environment.<br>
	`bitcoin_env\Scripts\activate`
4. Install the required dependencies.<br>
  `pip install -r requirements.txt`

### Step 4. Run the script. 
1. In the Command Prompt window, run the Streamlit application. Type:<br>
	`streamlit run bitcoin_analyzer.py`
<br>
<br>
This will start a local web server and open the application in your browser. Press the Analyse button to view the results. 

## Web app in action
![Alt text for screen reader](https://github.com/renabracha/Bitcoin-analyzer-prompt-demo/blob/main/bitcoin_analyzer_UI.jpg?raw=true)