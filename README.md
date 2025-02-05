# Neurodivergent Translation System

This project provides a translation system that converts between Neurotypical (NT) and Neurodivergent (ND) phrases. It leverages OpenAI's GPT model to provide translations that are tailored to both neurodivergent and neurotypical individuals, with caching to optimize repeated translations.

## Features
- Translates NT (Neurotypical) phrases into ND (Neurodivergent) phrases (e.g., autism-friendly translations).
- Translates ND (Neurodivergent) phrases into NT (Neurotypical) phrases.
- Caches translations to reduce API calls and improve performance.
- Customizable translation directions ("NT->ND" or "ND->NT").

## Prerequisites

- Python 3.x
- OpenAI account with a created API key [API keys](https://platform.openai.com/settings/organization/api-keys)
- Added payment credentials and pre-pay at least $5 ($6 with tax) to your OpenAI account

### Dependencies

- `openai==0.27.0`
- `argparse==1.4.0` (optional for Python >= 3.2)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Configuration

Before running the application, you'll need to configure your OpenAI API key. Rename `settings example.py` to `settings.py` or create a new file by that name and add the following:

```python
OPENAI_API_KEY = 'your-api-key-here'  # Replace with your actual API key
OPENAI_ENGINE = 'gpt-3.5-turbo-instruct'  # You can change this to your preferred engine
MAX_TOKENS = 100  # Maximum tokens to use for each translation request
TEMPERATURE = 0.5  # Controls the creativity of the translation (lower = more rigid, higher = more creative)
```

### Note on engines

At the moment of writing, the most cost-efficient engine that responds in a reasonable time is `gpt-3.5-turbo-instruct`. It will cost about $3 per every 1 million translations requested, as you're making both a input and output request.
The current list of available and compatible engines is

| Model                        | Price (Standard)    | Price (Premium)   |
|------------------------------|---------------------|-------------------|
| chatgpt-4o-latest             | $5.00 / 1M tokens  | $15.00 / 1M tokens|
| gpt-4-turbo                   | $10.00 / 1M tokens | $30.00 / 1M tokens|
| gpt-4-turbo-2024-04-09        | $10.00 / 1M tokens | $30.00 / 1M tokens|
| gpt-4                         | $30.00 / 1M tokens | $60.00 / 1M tokens|
| gpt-4-32k                     | $60.00 / 1M tokens | $120.00 / 1M tokens|
| gpt-4-0125-preview            | $10.00 / 1M tokens | $30.00 / 1M tokens|
| gpt-4-1106-preview            | $10.00 / 1M tokens | $30.00 / 1M tokens|
| gpt-4-vision-preview          | $10.00 / 1M tokens | $30.00 / 1M tokens|
| gpt-3.5-turbo-0125            | $0.50 / 1M tokens  | $1.50 / 1M tokens |
| gpt-3.5-turbo-instruct        | $1.50 / 1M tokens  | $2.00 / 1M tokens |
| gpt-3.5-turbo-1106            | $1.00 / 1M tokens  | $2.00 / 1M tokens |
| gpt-3.5-turbo-0613            | $1.50 / 1M tokens  | $2.00 / 1M tokens |
| gpt-3.5-turbo-16k-0613        | $3.00 / 1M tokens  | $4.00 / 1M tokens |
| gpt-3.5-turbo-0301            | $1.50 / 1M tokens  | $2.00 / 1M tokens |

If these become outdated, look up [the deprecation list](https://platform.openai.com/docs/deprecations) for the nearest equivalent model.

## Usage

Once everything is set up, you can run the script to translate phrases between NT and ND. A `main.py` file is included with an example of how you can use this:

### Command-line Interface

You can run the example system from the command line and provide a phrase for translation:

```bash
python main.py "Your phrase here" --direction nt->nd
```

The `--direction` argument can be either:
- `nt->nd` (translate from Neurotypical to Neurodivergent)
- `nd->nt` (translate from Neurodivergent to Neurotypical)

By default, the direction is set to `nt->nd`.

### Example

#### Input:

```bash
python main.py "It's just common sense." --direction nt->nd
```

#### Output:

```bash
Translation not cached, getting from external service using context NT->ND
NT -> ND: It's something most people know without having to think about it.
```

## Cache

The application uses a cache file (`cache.json`) to store previously translated phrases and their results. This helps avoid making redundant requests to OpenAI's API, saving both time and costs.

#### Cache Location

The cache will be stored in a file named `cache.json` in the same directory as the script. The file will automatically be created based on the user's queries.

#### Cache format exanple

```json
{"It's just common sense": {"translation": "It's something most people know without having to think about it.", "timestamp": 1738762433.549149}
```

### Permissions

Ensure that the user running the application has **read/write** permissions for `cache.json`, as the application needs to both read from and write to this file.

Additionally, ensure the application has **write** permissions for the directory in which it is running, so it can create the `cache.json` file if it does not already exist.

## Troubleshooting

- If you encounter issues with the cache file not being created or updated, check the file permissions to ensure that the application has the necessary access.
- If the translation is not accurate or there are errors, check the `TEMPERATURE` and `MAX_TOKENS` configuration settings in `settings.py`.
- If OpenAI throws an error, it most often returns a solution to the problem. Most OpenAI-related settings is in the settings.py file
- If OpenAI throws the `You exceeded your current quota, please check your plan and billing details.` error, you have most likely not set up payment methods for your OpenAI account.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
