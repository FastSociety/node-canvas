#!/bin/bash

rm -rf ./node_modules/Nile-Delta
git clone --recursive git@github.com:victusfate/Nile-Delta ./node_modules/Nile-Delta
rm -rf ./node_modules/Nile-Delta/.git
rm -rf ./node_modules/Nile-Delta/package.json

node-gyp clean
`node-gyp configure` make --jobs 6 -C build

exit 0
