# Email MCP Server

A simple tool that lets you send emails directly from Amazon Q using your Gmail account.

## What is this?

This is an MCP server that connects Amazon Q to your Gmail account, allowing you to send emails by simply asking Q to do it for you.

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager installed
  - Follow the installation instructions at: https://docs.astral.sh/uv/getting-started/installation/
  - After installing uv, run `uv python install` to ensure Python is properly set up with uv

## Setup Guide

### Step 1: Add the MCP server to your mcp.json file

Add the following configuration to your `~/.aws/amazonq/mcp.json` file:

```json
"email-mcp": {
  "command": "uvx",
  "args": ["--from", "git+https://github.com/mikebrugnoni/q-email-mcp.git", "email-mcp"],
  "env": {
    "FASTMCP_LOG_LEVEL": "ERROR"
  },
  "autoApprove": [],
  "disabled": false
}
```

### Step 2: Set up OAuth credentials

1. First, you need to get your OAuth credentials file:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Gmail API
   - Create OAuth 2.0 credentials (Desktop application)
   - Download the credentials file

2. Once you have your credentials file, simply ask Amazon Q:
   ```
   Set up my OAuth credentials for email using /path/to/certificate.json
   ```
   Replace `/path/to/certificate.json` with the actual path to your downloaded credentials file.

### Step 3: Start using it!

Now you can ask Q to send emails for you! For example:
```
Please send an email to example@example.com with the subject "Hello" and the message "This is a test email."
```

NOTE: Your web browser will launch the first time you attempt to send an email in order to complete the OAuth authentication process.

## Available Tools

### send_email
Sends an email using your Gmail account.

### setup_credentials
Sets up your OAuth credentials by copying your certificate file to the right location.

### get_credentials_status
Checks if your OAuth credentials are properly set up.

## Where Files Are Stored

All your credentials and tokens are stored securely in:
- `~/.aws/amazonq/email-mcp/`
