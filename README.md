A simple repo to showcase AI agent capabilities using FastAPI and React

1. To run, create a virtual env and install dependencies

```
python -m venv <name>

source <name>/bin/activate

pip install -r requirements.txt
```

2. Generate and create a free OpenAI API key for CrewAI usage. Set it as an env variable.

`export OPENAI_API_KEY=<your api key>`

3. To run the FastAPI server,
```
uvicorn api:api --port 8080 --reload
```

4. To run the frontend:
`cd frontend` and then `npm start`

