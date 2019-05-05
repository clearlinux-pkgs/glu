#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glu
Version  : 9.0.0
Release  : 13
URL      : ftp://ftp.freedesktop.org/pub/mesa/glu/glu-9.0.0.tar.gz
Source0  : ftp://ftp.freedesktop.org/pub/mesa/glu/glu-9.0.0.tar.gz
Summary  : Mesa OpenGL Utility library
Group    : Development/Tools
License  : SGI-B-1.0
Requires: glu-lib = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(gl)

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


%package lib
Summary: lib components for the glu package.
Group: Libraries

%description lib
lib components for the glu package.


%package lib32
Summary: lib32 components for the glu package.
Group: Default

%description lib32
lib32 components for the glu package.


%prep
%setup -q -n glu-9.0.0
pushd ..
cp -a glu-9.0.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557086585
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1557086585
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/glu.h
/usr/include/GL/glu_mangle.h
/usr/lib64/libGLU.so
/usr/lib64/pkgconfig/glu.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libGLU.so
/usr/lib32/pkgconfig/32glu.pc
/usr/lib32/pkgconfig/glu.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libGLU.so.1
/usr/lib64/libGLU.so.1.3.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libGLU.so.1
/usr/lib32/libGLU.so.1.3.1
