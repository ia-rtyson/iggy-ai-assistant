This is the Github repo for the AI “Iggy” project that was presented at ICC 2025. Feel free to download and use it! 

To run this project, make sure to have Docker downloaded. Simply run "docker compose up -d" in the same folder as the docker-compose.yml to spin up this stack. All the data that was used for the presentation should autopopulate and be available upon runtime.

You will need to use your own LLM. This could be a locally hosted LLM using Ollama, for example, or an API key to hosted LLMs such as Gemini, Claud, ChatGPT, etc. This can currently be specified in the n8n workflows. In the future, we would like to take advantage of environment variables to specify the LLM and authentication profiles within the compose file. The LLM credential is used in most of the n8n workflows and will need to be updated accordingly.

The services within this Docker Stack can be found at the following after :

n8n - http://localhost:5678/
Demo User: admin@local.com
Demo Pass: Password1

Ignition - http://localhost:8088/

pgAdmin(postgres database) - http://localhost:5050/browser/
