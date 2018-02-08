## Kubernetes AWS EBS FlexVolume

Exploration of out tree persistent volumes.

Quite a bit of confusing material on the internet, k8s moves fast, but the internet paints in ink.

Underlying there are two core concepts from an implementor's perspective. A flexvolume provides
out of tree capabilities for attaching a volume. A storage class provides for dynamic provisioning
of the volume.

See cluster-install.yml for ansible playbook to install onto host


# Todo

- job/daemonset install


# Links


- https://github.com/kubernetes/community/blob/master/contributors/devel/flexvolume.md

- https://github.com/kubernetes/kubernetes/tree/master/pkg/volume/flexvolume

- https://docs.openshift.org/latest/install_config/persistent_storage/persistent_storage_flex_volume.html

- https://docs.openshift.org/latest/install_config/provisioners.html

- https://docs.openshift.org/latest/install_config/persistent_storage/dynamically_provisioning_pvs.html

# Blog Posts

- http://leebriggs.co.uk/blog/2017/03/12/kubernetes-flexvolumes.html

- https://developer.hpe.com/blog/doryd-a-dynamic-provisioner-for-docker-volume-plugins

- https://community.hpe.com/t5/HPE-Nimble-Storage-Tech-Blog/Dory-A-FlexVolume-Driver-that-speaks-Whale/ba-p/6986638


# Other implementations (partial)

- https://github.com/kubernetes-incubator/external-storage

- https://github.com/sysoperator/kube-vcloud-flexvolume/

- https://github.com/openstack/fuxi-kubernetes/

# Usages

- https://github.com/kubernetes/contrib/tree/master/statefulsets/zookeeper
