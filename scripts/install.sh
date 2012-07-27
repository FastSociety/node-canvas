#!/bin/bash
#npm install Nile-Delta
wget -O ./src/logStream.h https://raw.github.com/victusfate/Nile-Delta/master/src/logStream.h

node-gyp rebuild

exit 0
