# Neurodivergent Translation System

This project provides a translation system that converts between Neurotypical (NT) and Neurodivergent (ND) phrases. It leverages OpenAI's GPT model to provide translations that are tailored to both neurodivergent and neurotypical individuals, with caching to optimize repeated translations.

## Features
- Translates NT (Neurotypical) phrases into ND (Neurodivergent) phrases (e.g., autism-friendly translations).
- Translates ND (Neurodivergent) phrases into NT (Neurotypical) phrases.
- Caches translations to reduce API calls and improve performance.
- Customizable translation directions ("NT->ND" or "ND->NT").

## Prerequisites

Ensure that you have Python 3.6 or higher installed, along with the necessary dependencies. You will also need an OpenAI API key.

### Dependencies

- `openai==0.27.0`
- `argparse==1.4.0` (optional for Python >= 3.2)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Configuration

Before running the application, you'll need to configure your OpenAI API key. Create a file named `settings.py` and add the following:

```python
OPENAI_API_KEY = 'your-api-key-here'  # Replace with your actual API key
OPENAI_ENGINE = 'gpt-3.5-turbo-instruct'  # You can change this to your preferred engine
MAX_TOKENS = 100  # Maximum tokens to use for each translation request
TEMPERATURE = 0.5  # Controls the creativity of the translation (lower = more rigid, higher = more creative)
```

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
ND -> NT: It's something most people know without having to think about it.
```

## Cache

The application uses a cache file (`cache.json`) to store previously translated phrases and their results. This helps avoid making redundant requests to OpenAI's API, saving both time and costs.

### Cache Location

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
- If the translation is not accurate or there are errors, check the OpenAI API key and configuration settings in `settings.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
