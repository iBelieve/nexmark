project('nexmark', 'cpp', version: '0.0.1')

add_global_arguments('-Wall', '-Wunused-variable', '-Wunreachable-code',
                     language: 'cpp')

compiler = meson.get_compiler('cpp')

qt5 = import('qt5')

qt5_dep = dependency('qt5', modules: ['Core', 'Gui', 'Quick', 'Sql', 'Xml', 'XmlPatterns'])

kf5_components_needed = [
    'Archive',
]

kf5_deps = []

foreach kde_component: kf5_components_needed
    dep_tmp_lib = compiler.find_library('KF5' + kde_component)
    dep_tmp_kf5 = declare_dependency(
        dependencies: [
            dep_tmp_lib,
        ],
        include_directories: [
            include_directories('/usr/include/KF5/K' + kde_component),
        ],
    )
    kf5_deps += dep_tmp_kf5
endforeach

inc = include_directories('src')

resources = qt5.preprocess(moc_headers: ['src/book.h', 'src/booksmanager.h', 'src/epubfile.h'],
                           qresources: 'src/app.qrc',
                           include_directories: inc)

executable('nexmark',
           'src/main.cpp', 'src/book.cpp', 'src/booksmanager.cpp', 'src/epubfile.cpp',
           resources,
           include_directories: inc,
           dependencies: [qt5_dep, kf5_deps],
           install: true)
