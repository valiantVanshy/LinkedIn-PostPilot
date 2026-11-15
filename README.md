# LinkedIn PostPilot 💼

An AI-powered LinkedIn post generator built with **Python**, **Streamlit**, **LangChain**, and **Groq**.

Select a topic and post length to generate an English-language draft, guided by sample posts from a local dataset.

## Features

- **Topic selection:** Choose from topics available in the sample dataset.
- **Adjustable length:** Generate short, medium, or long posts.
- **Few-shot prompting:** Use up to two matching examples to guide the writing style.
- **AI generation:** Create drafts using Groq’s `llama-3.3-70b-versatile` model.
- **Interactive interface:** Generate and view posts through a styled Streamlit application.
- **Dataset preprocessing:** Extract post metadata and consolidate related topic tags.

> PostPilot generates drafts for review and manual sharing. It does not publish or schedule posts on LinkedIn.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Streamlit | Web interface |
| LangChain | Prompt construction and model integration |
| Groq | LLM inference |
| pandas | Filtering sample posts |
| python-dotenv | Loading environment variables |

## How It Works

1. Loads sample posts from `data/processed_posts.json`.
2. Collects your selected topic, length, and language.
3. Filters examples matching those selections.
4. Builds a prompt with your preferences and up to two matching examples.
5. Sends the prompt to Groq and displays the generated draft.

If no examples match, the application generates a draft using the selected preferences alone.

### Post Length Options

| Option | Requested Output |
|---|---|
| Short | 1–5 lines |
| Medium | 6–10 lines |
| Long | 11–15 lines |

These ranges are prompt instructions; actual output length may vary.

## Getting Started

### Prerequisites

- Python 3.11 or newer recommended
- Git
- A [Groq API key](https://console.groq.com/)
- Internet access for model requests

### 1. Clone the Repository

```bash
git clone https://github.com/valiantVanshy/LinkedIn-PostPilot.git
cd LinkedIn-PostPilot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows — PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
python -m pip install python-dotenv
```

> The application imports `python-dotenv`, but it is currently missing from `requirements.txt`, so install it separately.

### 4. Configure Your API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your Groq API key.

The repository’s `.gitignore` excludes `.env`. Keep your API key private.

### 5. Run the Application

From the project root, run:

```bash
streamlit run main.py
```

Open the URL shown in your terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Select a **Topic**.
2. Choose **Short**, **Medium**, or **Long**.
3. Keep **English** selected; it is currently the only language available in the interface.
4. Click **Generate LinkedIn Post**.
5. Review and edit the generated draft before sharing it.

## Project Structure

```text
LinkedIn-PostPilot/
├── data/
│   ├── raw_posts.json          # Source sample posts
│   └── processed_posts.json    # Posts enriched with metadata
├── .gitignore
├── LICENSE                    # MIT License
├── few_shot.py                # Loads and filters sample posts
├── llm_helper.py              # Configures the Groq model
├── main.py                    # Streamlit application
├── post_generator.py          # Builds prompts and generates drafts
├── preprocess.py              # Extracts metadata and unifies tags
└── requirements.txt           # Project dependencies
```

## Customize the Dataset

Processed examples are included, so preprocessing is optional during initial setup.

To use your own examples:

1. Update `data/raw_posts.json`.
2. Run the preprocessing script.
3. Restart the application.

### Input Format

Each post must contain a `text` field:

```json
[
  {
    "text": "Your first sample LinkedIn post."
  },
  {
    "text": "Another sample post demonstrating your preferred writing style."
  }
]
```

### Run Preprocessing

```bash
python preprocess.py
```

The script:

- Extracts `line_count`, `language`, and up to two topic tags per post.
- Consolidates related tags into shared categories.
- Saves the results to `data/processed_posts.json`.

> Preprocessing makes Groq API calls and overwrites the processed dataset. The current metadata prompt assigns English as the language.

### Example Categorization

Sample posts are classified by their stored line count:

| Category | Example Line Count |
|---|---|
| Short | Fewer than 5 |
| Medium | 5–10 |
| Long | More than 10 |

These categories determine which examples are included in a generation prompt.

## Model Configuration

The model is configured in `llm_helper.py`:

```python
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)
```

To use another model, replace `model_name` with a model available to your Groq account.

To adjust the generation instructions, edit `post_generator.py`.

## Troubleshooting

| Issue | Suggested Fix |
|---|---|
| Missing or invalid API key | Check `GROQ_API_KEY` in `.env` and restart the application. |
| `No module named 'dotenv'` | Run `python -m pip install python-dotenv`. |
| Dataset file not found | Run the app from the project root and confirm `data/processed_posts.json` exists. |
| Model request fails | Check connectivity, API key validity, and model availability. |
| Rate limit reached | Check your Groq account limits and retry later. |
| Generated length varies | Edit the draft or adjust the prompt in `post_generator.py`. |

## Current Limitations

- The interface supports English only.
- Topics come from the processed dataset; free-text topic entry is not available.
- Example selection uses exact topic, language, and length matches.
- Generated content requires review for accuracy, relevance, and tone.
- LinkedIn authentication, publishing, and scheduling are not implemented.

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make and verify your changes.
4. Commit your updates:

   ```bash
   git commit -m "Describe your change"
   ```

5. Push your branch:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a pull request describing your changes.

Report bugs or suggest features through
[GitHub Issues](https://github.com/valiantVanshy/LinkedIn-PostPilot/issues).

## Author

**Vanshika Sharma**

GitHub: [@valiantVanshy](https://github.com/valiantVanshy)

## License

This project is licensed under the [MIT License](LICENSE).

Copyright © 2026 Vanshika Sharma.
