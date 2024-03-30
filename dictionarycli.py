import typer
import requests
import json
import os

from yaspin import yaspin
from rich.console import Console
from rich.table import Table
from yaspin.spinners import Spinners
from db import Database

app = typer.Typer()
console = Console()
db = Database(db_file="dictionary")
db.create_table(table_name="dictionary", word="Word", meaning="Meaning")

API_KEY = "<MERRIAM-WEBSTER API KEY>"
API_KEY_MEDICAL = "<MERRIAM-WEBSTER API KEY>"
dict_type = "sd3"


def load_json(word):
    with open(f"words/{word}.json") as data:
        word_json = json.load(data)
        return [(word["meta"]["id"], ",".join(word["shortdef"])) for word in word_json]


def dump_json(resp_json, word):
    with open(f"words/{word}.json", "w") as data:
        json.dump(resp_json, data, indent=4)
    return [(word["meta"]["id"], ",".join(word["shortdef"])) for word in resp_json]


def print_table(word_list):
    table = Table(show_header=True, header_style="green", show_lines=True)
    table.add_column("No.", style="dim", width=4)
    table.add_column("Word", min_width=10)
    table.add_column("Meaning", min_width=20)

    for index, word in enumerate(word_list, start=1):
        table.add_row(str(index), word[0], word[1])
    console.print("\n", table)


@app.command(short_help="Search word online. Use Type [medical] for Medical Dictionary.")
@yaspin(text="Wait Loading...", color="green", timer=True, spinner=Spinners.earth)
def search_online(word: str = None, type: str = "Intermediate"):
    try:
        if "medical" in type:
            API_KEY = API_KEY_MEDICAL
            dict_type = "medical"
        resp = requests.get(f"https://www.dictionaryapi.com/api/v3/references/{dict_type}/json/{word}?key={API_KEY}")
        resp = resp.json()
        word_list = dump_json(resp, word=word)
        db.insert_value(word_list)
        print_table(word_list)
    except requests.exceptions.ConnectionError as ce:
        # print(f"\n Please check internet connection: \n{ce}")
        print("\n Please check internet connection.")


@app.command(short_help="Search word in local database.")
@yaspin(text="Searhing Database...", color="green", timer=True, spinner=Spinners.earth)
def search_db(word: str = None):
    word_list = db.search_table(word=word)
    print_table(word_list)
    return word_list


@app.command(short_help="Search files for the word.")
@yaspin(text="Searhing Files...", color="green", timer=True, spinner=Spinners.earth)
def search_json(word: str = None):
    if os.path.exists(f"words/{word}.json"):
        word_list = load_json(word)
        print_table(word_list)
        return word_list


if __name__ == "__main__":
    app()
