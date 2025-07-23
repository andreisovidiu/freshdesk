# Setup

## Prerequisites

- Python 3.x
- PIP
- Freshdesk account with API access
- API key from your Freshdesk instance

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with your Freshdesk credentials:

```env
API_KEY=your_freshdesk_api_key_here
DOMAIN=your_freshdesk_domain_here
```

**Note:** Replace `your_freshdesk_api_key_here` with your actual API key and `your_freshdesk_domain_here` with your Freshdesk subdomain ((e.g., if your Freshdesk URL is `https://company.freshdesk.com`, use `company` as the domain)).