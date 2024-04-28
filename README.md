# e2e_medical_chatbox
end to end medical chatbox application

# How to run?
### STEP 00 - Clone the repository:

```bash
Project repo: https://github.com/king610160/e2e_medical_chatbox
```

### STEP 01 - Create a conda environment after opening the repository

```bash
python -m venv env
```

```bash
source env/bin/activate
```

### STEP 02 - install the requirements

```bash
pip install -r requirements.txt
```

### STEP 03 - Create a `.env` file in the root directory and add your Pinecone credentials as follows: 

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### STEP 04 - Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

### STEP 05 - Save the data to Pinecone: 

```bash
python store_index.py
```

### STEP 06 - Start the application to ask the LLM with data in Pinecone:

```bash
python app.py
```

After start application, you can open the [localhost:8000](http://127.0.0.1:8000)


## TechStack Used

- Python
- Flask
- Meta Llama 2
- Langchain
- Pinecone