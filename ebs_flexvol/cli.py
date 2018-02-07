import click
import json
import volume

Success = 'Success'


@click.group()
def cli():
    pass


@cli.command()
def init():
    return json.dumps(
        {'status': Success, 'capabilities': {'attach': True}})


@cli.command()
@cli.argument('options')
@cli.argument('node')
def attach(options, node):
    return json.dumps(
        {'status': Success, 'device': '/dev/xvdf'})


@cli.command()
@cli.argument('device_name')
@cli.argument('node')
def detach(device_name, node):
    return json.dumps({'status': Success})


@cli.command()
@cli.argument('options')
@cli.argument('node')
def isattached(options, node):
    return json.dumps({'status': Success, 'attached': True})


@cli.command()
@cli.command()
@cli.argument('mount_device')
@cli.argument('options')
def wait_for_attach(mount_device, options):
    return json.dumps(
        {'status': Success})


