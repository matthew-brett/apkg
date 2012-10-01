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
