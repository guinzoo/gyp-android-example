# gyp-android-example
An example of using GYP for building native library for Android

### Prerequisites

- ninja
- environment variable NDK_DIR=/path/to/ndk

Here is an example of generating ninja files for x86 architecture on macOS

    cd app/src/main/cpp
    gyp3 -f ninja-android -DHOST=darwin -DARCH=x86 --depth . test.gyp
    
After that you can build shared library

    cd out/Default
    ninja
    
Next copy lib/libnative-lib.so to app/src/native-libs/x86/ and then you can build and run project in Android Studio.

I use GYP3, that can be found at https://github.com/refack/GYP, but original version should works too.

Building was tested on macOS and linux. For linux use -DHOST=linux.
