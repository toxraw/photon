Summary:        SQLite: An Embeddable SQL Database Engine
Name:           sqlite2
Version:        2.8.17
Release:        1%{?dist}
URL:            http://www.sqlite.org
License:        Public Domain
Group:          System Environment/GeneralLibraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        ftp://ftp.za.freebsd.org/openbsd/distfiles/sqlite-%{version}.tar.gz
%define sha1    sqlite=75db1cf3b00ea18ae8528e676fc9fdf698e2fe58

%description
SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. SQLite is the most used database engine in the world.

%package devel
Summary: Headers and development libraries for sqlite2
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Headers and development libraries for sqlite2

%prep
%setup -q -n sqlite-%{version}

%build
./configure \
       --prefix=%{_prefix}  \
       --mandir=%{_mandir}  \
       --enable-threads     \
       --enable-shared      \
       --enable-symbols
make %{?_smp_mflags}

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libsqlite.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libsqlite.a
%{_libdir}/libsqlite.la
%{_libdir}/libsqlite.so

%changelog
*   Wed Apr 12 2017 Xiaolin Li <xiaolinl@vmware.com>  2.8.17-1
-   Initial build.  First version
