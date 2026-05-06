# __main__.py

import pulumi
from components import RegionalBucket

regions = ["us-east-1", "us-west-2"]

buckets = [
    RegionalBucket(f"lab-{regions[0]}", region=regions[0], lifecycle_days=60,  bucket_name_prefix="mlops-"),
    RegionalBucket(f"lab-{regions[1]}", region=regions[1], lifecycle_days=120, bucket_name_prefix="mlops-"),
]

pulumi.export("bucket_arns", {r: b.bucket.arn for r, b in zip(regions, buckets)})