#!/usr/bin/env python

import click
import pandas as pd
from datetime import datetime

# build a click group
@click.group()
def cli():
    """A simple CLI to run different operations on dataset"""


# build a click command
@cli.command()
def describe():
    """Load the data and print the description in the terminal"""
    data = pd.read_csv("TeslaInc.csv").describe()
    print(data)

@cli.command()
@click.option(
    "--r", default="1", help="Index of row sorted by. If 1 then sort by the first row."
)
@click.option("--asc", default="1", help="If 1 then ascending, if 0 descending.")
def sort(r, asc):
    """Sort the data ascending/desceding by a chosen column."""
    data = pd.read_csv("TeslaInc.csv")
    data.Date = pd.to_datetime(data.Date)
    col = list(data.columns)[int(r) - 1]
    flag = True if asc == "1" else False
    ans = data.sort_values(by=[col], ascending=flag)
    print(ans)


# run the CLI
if __name__ == "__main__":
    cli()

