"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws

config = pulumi.Config()


conf = pulumi.Config('core-infra')

stack_ref = pulumi.StackReference(f"organization/{conf.require('core-project-name')}/dev")

vpc_id = stack_ref.require_output('vpc_id')


subnet = aws.ec2.Subnet("test_subnet",
    vpc_id=vpc_id,
    cidr_block="10.0.0.0/24",
    availability_zone="us-east-1a",
    tags={
        "Name": "tf-example",
    })


amzn_linux_2023_ami = aws.ec2.get_ami(most_recent=True,
    owners=["amazon"],
    filters=[{
        "name": "name",
        "values": ["al2023-ami-2023.*-x86_64"],
    }])

foo_instance = aws.ec2.Instance("foo",
    ami=amzn_linux_2023_ami.id,
    instance_type=aws.ec2.InstanceType.T2_MICRO,
    subnet_id=subnet.id,
    credit_specification={
        "cpu_credits": "unlimited",
    })