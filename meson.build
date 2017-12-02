project('nexmark', version: '0.0.1')

project_id = 'io.mspencer.Nexmark'

python = import('python3')
gnome = import('gnome')

message('Looking for dependencies')
python_bin = python.find_python()
if not python_bin.found()
  error('No valid python3 binary found')
else
  message('Found python3 binary')
endif

dependency('glib-2.0')
dependency('gobject-introspection-1.0')
dependency('gtk+-3.0')

bindir = join_paths(get_option('prefix'), get_option('bindir'))
libdir = join_paths(get_option('prefix'), get_option('libdir'))
datadir = join_paths(get_option('prefix'), get_option('datadir'))

python_dir = join_paths(get_option('prefix'), python.sysconfig_path('purelib'))
pkgdatadir = join_paths(datadir, meson.project_name())
pkglibdir = join_paths(libdir, meson.project_name())
schemadir = join_paths(datadir, 'glib-2.0', 'schemas')

conf = configuration_data()
conf.set('VERSION', meson.project_version())
conf.set('BIN_DIR', bindir)
conf.set('DATA_DIR', pkgdatadir)
conf.set('LIB_DIR', pkglibdir)
conf.set('PYTHON', python_bin.path())

subdir('data')

install_subdir('nexmark', install_dir: python_dir)

configure_file(input: 'nexmark.in', output: 'nexmark', configuration: conf, install_dir: bindir)
install_data(sources: 'startnexmark', install_dir: bindir)

meson.add_install_script('meson/meson-postinstall.sh')
