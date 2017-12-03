project('nexmark', 'cpp', version: '0.0.1')

qt5 = import('qt5')

qt5_dep = dependency('qt5', modules: ['Core', 'Gui', 'Quick', 'Sql'])

inc = include_directories('src')

resources = qt5.preprocess(moc_headers: 'src/booksmanager.h',
                           qresources: 'src/app.qrc',
                           include_directories: inc)

executable('nexmark', 'src/main.cpp', 'src/booksmanager.cpp', resources,
           include_directories: inc,
           dependencies: qt5_dep,
           install: true)
