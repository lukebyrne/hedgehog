#!/bin/bash

# Colors for better formatting
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${CYAN}🦔 Hedgehog AI Hedge Fund 🦔${NC}"
echo ""

# Check for Python environment
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Setting up...${NC}"
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .
else
    source .venv/bin/activate
fi

# Check for .env file
if [ ! -f ".env" ]; then
    echo -e "${RED}Error: .env file not found.${NC}"
    echo "Creating example .env file. Please edit with your API keys."
    echo "OPENROUTER_API_KEY=your_openrouter_api_key" > .env
    echo "FINANCIAL_DATASETS_API_KEY=your_financial_datasets_api_key" >> .env
    echo "HEDGEHOG_DARK_MODE=0" >> .env
    exit 1
fi

# Display menu
echo "Please select an option:"
echo -e "${GREEN}1.${NC} Analyze stocks (interactive mode)"
echo -e "${GREEN}2.${NC} Run backtest (last 6 months)"
echo -e "${GREEN}3.${NC} Analyze FAANG stocks (Apple, Amazon, Meta, Google, Netflix)"
echo -e "${GREEN}4.${NC} Analyze semiconductor stocks (NVDA, AMD, INTC, TSM, AVGO)"
echo -e "${GREEN}5.${NC} Run custom command"
echo -e "${GREEN}q.${NC} Quit"
echo ""

read -p "Enter your choice: " choice

case $choice in
    1)
        echo -e "${CYAN}Running stock analysis in interactive mode...${NC}"
        python -m hedgehog.main analyze AAPL MSFT GOOGL --interactive
        ;;
    2)
        echo -e "${CYAN}Running backtest for last 6 months...${NC}"
        # Calculate dates
        END_DATE=$(date +%Y-%m-%d)
        START_DATE=$(date -v-6m +%Y-%m-%d 2>/dev/null || date --date="6 months ago" +%Y-%m-%d)
        echo "From $START_DATE to $END_DATE"
        python -m hedgehog.main backtest AAPL MSFT GOOGL AMZN META --start=$START_DATE --end=$END_DATE
        ;;
    3)
        echo -e "${CYAN}Analyzing FAANG stocks...${NC}"
        python -m hedgehog.main analyze AAPL AMZN META GOOGL NFLX --interactive
        ;;
    4)
        echo -e "${CYAN}Analyzing semiconductor stocks...${NC}"
        python -m hedgehog.main analyze NVDA AMD INTC TSM AVGO --interactive
        ;;
    5)
        echo -e "${YELLOW}Enter command to run (python -m hedgehog.main ...):${NC}"
        read -p "> " cmd
        eval $cmd
        ;;
    q|Q)
        echo -e "${CYAN}Exiting. Thank you for using Hedgehog!${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}Invalid option. Exiting.${NC}"
        exit 1
        ;;
esac