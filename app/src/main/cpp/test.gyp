{
  'conditions': [
    [ 'GENERATOR_FLAVOR=="android"', {
        'variables': {
          'ndk_dir': '<!(echo $NDK_DIR)',
          'toolchain': '<(ndk_dir)/toolchains/llvm/prebuilt/<(HOST)-x86_64',
          'api': '16',
          'conditions': [
            [ 'ARCH=="x86"', {
                'clang_prefix': 'i686-linux-android',
                'tools_prefix': 'i686-linux-android',
              },
              'ARCH=="x64"', {
                'clang_prefix': 'x86_64-linux-android',
                'tools_prefix': 'x86_64-linux-android',
              },
              'ARCH=="arm"', {
                'clang_prefix': 'armv7a-linux-androideabi',
                'tools_prefix': 'arm-linux-androideabi',
              },
              'ARCH=="arm64"', {
                'clang_prefix': 'aarch64-linux-android',
                'tools_prefix': 'aarch64-linux-android',
              },
            ],
          ],
        },
        'make_global_settings': [
          ['CC', '<(toolchain)/bin/<(clang_prefix)<(api)-clang'],
          ['CXX', '<(toolchain)/bin/<(clang_prefix)<(api)-clang++'],
          ['AR', '<(toolchain)/bin/<(tools_prefix)-ar'],
          ['NM', '<(toolchain)/bin/<(tools_prefix)-nm'],
          ['READELF', '<(toolchain)/bin/<(tools_prefix)-readelf'],
        ],
      },
    ],
  ],
  'target_defaults': {
    'sources': [
      'native-lib.cpp',
    ],
    'cflags': [
      '-fno-addrsig',
      '-fPIE',
      '-fPIC',
    ],
    'cflags_cc': [
      '-stdlib=libc++',
      '-std=c++11',
    ],
    'ldflags': [
      '-static-libstdc++',
    ],
    'conditions': [
      [ 'ARCH=="x86"', {
          'cflags': [
            #remove it if target api >= 24
            '-mstackrealign',
          ],
        },
      ],
    ],
  },
  'targets': [
    {
      'target_name': 'native-lib',
      'type': 'shared_library',
    },
  ],
}
