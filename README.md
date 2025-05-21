# Email MCP Server for Amazon Q CLI

This MCP (Model Context Protocol) server allows Amazon Q CLI to send emails using Gmail's OAuth 2.0 authentication.

## Setup Instructions

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Create OAuth 2.0 credentials in Google Cloud Console:

   a. Go to [Google Cloud Console](https://console.cloud.google.com/)
   b. Create a new project or select an existing one
   c. Enable the Gmail API for your project
   d. Create OAuth 2.0 credentials (Desktop application type)
   e. Download the credentials JSON file

3. Start the MCP server:

```bash
python email_mcp_server.py
```

4. Register the MCP server with Amazon Q CLI:

```bash
q config add-mcp-server email http://localhost:8080
```

5. Set up OAuth credentials using Amazon Q:

```bash
q chat
```

Then ask Q to set up OAuth:

```
Can you set up OAuth for my email MCP server using my credentials file at /path/to/credentials.json?
```

## Usage

Once set up, you can ask Amazon Q to send emails:

```
Can you send an email to example@example.com with the subject "Hello" and body "This is a test email"?
```

## Available Tools

The MCP server provides two tools:

1. `setup_oauth` - Sets up OAuth 2.0 credentials for Gmail
2. `send_email` - Sends an email using the configured Gmail account

## Configuration

- Default port: 8080 (can be changed with `--port` argument)
- OAuth token storage: `~/repos/mcp/.email_mcp_token.pickle`
- OAuth credentials storage: `~/repos/mcp/.email_mcp_credentials.json`
