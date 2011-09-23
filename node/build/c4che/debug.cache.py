AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
CC = ['/usr/bin/gcc']
CCDEFINES_ST = '-D%s'
CCFLAGS = ['-rdynamic', '-D_GNU_SOURCE', '-DHAVE_CONFIG_H=1', '-pthread', '-g', '-O0', '-Wall', '-Wextra']
CCFLAGS_DEBUG = ['-g']
CCFLAGS_MACBUNDLE = ['-fPIC']
CCFLAGS_RELEASE = ['-O2']
CCLNK_SRC_F = ''
CCLNK_TGT_F = ['-o', '']
CC_NAME = 'gcc'
CC_SRC_F = ''
CC_TGT_F = ['-c', '-o', '']
CC_VERSION = ('4', '5', '2')
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPP = '/usr/bin/cpp'
CPPFLAGS = ['-DHAVE_OPENSSL=1', '-DEV_FORK_ENABLE=0', '-DEV_EMBED_ENABLE=0', '-DEV_MULTIPLICITY=0', '-DX_STACKSIZE=65536', '-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64', '-DEV_MULTIPLICITY=0', '-DHAVE_FDATASYNC=1', '-DPLATFORM="linux"', '-D__POSIX__=1', '-Wno-unused-parameter', '-D_FORTIFY_SOURCE=2', '-DDEBUG']
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES_ST = '-D%s'
CXXFLAGS = ['-pthread', '-g', '-O0', '-Wall', '-Wextra']
CXXFLAGS_DEBUG = ['-g']
CXXFLAGS_RELEASE = ['-O2']
CXXLNK_SRC_F = ''
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = ''
CXX_TGT_F = ['-c', '-o', '']
DEST_BINFMT = 'elf'
DEST_CPU = 'x64'
DEST_OS = 'linux'
FULLSTATIC_MARKER = '-static'
HAVE_CEIL = 1
HAVE_CLOCK_GETTIME = 1
HAVE_CLOCK_SYSCALL = 1
HAVE_CONFIG_H = 1
HAVE_EPOLL_CTL = 1
HAVE_EVENTFD = 1
HAVE_FDATASYNC = 1
HAVE_FUTIMES = 1
HAVE_INOTIFY_INIT = 1
HAVE_KQUEUE = ()
HAVE_NANOSLEEP = 1
HAVE_OPENSSL = 1
HAVE_POLL = 1
HAVE_POLL_H = 1
HAVE_PORT_H = ()
HAVE_PREADWRITE = 1
HAVE_PTHREAD_ATFORK = 1
HAVE_PTHREAD_CREATE = 1
HAVE_READAHEAD = 1
HAVE_SELECT = 1
HAVE_SENDFILE = 1
HAVE_SYNC_FILE_RANGE = 1
HAVE_SYS_EPOLL_H = 1
HAVE_SYS_EVENTFD_H = 1
HAVE_SYS_EVENT_H = ()
HAVE_SYS_INOTIFY_H = 1
HAVE_SYS_QUEUE_H = 1
HAVE_SYS_SELECT_H = 1
LIBDIR = '/home/yanzheng/local/node/lib'
LIBPATH_ST = '-L%s'
LIBPATH_UTIL = ['/usr/lib', '/usr/local/lib']
LIB_CEIL = ['m']
LIB_CLOCK_GETTIME = ['rt']
LIB_DL = ['dl']
LIB_NANOSLEEP = ['rt']
LIB_OPENSSL = ['ssl', 'crypto']
LIB_PTHREAD = ['pthread']
LIB_PTHREAD_ATFORK = ['pthread']
LIB_PTHREAD_CREATE = ['pthread']
LIB_RT = ['rt']
LIB_ST = '-l%s'
LIB_UTIL = ['util']
LINKFLAGS = ['-pthread']
LINKFLAGS_DL = ['-rdynamic']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
PLATFORM_FILE = 'src/platform_linux.cc'
PREFIX = '/home/yanzheng/local/node'
RANLIB = '/usr/bin/ranlib'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SNAPSHOT_V8 = True
SONAME_ST = '-Wl,-h,%s'
STATICLIBPATH_ST = '-L%s'
STATICLIB_MARKER = '-Wl,-Bstatic'
STATICLIB_ST = '-l%s'
USE_DEBUG = False
USE_GDBJIT = False
USE_OPENSSL = True
USE_PROFILING = False
USE_SHARED_CARES = False
USE_SHARED_LIBEV = False
USE_SHARED_V8 = False
_VARIANT_ = 'debug'
cfg_files = ['config.h']
defines = {'HAVE_SELECT': 1, 'HAVE_SYS_INOTIFY_H': 1, 'HAVE_PORT_H': (), 'HAVE_KQUEUE': (), 'HAVE_SYS_SELECT_H': 1, 'HAVE_SYS_EVENT_H': (), 'HAVE_PREADWRITE': 1, 'HAVE_PTHREAD_CREATE': 1, 'HAVE_CEIL': 1, 'HAVE_SYS_QUEUE_H': 1, 'HAVE_SYS_EPOLL_H': 1, 'HAVE_CLOCK_SYSCALL': 1, 'HAVE_FUTIMES': 1, 'HAVE_EPOLL_CTL': 1, 'HAVE_READAHEAD': 1, 'HAVE_SYNC_FILE_RANGE': 1, 'HAVE_FDATASYNC': 1, 'HAVE_CONFIG_H': 1, 'HAVE_NANOSLEEP': 1, 'HAVE_OPENSSL': 1, 'HAVE_INOTIFY_INIT': 1, 'HAVE_SENDFILE': 1, 'HAVE_EVENTFD': 1, 'HAVE_CLOCK_GETTIME': 1, 'HAVE_POLL_H': 1, 'HAVE_PTHREAD_ATFORK': 1, 'HAVE_POLL': 1, 'HAVE_SYS_EVENTFD_H': 1}
macbundle_PATTERN = '%s.bundle'
program_PATTERN = '%s'
shlib_CCFLAGS = ['-fPIC', '-DPIC']
shlib_CXXFLAGS = ['-fPIC', '-DPIC']
shlib_LINKFLAGS = ['-shared']
shlib_PATTERN = 'lib%s.so'
staticlib_LINKFLAGS = ['-Wl,-Bstatic']
staticlib_PATTERN = 'lib%s.a'
