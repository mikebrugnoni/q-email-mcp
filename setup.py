from setuptools import setup

setup(
    name="email-mcp-server",
    version="0.1.0",
    description="Email MCP Server for Amazon Q CLI",
    py_modules=["email_mcp_server"],
    entry_points={
        'console_scripts': [
            'email-mcp-server=email_mcp_server:run_server',
        ],
    },
    install_requires=[
        "google-auth-oauthlib",
        "google-auth",
        "google-api-python-client",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
