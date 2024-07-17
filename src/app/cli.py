import typer
from colorama import Fore, Style
from art import text2art

from app.version import __version__, __template_version__
from app.config import settings


cli = typer.Typer()


def print_startup_logo():
    version_colored = Fore.MAGENTA + Style.BRIGHT + "v" + __version__ + Style.RESET_ALL
    template_version_colored = (
        Fore.GREEN + Style.BRIGHT + "v" + __template_version__ + Style.RESET_ALL
    )
    project_name = """.fastapi.\nstarter"""
    # other selected fonts
    # isometric1
    # alpha
    # smisome1
    # starwars
    logo = (
        Fore.CYAN
        + Style.BRIGHT
        + text2art(project_name, font="tarty1")
        + Style.RESET_ALL
    )
    print(logo)
    print(
        f"\nRunning service {version_colored} 🚀 via fastapi-starter template {template_version_colored} 📦\n"
    )


@cli.command()
def run(host: str = settings.app_api_host, port: int = settings.app_api_port):
    print_startup_logo()

    from app.main import run_service

    run_service(host, port)


@cli.command()
def version():
    print(f"🚀 {__version__}")


if __name__ == "__main__":
    cli()
