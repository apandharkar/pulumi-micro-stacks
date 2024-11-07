"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import pulumilibs
from pulumilibs import *

#main = aws.ec2.Vpc("test", cidr_block="10.0.0.0/16")


main = Vpc("test","10.0.0.0/16")

pulumi.export("vpc_id", main.vpc.id)