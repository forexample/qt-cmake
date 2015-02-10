#!/usr/bin/env python3

import os
import platform
import shutil
import subprocess
import sys

def do_call(args):
  quoted = ['"{}"'.format(x) for x in args]
  print('[{}]> {}'.format(os.getcwd(), ' '.join(quoted)))
  try:
    subprocess.check_call(args)
  except subprocess.CalledProcessError as error:
    print(error)
    print(error.output)
    sys.exit(1)
  except OSError as error:
    print(error)
    sys.exit(1)

if platform.system() == 'Windows':
  do_call(['where', 'cmake'])
else:
  do_call(['which', 'cmake'])

do_call(['cmake', '--version'])

build_dir = os.path.join(os.getcwd(), '_builds')
install_dir = os.path.join(os.getcwd(), '_install')

if os.path.exists(build_dir):
  shutil.rmtree(build_dir)

if os.path.exists(install_dir):
  shutil.rmtree(install_dir)

proj_dir = os.getcwd()

build_type = 'Release'
cpack_generator = 'NSIS'

do_call([
    'cmake',
    '-DCMAKE_BUILD_TYPE={}'.format(build_type),
    '-DCMAKE_INSTALL_PREFIX={}'.format(install_dir),
    '-Tv120_xp',
    '-GVisual Studio 12 2013 Win64',
    '-H{}'.format(proj_dir),
    '-B{}'.format(build_dir)
])

do_call([
     'cmake',
     '--build',
     build_dir,
     '--config',
     build_type,
     '--target',
     'install'
])

os.chdir(build_dir)
do_call(['cpack', '--verbose', '-C', build_type, '-G{}'.format(cpack_generator)])
