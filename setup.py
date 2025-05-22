from setuptools import setup, find_packages

setup(
    name="email-mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastmcp>=2.4.0",
        "google-api-python-client>=2.0.0",
        "google-auth-httplib2>=0.1.0",
        "google-auth-oauthlib>=0.5.0",
    ],
    py_modules=["server"],
    entry_points={
        "console_scripts": [
            "email-mcp=server:mcp.run_cli",
        ],
    },
)
