#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

version = platform.python_version()
arch = platform.architecture()
processor = platform.processor()
system = platform.system()
user = platform.uname()
print('This is python version {}'.format(version))
print('this is architecture {}'.format(arch))
print(f'this is processor {processor}')
print('this is system {}'.format(system))
print('user is {}'.format(user))
