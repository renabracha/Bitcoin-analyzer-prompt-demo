# Bitcoin Analyzer

This is a little demonstration that prompting is enough to build a Web app that analyses real-time historical Bitcoin prices and advises you whether or not to buy, with no need to build an Agent with heavy programming. 

The data on Bitcoin prices is being pulled from Coin Paprika using a free API. This extremely limits the volume of data that I am able to obtain. Increasing the volume of data that can be fed into the model will obviously improve the quality of its output. Again, this is only a demonstration for the power of prompting. 


To run bitcoin_analyzer.py, do the following:

### Step 1. Place the files in a folder. 
1. Place the .py file in a local folder (e.g. C:\temp\bitcoin_analyzer).
2. Create a file called ".env" and place the GROQ API key in the following format:
	GROQ_API_KEY = <groq_api_key>
3. Place the .env file in the same local folder. 

### Step 2. Install Python. 
1. In Windows, open the Command Prompt window.
2. Make sure Python is installed. In the Command Prompt window, type:
	python --version
If you get an error or "Python is not recognized", you need to install Python:
	1. Go to https://www.python.org/downloads/
	2. Download the latest Python installer for Windows
	3. Run the installer and make sure to check "Add Python to PATH" during installation

### Step 3. Set up a virtual environment. 
This keeps your project dependencies isolated:
1. In the Command Prompt window, go to the script folder. Type:
	cd c:\<path to your script folder>.
2. In the Command Prompt, create a Python virtual environment named "bitcoin_env".
	python -m venv bitcoin_env
3. In the Command Prompt, activate the Python virtual environment.
	bitcoin_env\Scripts\activate

### Step 4. Install the required packages. 
1. In the Command Prompt window, type:
	pip install python-dotenv groq streamlit

### Step 5. Run the script. 
1. In the Command Prompt window, run the Streamlit application. Type:
	streamlit run bitcoin_analyzer.py

This will start a local web server and open the application in your browser. Press the Analyse button to view the results. 