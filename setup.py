from setuptools import setup, find_packages, Extension

rti = Extension('_rti',
                sources=['src/_rti/exceptions.cpp',
                         'src/_rti/federateambassador.cpp',
                         'src/_rti/handles.cpp',
                         'src/_rti/module.cpp',
                         'src/_rti/rtiambassador.cpp'],
                define_macros=[('RTI_USES_STD_FSTREAM', None)],
                libraries=['RTI-NG', 'FedTime'])

omt = Extension('_omt',
                sources=['src/_omt/basicdata.cpp',
                         'src/_omt/module.cpp'])

setup(
    name="pyhla-evolved",
    version="0.1",
    packages=find_packages(),
    ext_package='hla',
    ext_modules=[rti, omt]
)
