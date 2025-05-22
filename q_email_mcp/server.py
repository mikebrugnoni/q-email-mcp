# server.py
from fastmcp import FastMCP
import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
import json
from pathlib import Path

# Google API imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

mcp = FastMCP("Email MCP 📧")

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Default paths for credentials and tokens
DEFAULT_CONFIG_DIR = os.path.expanduser("~/.aws/amazonq/email-mcp")
DEFAULT_CREDENTIALS_PATH = os.path.join(DEFAULT_CONFIG_DIR, "certificate.json")
DEFAULT_TOKEN_PATH = os.path.join(DEFAULT_CONFIG_DIR, "token.json")

# Ensure config directory exists
os.makedirs(DEFAULT_CONFIG_DIR, exist_ok=True)

@mcp.tool()
def send_email(
    to: List[str], 
    subject: str, 
    body: str, 
    cc: Optional[List[str]] = None, 
    bcc: Optional[List[str]] = None,
    html: bool = True
) -> dict:
    """
    Send an email using Gmail API with OAuth 2.0 authentication.
    
    Args:
        to: List of recipient email addresses
        subject: Email subject line
        body: Email body content (can include HTML if html=True)
        cc: Optional list of CC recipients
        bcc: Optional list of BCC recipients
        html: Whether to treat the body as HTML (default: True)
        
    Returns:
        Dictionary with status and message ID if successful
    """
    try:
        # Check if credentials file exists in the default location
        if not os.path.exists(DEFAULT_CREDENTIALS_PATH):
            return {
                "success": False,
                "error": f"Credentials file not found at {DEFAULT_CREDENTIALS_PATH}. Please place your OAuth certificate.json file there."
            }
        
        # Get credentials and build service
        creds = None
        if os.path.exists(DEFAULT_TOKEN_PATH):
            creds = Credentials.from_authorized_user_info(
                json.loads(open(DEFAULT_TOKEN_PATH).read()), SCOPES)
        
        # If credentials don't exist or are invalid, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    DEFAULT_CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(DEFAULT_TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
        
        # Build the Gmail service
        service = build('gmail', 'v1', credentials=creds)
        
        # Create message
        message = MIMEMultipart()
        message['to'] = ', '.join(to)
        message['subject'] = subject
        
        if cc:
            message['cc'] = ', '.join(cc)
        if bcc:
            message['bcc'] = ', '.join(bcc)
            
        # Attach body
        content_type = 'html' if html else 'plain'
        message.attach(MIMEText(body, content_type))
        
        # Encode message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Send message
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': encoded_message}
        ).execute()
        
        return {
            "success": True,
            "message_id": send_message['id'],
            "message": "Email sent successfully!"
        }
        
    except HttpError as error:
        return {
            "success": False,
            "error": f"An error occurred: {error}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"An unexpected error occurred: {str(e)}"
        }

@mcp.tool()
def setup_credentials(source_path: str = None) -> dict:
    """
    Set up OAuth 2.0 credentials for Gmail API by copying from a source path or creating a new file.
    
    Args:
        source_path: Optional path to an existing OAuth certificate.json file
        
    Returns:
        Dictionary with status and file path
    """
    try:
        # If source path is provided, copy the file to the default location
        if source_path:
            if not os.path.exists(source_path):
                return {
                    "success": False,
                    "error": f"Source credentials file not found at {source_path}"
                }
            
            # Read the source file to validate it's a proper JSON
            with open(source_path, 'r') as src_file:
                credentials_data = json.load(src_file)
            
            # Write to the default location
            with open(DEFAULT_CREDENTIALS_PATH, 'w') as dest_file:
                json.dump(credentials_data, dest_file, indent=2)
                
            return {
                "success": True,
                "file_path": DEFAULT_CREDENTIALS_PATH,
                "message": f"Credentials copied to {DEFAULT_CREDENTIALS_PATH}"
            }
        else:
            # Check if credentials already exist
            if os.path.exists(DEFAULT_CREDENTIALS_PATH):
                return {
                    "success": True,
                    "file_path": DEFAULT_CREDENTIALS_PATH,
                    "message": f"Credentials already exist at {DEFAULT_CREDENTIALS_PATH}"
                }
            else:
                return {
                    "success": False,
                    "error": f"No credentials found at {DEFAULT_CREDENTIALS_PATH}. Please provide a source_path to copy from."
                }
    except Exception as e:
        return {
            "success": False,
            "error": f"Failed to set up credentials: {str(e)}"
        }

@mcp.tool()
def get_credentials_status() -> dict:
    """
    Check the status of OAuth credentials and token.
    
    Returns:
        Dictionary with status information
    """
    result = {
        "config_dir": DEFAULT_CONFIG_DIR,
        "credentials_path": DEFAULT_CREDENTIALS_PATH,
        "token_path": DEFAULT_TOKEN_PATH,
        "credentials_exist": os.path.exists(DEFAULT_CREDENTIALS_PATH),
        "token_exists": os.path.exists(DEFAULT_TOKEN_PATH)
    }
    
    if result["credentials_exist"]:
        try:
            with open(DEFAULT_CREDENTIALS_PATH, 'r') as f:
                creds_data = json.load(f)
            result["credentials_valid"] = "installed" in creds_data or "web" in creds_data
        except:
            result["credentials_valid"] = False
    
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio") # THIS IS SUPER IMPORTANT FOR Q CLI
