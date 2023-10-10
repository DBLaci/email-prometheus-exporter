import signal
import sys
from flask import Flask, Response
import imaplib
import os

app = Flask(__name__)

def fetch_unread_count(imap_server, email, password):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email, password)
        mail.select('inbox')
        result, data = mail.search(None, '(UNSEEN)')
        unread_count = len(data[0].split())
        return unread_count
    except Exception as e:
        print(f"Error for account {email}: {e}")
        return None

@app.route("/metrics")
def metrics():
    accounts = os.environ['EMAIL_ACCOUNTS'].split(',')
    output = []

    for account in accounts:
        imap_server, email, password = account.split(':')
        unread_count = fetch_unread_count(imap_server, email, password)
        if unread_count is not None:
            output.append(f'email_unread_count{{email="{email}"}} {unread_count}')

    return Response('\n'.join(output) + '\n', content_type="text/plain; version=0.0.4")

def signal_handler(sig, frame):
    print("Shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
