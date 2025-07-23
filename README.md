# Flask OpenAI API Backend

A Flask backend that accepts prompts from frontend applications and returns responses from the OpenAI API, with support for both chat and completion modes.

## Features

- ✅ **CORS Support** - Cross-origin requests enabled
- ✅ **Dual Mode Support** - Chat (GPT-4) or Completion (GPT-3)
- ✅ **Error Handling** - Proper exception handling and error responses
- ✅ **Environment Variables** - Secure API key management

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your-openai-key-here
```

**Get your OpenAI API key from:** https://platform.openai.com/api-keys

### 3. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### POST `/generate`

Generates AI responses using OpenAI API.

**Request Body:**
```json
{
  "prompt": "Explain quantum computing in simple terms",
  "mode": "chat"
}
```

**Parameters:**
- `prompt` (string, required): The input prompt for the AI
- `mode` (string, optional): Either "chat" (GPT-4) or "completion" (GPT-3). Defaults to "chat"

**Response:**
```json
{
  "response": "Quantum computing is a type of computation that harnesses the collective properties of quantum states..."
}
```

**Error Response:**
```json
{
  "error": "Error message here"
}
```

## Testing

### Using curl

```bash
# Chat mode (GPT-4)
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt":"Write a poem about AI", "mode":"chat"}'

# Completion mode (GPT-3)
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt":"Write a poem about AI", "mode":"completion"}'
```

### Using JavaScript/Fetch

```javascript
const response = await fetch('http://localhost:5000/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    prompt: 'Explain quantum computing in simple terms',
    mode: 'chat'
  })
});

const data = await response.json();
console.log(data.response);
```

## Project Structure

```
flask-openai-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
└── README.md          # This file
```

## Modes Explained

### Chat Mode (`mode: "chat"`)
- Uses GPT-4o-mini model (latest and most cost-effective)
- Better for conversational responses
- More context-aware
- Higher quality responses

### Completion Mode (`mode: "completion"`)
- Uses GPT-3.5-turbo model
- Good for text completion tasks
- Faster response times
- More cost-effective for simple tasks

## Error Handling

The API includes comprehensive error handling:
- Missing or invalid API key
- Network connectivity issues
- OpenAI API rate limits
- Invalid request format

All errors return a 500 status code with an error message in the response body.

## Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure
- Consider implementing rate limiting for production use
- Add authentication if needed for production deployments 