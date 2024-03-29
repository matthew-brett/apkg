def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('apkg', parent_package, top_path)
    config.add_extension('anext',
                         sources=['anext.c'])
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    config = configuration(top_path='').todict()
    setup(**config)
