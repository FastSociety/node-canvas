{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'GTK_Root%': 'C:/GTK', # Set the location of GTK all-in-one bundle
        'with_jpeg%': 'false',
        'with_gif%': 'false',
        'with_pango%': 'false',
        'with_freetype%': 'false'
      }
    }, { # 'OS!="win"'
      'variables': {
        'with_jpeg%': '<!(./util/has_lib.sh jpeg)',
        'with_gif%': '<!(./util/has_lib.sh gif)',
        # disable pango as it causes issues with freetype.
        'with_pango%': 'false',
        'with_freetype%': '<!(./util/has_cairo_freetype.sh)'
      }
    }]
  ],
  'targets': [
    {
      'target_name': 'canvas',
      'sources': [
        'src/Canvas.cc',
        'src/CanvasGradient.cc',
        'src/CanvasPattern.cc',
        'src/CanvasRenderingContext2d.cc',
        'src/color.cc',
        'src/Image.cc',
        'src/ImageData.cc',
        'src/init.cc',
        'src/PixelArray.cc'
      ],
      'include_dirs+': [
        './node_modules/Nile-Delta/src/',
        '../../Nile-Delta/src/',
        '/usr/local/include'
      ],
      'defines': [
        'HAVE_JPEG'
      ],
      'cflags' : ['-g', '-DHAVE_PTHREADS', '-D__STDC_CONSTANT_MACROS', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE', '-Wall', '-std=c++0x'],      
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'libraries': [
           '<!@(pkg-config pixman-1 --libs)',  
           '<!@(pkg-config --libs cairomm-1.0)',
           '-L/usr/local/Cellar/jpeg/8d/lib -ljpeg',        
            '-lc++ -lc++abi'            
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [ '-g', '-mmacosx-version-min=10.7', '-std=c++11', '-stdlib=libc++', '-O3', '-D__STDC_CONSTANT_MACROS', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE', '-Wall' ],
            'OTHER_CPLUSPLUSFLAGS': [ '-g', '-mmacosx-version-min=10.7', '-std=c++11', '-stdlib=libc++', '-O3', '-D__STDC_CONSTANT_MACROS', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE', '-Wall' ]
          }
        }],
        ['OS=="linux"', {
          'libraries': [
            '<!@(pkg-config pixman-1 --libs)',
            '<!@(pkg-config cairo --libs)',
            '-ljpeg'
          ],
          'include_dirs': [
            '<!@(pkg-config cairo --cflags-only-I | sed s/-I//g)'
          ]        
        }]
      ]   
    }
  ]
}
