import os
import requests
import json
import streamlit as st
from datetime import datetime, timedelta
from groq import Groq
from dotenv import load_dotenv

# Set up the environment variables
load_dotenv()

# Initialise the model
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

# A helper function using Groq API
def generate_response(prompt):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Get Bitcoin Price From the last 24 hours using Coinpaprika API
def GetBitCoinPrices():

    # Calculate timestamp 24 hours ago in the required format
    start_time = (datetime.utcnow() - timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define the API endpoint and query parameters
    url = "https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical"
    params = {
        "start": start_time,  # Use Python datetime instead of shell command
        "interval": "24h"
    }
    
    # Define the request headers with API key and host
    headers = {
        "Accept": "application/json"
    }

    # Send a GET request to the API endpoint with query parameters and headers
    response = requests.request("GET", url, headers=headers, params=params)
    
    # Parse the response data as a JSON object
    data = json.loads(response.text)
    
    # Extract the "close" prices from the list of dictionaries
    closingPrices = ','.join(str(item["close"]) for item in data)  # Access parsed data
  
    # Return the comma-separated string of prices
    return closingPrices  # Fixed: Variable name consistency

def AnalyseBitCoin(bitcoinPrices):
    GroqPrompt = f"""You are an expert in crypto trading with more than 10 years of experience.
    I am a total beginner at this. 
    I will provide you with a list of Bitcoin prices for the last 24 hours.
    Please analyse the prices of Bitcoin and produce:
    * Price Overview
    * Moving Averages
    * Relative Strength Index (RSI)
    * Moving Average Convergence Divergence (MACD)
    Please advise whether I should buy or sell.
    Please be as detailed as you can in your analysis, and explain in a way that I will be able to understand. 
    Use headings in your answers.
    Here is the price list: {bitcoinPrices}"""

    try:
        message = generate_response(GroqPrompt)
    except Exception as e:
        message = "Sorry, something went wrong. Please try again later."
    return message


st.title('Crypto Price Analysis with Prompt Engineering')

if st.button('Analyse'):
    try:
        with st.spinner('Getting Bitcoin prices...'):
            bitcoinPrices = GetBitCoinPrices()
            st.success('Successfully retrieved Bitcoin prices')
        
        with st.spinner('Analysing Bitcoin prices...'):
            analysis = AnalyseBitCoin(bitcoinPrices)
            st.markdown("### Analysis Results")
            st.markdown(analysis)
            st.success('Analysis completed successfully')
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")