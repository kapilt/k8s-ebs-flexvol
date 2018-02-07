import logging

import boto3
import contextlib
import fnmatch
import os
import string

from botocore.vendored import requests


log = logging.getLogger('bunker.volumemgr')


class VolumeManager(object):

    def __init__(self):
        self.session = boto3.Session()
        self.client = self.session.client('ec2')
        self.instance_id = None
        self.zone = None

    @contextlib.contextmanager
    def attach(self, **params):
        # pass either Size and Kms params or SnapshotId
        params['AvailabilityZone'] = self.zone
        params['VolumeType'] = 'gp2'

        vol_id = self.client.create_volume(**params).get('VolumeId')

        log.info(
            "Created Volume %s Zone %s Tags %s",
            vol_id, self.zone, str("na"))
        waiter = self.client.get_waiter('volume_available')
        waiter.wait(VolumeIds=[vol_id])
        device_name = next_device_name()

        try:
            self.client.attach_volume(
                InstanceId=self.instance_id,
                VolumeId=vol_id,
                Device=device_name)
            waiter = self.client.get_waiter('volume_in_use')
            waiter.wait(VolumeIds=[vol_id])
            yield vol_id, device_name
        finally:
            self.client.detach_volume(VolumeId=vol_id, Force=True)
            waiter = self.client.get_waiter('volume_available')
            waiter.wait(VolumeIds=[vol_id])
            self.client.delete_volume(VolumeId=vol_id)


def next_device_name():
    devs = fnmatch.match(os.listdir('/dev'), 'xv*')
    devs.sort()
    idx = string.ascii_lowercase.index(devs[-1][0])
    return '/dev/xvd%s' % string.ascii_lowercase[idx]
