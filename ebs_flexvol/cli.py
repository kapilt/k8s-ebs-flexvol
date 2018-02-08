import click
import json
import logging
import volume
import sys

Success = 'Success'

log = logging.getLogger('ebs-flexvol')


@click.group(nvoke_without_command=True)
def cli():
    """aws ebs flexvolume"""
    logging.getLogger('boto3').setLevel(logging.WARNING)
    logging.basicConfig(
        filename='/flexdriver.log',
        level=logging.INFO,
        format="%(asctime)s: %(name)s:%(levelname)s %(message)s")
    log.info("invoked %s", sys.argv)


@cli.command()
def init():
    return click.echo(json.dumps(
        {'status': Success, 'capabilities': {'attach': True}}))


@cli.command()
@click.argument('options')
@click.argument('node')
def attach(options, node):
    return click.echo(json.dumps(
        {'status': Success, 'device': '/dev/xvdf'}))


@cli.command()
@click.argument('device_name')
@click.argument('node')
def detach(device_name, node):
    return click.echo(json.dumps({'status': Success}))


@cli.command()
@click.argument('options')
@click.argument('node')
def isattached(options, node):
    return click.echo(json.dumps({'status': Success, 'attached': True}))


@cli.command()
@click.argument('mount_device')
@click.argument('options')
def wait_for_attach(mount_device, options):
    return click.echo(json.dumps(
        {'status': Success}))


