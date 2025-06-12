# Blocklist Updater

A lightweight Python tool that fetches and updates a compressed peer-to-peer (P2P) blocklist from the [BT\_BlockLists](https://github.com/Naunter/BT_BlockLists) repository. It checks whether the remote file (`bt_blocklists.gz`) has been updated, and if so, downloads and extracts it to your desired location.

---

## 🚀 Features

* Automatically checks for updates using GitHub API
* Downloads and decompresses `.gz` blocklist files
* Sends a system notification on update status
* CLI flag to customize output path (`--output`)
* Cron-compatible for automation

---

## 🧱 Requirements

* Python 3.12.4 (recommended via [pyenv](https://github.com/pyenv/pyenv))
* Poetry (for dependency and environment management)

---

## 📦 Installation

### Using Poetry (Recommended)

```bash
pyenv install 3.12.4
poetry install
```

This will automatically set up a virtual environment and install dependencies defined in `pyproject.toml`.

---

## ▶️ Usage

### Run Locally

```bash
poetry run blocklist_updater --output /your/destination/blocklist.txt
```

If `--output` is omitted, the default is `./blocklist.txt`.

### Run with Module Syntax (Optional)

```bash
poetry run python -m blocklist_updater
```

---

## 🕓 Cron Automation

To check daily at 10:00 AM:

```cron
0 10 * * * /opt/homebrew/bin/poetry -C /path/to/project run blocklist_updater --output /desired/path/blocklist.txt
```

> `-C` specifies the project directory, avoiding the need for `cd`.

---

## 🔗 Source Blocklist

This tool uses the public blocklist provided by:

👉 [Naunter/BT\_BlockLists](https://github.com/Naunter/BT_BlockLists)

---

## 🤝 License

This project is open-source. Feel free to fork, modify, or reuse it as you see fit. See the [UNLICENSE](./UNLICENSE) file for more details.
