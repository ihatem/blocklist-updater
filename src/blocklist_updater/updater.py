import argparse
import os
import requests
import gzip
import tempfile
from datetime import datetime
from notifypy import Notify

def main():
    # --- Parse CLI argument
    parser = argparse.ArgumentParser(description="Update P2P blocklist.")
    parser.add_argument('--output', '-o', help='Destination path for blocklist.txt', default='./blocklist.txt')
    args = parser.parse_args()
    dest_file = os.path.abspath(args.output)

    # --- Notifier
    notifier = Notify()
    notifier.title = "Blocklist updater"
    notifier.urgency = "critical"

    # --- GitHub repo info
    owner = 'Naunter'
    repo = 'BT_BlockLists'
    file_path = 'bt_blocklists.gz'
    branch = 'master'

    api_url = f'https://api.github.com/repos/{owner}/{repo}/commits?path={file_path}&sha={branch}'
    file_url = f'https://github.com/{owner}/{repo}/raw/{branch}/{file_path}'

    # --- Main logic
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        commits = response.json()

        if not commits:
            notifier.message = "[CRITICAL] No commits found for file."
            notifier.send()
            exit(1)

        last_commit_date = commits[0]['commit']['committer']['date']
        remote_ts = datetime.strptime(last_commit_date, '%Y-%m-%dT%H:%M:%SZ').timestamp()
        local_ts = os.path.getmtime(dest_file) if os.path.exists(dest_file) else 0

        if remote_ts > local_ts:
            r = requests.get(file_url)
            r.raise_for_status()

            with tempfile.NamedTemporaryFile(delete=False) as gz_file:
                gz_file.write(r.content)

            with tempfile.NamedTemporaryFile(delete=False) as txt_file:
                with gzip.open(gz_file.name, 'rb') as f_in:
                    txt_file.write(f_in.read())

            os.replace(txt_file.name, dest_file)
            notifier.message = f"Blocklist updated: {dest_file}"
            notifier.send()

            os.unlink(gz_file.name)
        else:
            notifier.message = "Blocklist already up to date"
            notifier.send()

    except Exception as e:
        notifier.message = f"[CRITICAL] {str(e)}"
        notifier.send()
