"""
main.py

Package sw

Created by kinami on 2023-06-08
"""
import subprocess
from pathlib import Path
from typing import Annotated, Optional, List

import typer
import os

app = typer.Typer()

state = dict()


def deploy(service: str, force: bool = False, redeploy: bool = False):
    """
    Deploys the service to the swarm
    """
    if not os.path.isfile(f"{state['folder']}/{service}/{service}.yml"):
        typer.echo(f"Service {service} not found")
        return

    if os.path.isfile(f"{state['folder']}/{service}/.exclude") and not force:
        typer.echo(f"Service {service} is excluded")
        return

    if not redeploy and 'does not exist' not in subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8'):
        typer.echo(f"Service {service} is already deployed")
        return

    subprocess.run(['docker', 'stack', 'deploy', '-c', f"{state['folder']}/{service}/{service}.yml", service])


@app.command()
def d(
        service: List[str] = Annotated[Optional[List[str]], typer.Argument(..., help="The name of the service to deploy. If not provided, all services will be deployed")],
        force: bool = typer.Option(False, help="Force the deployment, even if the service is excluded"),
        redeploy: bool = typer.Option(False, help="Force redeployment if the service is already deployed")
):
    """
    Deploys the service to the swarm
    """
    for ser in service if service else os.listdir(state["folder"]):
        deploy(ser, force, redeploy)


@app.command()
def r(
        service: List[str] = Annotated[Optional[List[str]], typer.Argument(..., help="The name of the service to remove")],
):
    """
    Removes the service from the swarm
    """
    for ser in service if service else os.listdir(state["folder"]):
        subprocess.run(['docker', 'stack', 'rm', ser])


@app.command()
def s(
        service: str = typer.Argument(..., help="The name of the service"),
        truncate: bool = typer.Option(False, "-t", "--truncate", help="Truncate the output")
):
    """
    Shows the status of the service
    """
    if truncate:
        subprocess.run(['docker', 'stack', 'ps', service])
    else:
        subprocess.run(['docker', 'stack', 'ps', service, '--no-trunc'])


@app.callback()
def main(folder: Path = typer.Option("~/mistborn/services", help="The folder containing the services")):
    """
    Small utility for managing services in a swarm easily
    """
    state["folder"] = folder


if __name__ == "__main__":
    app()
