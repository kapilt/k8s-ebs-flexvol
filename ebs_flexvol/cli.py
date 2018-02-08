from __future__ import print_function

import click
import json
import hashlib
import logging
import volume
import sys

log = logging.getLogger('ebs-flexvol')


class Result(object):
    Success = "Success"
    Error = "Failure"
    NotSupported = "Not supported"


def error(msg):
    print(json.dumps(msg), file=sys.stderr)
    sys.exit(1)


def output(msg):
    print(json.dumps(msg), file=sys.stdout)
    sys.exit(0)


@click.group()
def cli():
    """aws ebs flexvolume"""
    logging.basicConfig(
        filename='/flexdriver.log',
        level=logging.INFO,
        format="%(asctime)s: %(name)s:%(levelname)s %(message)s")
    log.info("invoked %s", sys.argv)


@cli.command()
def init():
    return click.echo(json.dumps(
        {'status': Result.Success, 'capabilities': {'attach': True}},
        indent=2))


@cli.command()
@click.argument('params')
def getvolumename(params):
    params = json.loads(params)
    return click.echo(json.dumps({
        'status': Result.NotSupported}))

    click.echo(json.dumps({
        'status': Result.Success,
        'volumeName': hashlib.md5(
            params.get('kubernetes.io/pvOrVolumeName', '')).hexdigest()},
                          indent=2))


@cli.command()
@click.argument('params')
@click.argument('node')
def attach(params, node):
    return click.echo(json.dumps(
        {'status': Result.Success, 'device': '/dev/xvdf'}, indent=2))


@cli.command()
@click.argument('device_name')
@click.argument('node')
def detach(device_name, node):
    return click.echo(json.dumps(
        {'status': Result.Success}, indent=2))


@cli.command()
@click.argument('options')
@click.argument('node')
def isattached(options, node):
    return click.echo(json.dumps(
        {'status': Result.Success, 'attached': True}, indent=2))


@cli.command()
@click.argument('mount_device')
@click.argument('options')
def waitforattach(mount_device, options):
    return click.echo(json.dumps(
        {'status': Result.Success}, indent=2))


@cli.command()
@click.argument('mount_device')
@click.argument('options')
def waitfordetach(mount_device, options):
    return click.echo(json.dumps(
        {'status': Result.Success}, indent=2))


@cli.command()
@click.argument("x")
@click.argument("y")
def mount(x, y):
    return click.echo(json.dumps(
        {'status': Result.Success}, indent=2))


@cli.command()
@click.argument("x")
@click.argument("y")
def unmount(x, y):
    return click.echo(json.dumps(
        {'status': Result.Success}, indent=2))

