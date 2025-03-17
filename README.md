# LangChain-Streamlit-API

A simple web application that integrates LangChain with FastAPI and Streamlit to create AI-powered content generation.

## Overview

This project demonstrates how to build a web application that leverages LangChain, FastAPI, and Streamlit to create an essay generation service powered by OpenAI's language models. The application consists of a backend API server built with FastAPI and LangServe, and a frontend interface built with Streamlit.

## Features

- FastAPI backend with LangServe for easy deployment of LangChain applications
- Streamlit frontend for user interaction
- Integration with OpenAI's language models
- Essay generation based on user input

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Required Python packages (see requirements.txt)

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/LangChain-Streamlit-API.git
cd LangChain-Streamlit-API
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up environment variables:
```
cp .env.example .env
```
Then add your OpenAI API key to the `.env` file.

### Usage

1. Start the FastAPI server:
```
python app.py
```
This will start the server at http://localhost:8000

2. In a separate terminal, start the Streamlit frontend:
```
streamlit run client.py
```
This will open the Streamlit interface in your default web browser.

3. Enter a topic in the text input field and get an AI-generated essay.

## API Endpoints

- `/openai`: Direct access to OpenAI chat completion
- `/essay`: Generates an essay on a given topic

## Project Structure

- `app.py`: FastAPI backend server with LangChain integration
- `client.py`: Streamlit frontend for user interaction
- `.env`: Environment variables (not tracked in git)

## Future Improvements

- Add more content generation options (poems, stories, etc.)
- Integrate with additional language models (Ollama, etc.)
- Add more customization options for generated content
