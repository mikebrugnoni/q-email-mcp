# Email MCP Server

A simple tool that lets you send emails directly from Amazon Q using your Gmail account.

## What is this?

This is an MCP server that connects Amazon Q to your Gmail account, allowing you to send emails by simply asking Q to do it for you.

## Setup Guide (For Beginners)

### Step 1: Install the package

```bash
# Navigate to the email_mcp directory
cd ~/repos/mcp/email_mcp

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the package
pip install -e .
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

NOTE: Your web browser will launch the first time you attempt to send an email in order to complete the Oauth authentication process.

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

## Troubleshooting

If you have issues sending emails:
1. Check your credentials status by asking Q: "Check my email credentials status"
2. Make sure you've completed the OAuth authorization flow when prompted
3. Verify your internet connection
