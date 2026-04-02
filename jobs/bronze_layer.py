import sys
from awsglue.utils import getResolvedOptions

from src.constants import name

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'SOURCE_PATH',
    'TARGET_PATH',
    'SECRET_NAME'
])

source_path = args['SOURCE_PATH']
target_path = args['TARGET_PATH']
secret_name = args['SECRET_NAME']
print(source_path)
print(target_path)
print("Name: ", name)


