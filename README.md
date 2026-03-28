# 🤖 AI Code Reviewer

A powerful AI-powered code review tool built with Streamlit and Groq API. Submit your code for automated analysis on readability, structure, design patterns, security, performance, and testability.

## Features

- **Multi-Language Support**: Review code in Java, Python, JavaScript, TypeScript, and C++
- **Customizable Analysis**: Adjust strictness levels (1-5) and select focus areas
- **Detailed Feedback**: Organized reviews with sections for strengths, improvements, and refactored code
- **Fast AI Processing**: Powered by Groq's ultrafactive llama-3.3-70b-versatile model
- **Professional Insights**: Reviews from the perspective of a Senior Staff Engineer

## Supported Focus Areas

- ✅ Readability
- 🏗️ Design Patterns
- 🔒 Security (OWASP)
- ⚡ Performance
- 🧪 Testability

## Installation

### Prerequisites

- Python 3.8+
- Groq API key ([get it here](https://console.groq.com))

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-code-reviewer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use

1. **Select Parameters** (left sidebar):
   - Choose your programming language
   - Set the strictness level (1=lenient, 5=strict)
   - Select focus areas for the review

2. **Paste Your Code**: Enter your code in the text area

3. **Analyze**: Click the "Analyze Code" button to get your review

4. **Review Results**: Get structured feedback with:
   - ✅ The Good - What's working well
   - ⚠️ Opportunities for Improvement - What could be better
   - 🚀 Refactored Version - Improved code example

## Requirements

- `streamlit` - Web UI framework
- `langchain-groq` - Groq API integration
- `python-dotenv` - Environment variable management
- `groq` - Groq Python client

## Environment Variables

Create a `.env` file with:
```
GROQ_API_KEY=your_groq_api_key
```

## Project Structure

```
ai-code-reviewer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
└── README.md          # This file
```

## Architecture

The application uses:
- **Streamlit**: Frontend UI and state management
- **Groq API**: AI-powered code analysis with llama-3.3-70b-versatile model
- **System Prompt**: Specialized prompt engineered for senior-level code reviews

## Configuration

Modify analysis behavior by adjusting:
- `strictness` slider: Controls review intensity (1-5)
- `focus_area`: Multi-select which aspects to emphasis
- `language`: Choose the programming language context
- Model parameters: `temperature=0.3, max_tokens=1500`

## Error Handling

The app includes error handling for:
- Missing API key
- Invalid code submissions
- API rate limits or failures

If analysis fails, check:
1. Your `.env` file has a valid `GROQ_API_KEY`
2. Your API key has available credits
3. Network connectivity

## Future Enhancements

- [ ] Code upload from files
- [ ] Batch code review
- [ ] Custom focus area templates
- [ ] Review history and comparisons
- [ ] Export reviews to PDF/JSON
- [ ] Integration with git workflows

## License

MIT

## Support

For issues or questions, please check:
- Groq API documentation: https://console.groq.com
- Streamlit docs: https://docs.streamlit.io
