"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import pulumilibs
from pulumilibs import *


main = Vpc("test","10.0.0.0/16")

pulumi.export("vpc_id", main.vpc.id)