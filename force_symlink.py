import errno
import argparse
import pathlib
from os import listdir, remove, symlink, getcwd


parser = argparse.ArgumentParser()

parser.add_argument('instance_path', metavar = 'i',
                    type=pathlib.Path, nargs='?', help='instance_path')

parser.add_argument('target', metavar = 't',
                    type=str, nargs='?', help='target')

parser.add_argument('project_dir', metavar = 'p',
                    type=pathlib.Path, nargs='?',
                    default=pathlib.Path(getcwd()),
                    help='project_dir')


args = parser.parse_args()
print(args)

# Copyright (C) 2019 CERN.
# Copyright (C) 2019 Northwestern University.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
# MIT License
#
# Copyright (C) 2019 CERN.
# Copyright (C) 2019 Northwestern University.
# Copyright (C) 2021 TU Wien.
# Copyright (C) 2022 Forschungszentrum Jülich GmbH.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
def force_symlink(target, link_name):
    """Forcefully create symlink at link_name pointing to target."""
    output = f"Symlinked {target} successfully."
    try:
        symlink(target, link_name)
    except OSError as e:
        if e.errno == errno.EEXIST:
            remove(link_name)
            symlink(target, link_name)
            output = output + "Deleted already existing link."

    return output


target_path = args.project_dir / args.target
link_path = args.instance_path / args.target

output = force_symlink(target_path, link_path)
print(output)
