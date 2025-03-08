# 🦔 Hedgehog AI Hedge Fund

Hedgehog is an AI-powered hedge fund analysis system that combines multiple AI analyst perspectives to provide comprehensive investment recommendations. It's designed to help investors make more informed decisions by aggregating insights from various investment styles and methodologies.

## Features

- **Multiple AI Analysts**: Get insights from AI analysts modeled after famous investors (Warren Buffett, Charlie Munger, Bill Ackman, Ben Graham, Cathie Wood)
- **Comprehensive Analysis**: Technical, fundamental, sentiment, and valuation perspectives combined into a single coherent recommendation
- **Backtesting**: Test strategies against historical data to evaluate performance
- **Modern AI Models**: Uses OpenRouter API to access the latest AI models from OpenAI, Anthropic, and more
- **Interactive CLI**: Choose your analysts and models through an intuitive command-line interface
- **Real-time Progress Tracking**: Monitor the analysis process with detailed progress tracking

## Requirements

- Python 3.10+
- OpenRouter API key (for accessing AI models)
- Financial Datasets API key (for market data)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hedgehog.git
cd hedgehog
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

3. Create a `.env` file with your API keys:
```
OPENROUTER_API_KEY=your_openrouter_api_key
FINANCIAL_DATASETS_API_KEY=your_financial_datasets_api_key
HEDGEHOG_DARK_MODE=0  # Set to 1 for dark mode
```

## Usage

### Analyzing Stocks

To analyze one or more stocks:

```bash
python -m hedgehog.main analyze AAPL MSFT GOOGL --interactive
```

Options:
- `--interactive`: Use interactive CLI to select analysts and models
- `--model`: Specify a model directly (e.g., `--model="anthropic/claude-3.5-sonnet"`)
- `--show-reasoning`: Show detailed reasoning from each analyst

### Running a Backtest

To run a historical backtest:

```bash
python -m hedgehog.main backtest AAPL MSFT GOOGL --start=2022-01-01 --end=2023-01-01 --capital=1000000
```

Options:
- `--start`: Start date (YYYY-MM-DD)
- `--end`: End date (YYYY-MM-DD)
- `--capital`: Initial capital (default: 1,000,000)
- `--max-positions`: Maximum number of positions (default: 10)
- `--position-size`: Maximum position size as percentage (default: 10.0)
- `--rebalance`: Rebalance frequency in days (default: 30)
- `--no-stop-loss`: Disable stop-loss

## Available Analysts

- **Warren Buffett**: Value investing with focus on moats and long-term business quality
- **Charlie Munger**: Mental models and multidisciplinary thinking
- **Bill Ackman**: Activist investing approach with focus on high-quality businesses
- **Ben Graham**: Classical value investing using strict quantitative criteria
- **Cathie Wood**: Innovation-focused investing with emphasis on disruptive technologies
- **Fundamentals Analyst**: Pure financial fundamental analysis
- **Technical Analyst**: Price action and technical indicators
- **Sentiment Analyst**: News, social media, and market sentiment
- **Valuation Analyst**: Detailed intrinsic value calculations

## Available Models

Hedgehog uses OpenRouter to access models from multiple providers:

- OpenAI: GPT-4o, o1, o1-mini, etc.
- Anthropic: Claude 3.5 Sonnet, Claude 3.7 Sonnet, etc.
- DeepSeek: DeepSeek R1 Distill LLaMa 70B, etc.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.