#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon-keyword-plugin-YAKE=neon_keyword_plugin_YAKE:YAKEExtractor'
setup(
    name='neon-keyword-plugin-YAKE',
    version='0.0.1',
    description='A keyword extractor for ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/neon-keyword-plugin-YAKE',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='GPL',
    packages=['neon_keyword_plugin_YAKE'],
    zip_safe=True,
    keywords='mycroft plugin keyword extractor',
    entry_points={'intentbox.keywords': PLUGIN_ENTRY_POINT}
)
