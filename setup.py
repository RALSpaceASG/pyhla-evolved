from setuptools import setup, find_packages, Extension

rti = Extension('_rti',
                sources=['hla/_rti/exceptions.cpp',
                         'hla/_rti/federateambassador.cpp',
                         'hla/_rti/handles.cpp',
                         'hla/_rti/module.cpp',
                         'hla/_rti/rtiambassador.cpp'],
                define_macros=[('RTI_USES_STD_FSTREAM', None)],
                libraries=['RTI-NG', 'FedTime'])

omt = Extension('_omt',
                sources=['hla/_omt/basicdata.cpp',
                         'hla/_omt/module.cpp'])

setup(
    name="pyhla-evolved",
    version="0.1",
    packages=find_packages(),
    ext_package='hla',
    ext_modules=[rti, omt]
)
