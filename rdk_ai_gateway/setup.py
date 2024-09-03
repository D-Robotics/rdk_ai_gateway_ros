import os
import sys
from setuptools import find_packages, setup

package_name = 'rdk_ai_gateway'

python_version = f"{sys.version_info.major}{sys.version_info.minor}"
apply_so_file = f'vocano_apply.cpython-{python_version}-aarch64-linux-gnu.so'
decode_so_file = f'decode.cpython-{python_version}-aarch64-linux-gnu.so'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('lib', package_name), [os.path.join('lib', apply_so_file)]),
        (os.path.join('lib', package_name), [os.path.join('lib', decode_so_file)]),
        (os.path.join('share', package_name), ['config/param.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'apply = rdk_ai_gateway.apply:main',
            'service = rdk_ai_gateway.infer:main',
            'client = rdk_ai_gateway.client:main'
        ],
    },
)
