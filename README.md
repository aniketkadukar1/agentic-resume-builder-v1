# Agentic Resume Builder v1

Agentic Resume Builder is a Python-based application designed to help users improve their resumes based on job descriptions. It leverages AI tools to analyze job postings and provide tailored suggestions for enhancing resumes.

## Features

- **Job Data Processing**: Extract and process job-related information such as title, company, location, salary, and responsibilities.
- **Resume Data Processing**: Analyze and structure resume data, including work experience, education, and skills.
- **AI-Powered Suggestions**: Use AI to provide recommendations for improving resumes based on job descriptions.
- **Tool Integration**: Seamlessly integrates tools for accessing and processing job and resume data.

## Project Structure

- **`agent.py`**: Main application file that orchestrates the interaction between the user, tools, and AI.
- **`tools.py`**: Contains tools for processing job and resume data.
- **`modules/job.py`**: Defines the `Job` model and provides mock job data.
- **`modules/resume.py`**: Defines the `Resume` model and provides mock resume data.
- **`.env`**: Environment variables file.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`LICENSE`**: MIT License for the project.

## Installation

- create .env file and add your GROQ_API_KEY
- install dependencies using 
```
pip install -r requirements.txt
```

## Run the application
python agent.py

