<pre>
# POC Chatbot using ChatGPT API

This repository contains a proof-of-concept (POC) chatbot built using the ChatGPT API, Django, and Python. 
The purpose of this project is to demonstrate how to create a simple yet effective chatbot using the OpenAI 
ChatGPT API and integrate it into a web application built on the Django framework.

## Features

- User-friendly chat interface
- Asynchronous API calls to ChatGPT
- Rate limiting and error handling
- Customizable conversation context and settings

## Requirements

- Python 3.8+
- Django 3.2+
- Requests library
- An OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/poc-chatbot-chatgpt.git
cd poc-chatbot-chatgpt
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set up the environment variable for your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

4. Migrate the database:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your web browser and navigate to `http://127.0.0.1:8000/` to interact with the chatbot.

## Usage

- Start a conversation with the chatbot by typing your message in the input field and pressing Enter.
- The chatbot will respond to your messages using the ChatGPT API.
- To customize the conversation context or settings, you can modify the `settings.py` file or the `chatbot/utils.py` module.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name, e.g., `git checkout -b add-new-feature`.
3. Make your changes and commit them with a clear commit message.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

Please ensure your changes do not break existing functionality by testing your code before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
</pre>
