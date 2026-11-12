\# 💬 Local LLM Chatbot



A private chatbot that runs entirely on your own machine using \*\*Ollama\*\* and \*\*Streamlit\*\*. No API fees, and no data leaves your computer.



\## Features



\- Real-time streaming responses

\- Conversation memory within a session

\- Model selector (automatically lists all models installed in Ollama)

\- Editable system prompt to change the bot's behavior

\- Clear chat button



\## Tech Stack



\- Python 3.10+

\- \[Ollama](https://ollama.com) (local LLM runtime)

\- \[Streamlit](https://streamlit.io) (web interface)

\- Llama 3.2 (default model)



\## Prerequisites



1\. Install \[Ollama](https://ollama.com/download)

2\. Pull a model:

&#x20;  ```

&#x20;  ollama pull llama3.2

&#x20;  ```



\## Setup



```

git clone https://github.com/SuryaMenon0809/ollama-chatbot.git

cd ollama-chatbot

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

```



\## Run



```

streamlit run app.py

```



Then open http://localhost:8501 in your browser.



\## Example Use Case: Freight Forwarding



Set the system prompt to:



> You are an assistant for a freight forwarding company. Help staff draft professional emails and explain logistics terms (Incoterms, Bill of Lading, customs, LCL/FCL).



The bot can then draft customer emails, explain shipping terms, and summarize email threads, all without sending sensitive data to the cloud.



\## Limitations



\- Does not know your private company data (see Roadmap)

\- Answers may contain mistakes, so verify rates, regulations, and HS codes

\- Speed depends on your hardware



\## Roadmap



\- \[ ] Add RAG to answer questions from your own documents

\- \[ ] Add PDF upload and summarization

\- \[ ] Save chat history to disk

\- \[ ] Docker support



\## License



MIT

