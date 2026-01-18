# examples
# requirements: idempotent
mkdirp('/','tmp','made','some','dir')

# my solutions

# not idempotent
import os
def mkdirp(*directories):
    os.makedirs('/'.join(directories));

import os
def mkdirp(*dirs):
    path = [dirs[0]]
    for d in dirs[1:]:
        path.append(d)
        if not os.path.exists('/'.join(path)):
            os.mkdir('/'.join(path))

# others
import os
def mkdirp(*directories):
    try:
        os.makedirs(os.path.join(*directories))
    except OSError:
        pass

import os
def mkdirp(*directories):
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
