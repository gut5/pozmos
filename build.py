#!/usr/bin/env python3

import argparse
import logging

from nxsd.package import NXSDPackage
from nxsd.components import atmosphere
from nxsd.components import hekate
from nxsd.components import homebrew
from nxsd.components import sigpatches
from nxsd.components import checkpoint
from nxsd.components import tinfoil


logger = logging.getLogger('nxsd')


def main():
    commands = {
        'build': build,
        'clean': clean,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', 
        help='enable verbose logging output to log/build.log')
    parser.add_argument('command', nargs='?', default='build', 
        choices=commands.keys(),
        help='build command to execute. options: build, clean (default: build)')

    args = parser.parse_args()

    if args.verbose == True:
        logger.setLevel(logging.DEBUG)
        logger.debug('Verbose logging enabled.')
    
    commands[args.command](args)

def build(args):
    packages = get_packages()
    for package in packages:
        package.build_components()
        logger.info('Created {name} package!'.format(name=package.name))

def clean(args):
    packages = get_packages()
    for package in packages:
        package.clean()
        logger.info('Cleaned {name} package!'.format(name=package.name))
    pass

def get_packages():
    nxsd_core = NXSDPackage(
        name='nxsd-core',
        build_directory='build/core/',
        output_filename='nx-sd.zip',
    )
    nxsd_core.components = [
        atmosphere,
        hekate,
        homebrew,
        sigpatches,
    ]

    nxsd_addon = NXSDPackage(
        name='nxsd-addon',
        build_directory='build/addon/',
        output_filename='nx-sd-addon.zip',
    )
    nxsd_addon.components = [
        checkpoint, 
        tinfoil
    ]

    return [nxsd_core, nxsd_addon]


if __name__ == '__main__':
    main()
