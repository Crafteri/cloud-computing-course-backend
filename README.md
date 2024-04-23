# Sentiment analysis back-end

## Setup

```ps
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

You will need to run the activation script to the virtual environment again if you close the command prompt.

```ps
.venv\Scripts\activate
```

## Running the program

After installing the dependencies you can run the program.

```python
python main.py
```

# Usage

POST request to `/sentiment_analysis` with the text in a JSON like this

```json
{
    "text": "It was so bad I walked out in the middle of the movie."
}
```

The endpoint will respond with the same format, adding a  `sentiment` property of positive/negative.