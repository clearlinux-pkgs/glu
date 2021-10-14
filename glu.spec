#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glu
Version  : 9.0.2
Release  : 19
URL      : https://mesa.freedesktop.org/archive/glu/glu-9.0.2.tar.gz
Source0  : https://mesa.freedesktop.org/archive/glu/glu-9.0.2.tar.gz
Summary  : Mesa OpenGL Utility library
Group    : Development/Tools
License  : SGI-B-1.0
Requires: glu-filemap = %{version}-%{release}
Requires: glu-lib = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkg-config

%description
No detailed description available

%package dev
Summary: dev components for the glu package.
Group: Development
Requires: glu-lib = %{version}-%{release}
Provides: glu-devel = %{version}-%{release}
Requires: glu = %{version}-%{release}

%description dev
dev components for the glu package.


%package dev32
Summary: dev32 components for the glu package.
Group: Default
Requires: glu-lib32 = %{version}-%{release}
Requires: glu-dev = %{version}-%{release}

%description dev32
dev32 components for the glu package.


%package filemap
Summary: filemap components for the glu package.
Group: Default

%description filemap
filemap components for the glu package.


%package lib
Summary: lib components for the glu package.
Group: Libraries
Requires: glu-filemap = %{version}-%{release}

%description lib
lib components for the glu package.


%package lib32
Summary: lib32 components for the glu package.
Group: Default

%description lib32
lib32 components for the glu package.


%prep
%setup -q -n glu-9.0.2
cd %{_builddir}/glu-9.0.2
pushd ..
cp -a glu-9.0.2 build32
popd
pushd ..
cp -a glu-9.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634253825
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1634253825
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/glu.h
/usr/lib64/libGLU.so
/usr/lib64/pkgconfig/glu.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libGLU.so
/usr/lib32/pkgconfig/32glu.pc
/usr/lib32/pkgconfig/glu.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-glu

%files lib
%defattr(-,root,root,-)
/usr/lib64/libGLU.so.1
/usr/lib64/libGLU.so.1.3.1
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libGLU.so.1
/usr/lib32/libGLU.so.1.3.1
