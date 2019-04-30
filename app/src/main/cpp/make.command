#!/bin/bash
cd `dirname $0`
gyp3 -f ninja-android -DHOST=darwin -DARCH=x86 --depth . test.gyp
