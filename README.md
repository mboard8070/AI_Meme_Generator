# AI Meme Generator

**Automated AI-Powered Meme Creation and Social Media Auto-Poster**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An open-source Python project that uses artificial intelligence to generate hilarious, context-aware memes and automatically post them to social platforms (currently with built-in Instagram support via session management).

## Features
- **AI-Driven Meme Generation**: Creates fresh, topical memes using cutting-edge language models.
- **Automated Posting**: Seamless auto-posting to Instagram; designed to be extensible to other platforms.
- **Modular & Clean Architecture**: Easy-to-understand structure with separate config, utils, and workflow directories.
- **Lightweight Dependencies**: Pure Python with all requirements listed in `requirements.txt`.

## Project Structure
```text
.
├── app.py                  # Main entry point – runs the meme generation and posting pipeline
├── generate_ig_session.py  # Utility to create and save Instagram session for auto-posting
├── requirements.txt        # Project dependencies
├── config/                 # Configuration files (prompts, templates, credentials, etc.)
├── utils/                  # Helper functions and utilities
├── workflows/              # Core automation logic and pipelines
└── .idea/                  # PyCharm/IntelliJ project files (can be ignored)


Quick Start
# 1. Clone the repo
git clone [https://github.com/mboard8070/AI_Meme_Generator.git](https://github.com/mboard8070/AI_Meme_Generator.git)
cd AI_Meme_Generator

# 2. Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate Instagram session (for auto-posting)
python generate_ig_session.py

Configuration
Customize prompts, templates, posting schedule, and AI settings inside the config/ folder.

Important: Always respect platform terms of service when using automated posting features.
*My instagram integration could be cleaner
# 5. Run the bot
python app.py
