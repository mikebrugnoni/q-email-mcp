# Email MCP Server

An MCP server for sending emails using Gmail API with OAuth 2.0 authentication.

## Setup

1. Create a virtual environment and install the package:
```
cd /path/to/email_mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

2. Place your OAuth 2.0 credentials:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Gmail API
   - Create OAuth 2.0 credentials (Desktop application)
   - Place your credentials file at: `~/.aws/amazonq/email-mcp/certificate.json`
   - Alternatively, use the `setup_credentials` tool to copy your credentials file

3. Send emails using the `send_email` tool

## Usage with Amazon Q

Once installed and set up, you can use this MCP server with Amazon Q:

```
q chat --mcp email-mcp
```

Then you can ask Q to send emails for you using the Gmail API.

## Tools

### send_email
Sends an email using Gmail API with OAuth 2.0 authentication.

### setup_credentials
Copies an existing OAuth 2.0 credentials file to the default location.

### get_credentials_status
Checks the status of your OAuth credentials and token.

## Default Paths

- Credentials directory: `~/.aws/amazonq/email-mcp/`
- Credentials file: `~/.aws/amazonq/email-mcp/certificate.json`
- Token file: `~/.aws/amazonq/email-mcp/token.json`
