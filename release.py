#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER", "alessandroamella")
REPO_NAME = os.getenv("REPO_NAME", os.path.basename(os.getcwd()))


def validate_config():
    """Validate required environment variables"""
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN is required in your .env file")
        sys.exit(1)
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")


def generate_pdf():
    """Run note.sh && pdflatex doc.tex"""
    try:
        print("Running note.sh && pdflatex doc.tex...")
        result = subprocess.run(
            "./note.sh && pdflatex doc.tex",
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )
        print("PDF generation completed successfully, result:")
        print(result.stdout)

        # Check if doc.pdf exists
        if not os.path.exists("doc.pdf"):
            raise FileNotFoundError("doc.pdf was not generated")

        return "doc.pdf"

    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        sys.exit(1)


def create_release_and_upload(pdf_path, custom_message=""):
    """Create GitHub release and upload PDF"""
    try:
        # Create release info
        timestamp = int(datetime.now().timestamp())
        release_tag = f"release-{timestamp}"
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        release_name = f"Release {formatted_date}"

        # Release body
        release_body = f"Release created on {formatted_date}"
        if custom_message:
            release_body += f"\n\n{custom_message}"

        # Headers
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

        # Create release
        print("Creating GitHub release...")
        release_data = {
            "tag_name": release_tag,
            "name": release_name,
            "body": release_body,
            "draft": False,
            "prerelease": False,
        }

        response = requests.post(
            f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases",
            headers=headers,
            json=release_data,
        )

        if response.status_code != 201:
            raise Exception(
                f"Failed to create release: {response.status_code} - {response.text}"
            )

        release_info = response.json()
        print(f"Release created: {release_name}")

        # Rename PDF to match tag name
        new_pdf_name = f"{release_tag}.pdf"

        # Upload PDF
        print(f"Uploading {pdf_path} as {new_pdf_name}...")
        upload_url = release_info["upload_url"].replace("{?name,label}", "")

        with open(pdf_path, "rb") as pdf_file:
            upload_response = requests.post(
                f"{upload_url}?name={new_pdf_name}",
                headers={
                    "Authorization": f"token {GITHUB_TOKEN}",
                    "Content-Type": "application/pdf",
                },
                data=pdf_file.read(),
            )

        if upload_response.status_code != 201:
            raise Exception(f"Failed to upload PDF: {upload_response.status_code}")

        print(f"PDF uploaded as: {new_pdf_name}")
        print(f"Release URL: {release_info['html_url']}")

    except Exception as e:
        print(f"Error creating release: {e}")
        sys.exit(1)


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Simple Release Script")
    parser.add_argument("-m", "--message", help="Custom message for the release")

    args = parser.parse_args()

    validate_config()
    pdf_path = generate_pdf()
    create_release_and_upload(pdf_path, args.message or "")
    print("Release completed successfully!")


if __name__ == "__main__":
    main()
