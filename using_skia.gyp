{
  'targets': [
    {
      'configurations': {
        'Debug': { },
        'Release': { }
      },
      'target_name': 'helloskia',
      'type': 'executable',
      'dependencies': [
        'third_party/skia/gyp/skia_lib.gyp:skia_lib'
      ],
      'include_dirs': [
        'third_party/skia/include/config',
        'third_party/skia/include/core',
      ],
      'sources': [
          'app/main.cpp'
      ],
      'ldflags': [
      ],
      'cflags': [
        '-Werror', '-W', '-Wall', '-Wextra', '-Wno-unused-parameter', '-g', '-O0'
      ]
    }
  ]
}
