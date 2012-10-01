from setup_helpers import (generate_a_pyrex_source)

# monkey-patch numpy distutils to use Cython instead of Pyrex
from numpy.distutils.command.build_src import build_src
build_src.generate_a_pyrex_source = generate_a_pyrex_source


def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.add_subpackage('apkg', 'apkg')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = 'apkg',
          version = '0.1',
          configuration = configuration)
