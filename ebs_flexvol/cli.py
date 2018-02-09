from __future__ import print_function

import click
import json
import logging
import volume
import sys

log = logging.getLogger('ebs-flexvol')


class Result(object):
    Success = "Success"
    Error = "Failure"
    NotSupported = "Not supported"


def error(msg):
    result = json.dumps(msg)
    log.info("err response: %s", result)
    click.echo(result, err=True)
    sys.exit(1)


def output(msg):
    result = json.dumps(msg)
    log.info("result response: %s", result)
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
    return output({'status': Result.Success, 'capabilities': {'attach': True}})


@cli.command()
@click.argument('params')
def getvolumename(params):
    params = json.loads(params)
    if 'volumeId' not in params:
        error({
            'status': Result.Error,
            'reason': 'missing volume-id in volume spec/request'})
    output({
        'status': Result.Success, 'volumeName': params['volumeId']})


@cli.command()
@click.argument('params')
@click.argument('node')
def attach(params, node):
    return output({'status': Result.Success, 'device': '/dev/xvdf'})


@cli.command()
@click.argument('device_name')
@click.argument('node')
def detach(device_name, node):
    return output({'status': Result.Success})


@cli.command()
@click.argument('options')
@click.argument('node')
def isattached(options, node):
    return output({'status': Result.Success, 'attached': True})


@cli.command()
@click.argument('mount_device')
@click.argument('options')
def waitforattach(mount_device, options):
    return output({'status': Result.Success})


@cli.command()
@click.argument('mount_device')
@click.argument('options')
def waitfordetach(mount_device, options):
    return output({'status': Result.Success})


@cli.command()
@click.argument("x")
@click.argument("y")
def mount(x, y):
    return output({'status': Result.Success})


@cli.command()
@click.argument("x")
@click.argument("y")
def unmount(x, y):
    return output({'status': Result.Success})

