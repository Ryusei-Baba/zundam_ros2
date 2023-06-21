from setuptools import setup

package_name = 'zundam_service'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryusei Baba',
    maintainer_email='babaryusei.kw@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zundam_service_node = zundam_service.zundam_service_node:main',
            'zundam_client_node = zundam_service.zundam_client_node:main',
        ],
    },
)
