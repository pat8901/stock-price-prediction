"""Console script for stock_price_prediction."""

import stock
import typing

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    stock.helloWorld()


if __name__ == "__main__":
    app()
