%define ver      0.1.5
%define rel      1
%define prefix   /usr

Summary: Mail Retrieval Proxy
Name: perdition
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Internet
Source: ftp://ftp.vergenet.net/pub/perdition/perdition-%{ver}.tar.gz
BuildRoot: /var/tmp/perdition-%{PACKAGE_VERSION}-root
Packager: Horms <horms@vergenet.net>
URL: http://vergenet.net/linux/perdition/
Docdir: %{prefix}/doc
Provides: perdition-%{ver}-%{rel}

%description
Perdition is allows users to connect to a content-free POP3 or IMAP4 server
that will redirect them to their real POP3 or IMAP4 server. This enables
mail retrieval for a domain to be split across multiple backend servers on
a per user basis. This can also be used to as a POP3 or IMAP4 proxy
especially in firewall applications. Perdition supports arbitrary library
based map access to determine the server for a user. POSIX Regular
Expression, GDBM and MySQL libraries ship with the distribution. 

%package devel
Summary: Headers and static libraries for perditiondb library development
Group: Development/Libraries
Requires: perdition-%{ver}-%{rel}

%description devel
Perdition allows for arbitrary user database access through
shared libraries much in the maner of NSS in glibc. This package
provides headers and libraries that may be useful in the development
of perditiondb librarys.

%package libtcp_socket
Summary: Library to imliment simple TCP client/server connections
Group: Development/Libraries
Copyright: LGPL
Provides: libtcp_socket-%{ver}-%{rel}

%description libtcp_socket
Library that allows fast imlementation of tcp client/server conenctions.
The library provides calls to set up and listen on a port, connect
to a port and transfer data between a listening server port and a 
connected client port.

%package libtcp_socket-devel
Summary: Headers and static libraries required to compile against libtcp_socket
Group: Development/Libraries
Copyright: LGPL
Requires: libtcp_socket-%{ver}-%{rel}

%description libtcp_socket-devel
Headers and static libraries required when writing programmes that
use libtcp_socket.



%prep
%setup

%build
CFLAGS="${RPM_OPT_FLAGS}" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{,etc/{,rc.d/init.d,perdition/{mysql,postgresql},pam.d},@prefix/sbin}

make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

install -m744 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/rc.d/init.d/perdition \
  ${RPM_BUILD_ROOT}/etc/rc.d/init.d/perdition
install -m744 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/pam.d/perdition \
  ${RPM_BUILD_ROOT}/etc/pam.d/perdition
  
install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/mysql/makedb \
  ${RPM_BUILD_ROOT}/etc/perdition/mysql/makedb
install -m600 \
  ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/mysql/perdition.sql \
  ${RPM_BUILD_ROOT}/etc/perdition/mysql/perdition.sql

install -m600 \
  ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/postgresql/makedb \
  ${RPM_BUILD_ROOT}/etc/perdition/postgresql/makedb

install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/popmap \
  ${RPM_BUILD_ROOT}/etc/perdition/popmap
install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/popmap.re \
  ${RPM_BUILD_ROOT}/etc/perdition/popmap.re
install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/Makefile \
  ${RPM_BUILD_ROOT}/etc/perdition/Makefile
install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/perdition.conf \
  ${RPM_BUILD_ROOT}/etc/perdition/perdition.conf
install -m600 ${RPM_BUILD_DIR}/perdition-%{ver}/etc/perdition/Makefile \
  ${RPM_BUILD_ROOT}/etc/perdition/Makefile

cd ${RPM_BUILD_ROOT}/usr/sbin
ln -s perdition perdition.0
ln -s perdition perdition.1

%clean
rm -rf $RPM_BUILD_DIR/perdition-%{ver}
rm -rf $RPM_BUILD_ROOT

%post
make -q	-C /etc/perdition/
/sbin/chkconfig --add perdition

%postun

%preun
/sbin/chkconfig --del perdition

%files
%defattr(-,root,root)
%doc README README.perditiondb AUTHORS ChangeLog NEWS CODING_LOCATIONS TODO
%attr(755,root,root) %{prefix}/bin/makegdbm
%attr(755,root,root) %{prefix}/sbin/perdition
%attr(755,root,root) %{prefix}/sbin/perdition.0
%attr(755,root,root) %{prefix}/sbin/perdition.1
%attr(755,root,root) %{prefix}/lib/libjain.so
%attr(755,root,root) %{prefix}/lib/libjain.so.0
%attr(755,root,root) %{prefix}/lib/libjain.so.0.0.0
%attr(755,root,root) %{prefix}/lib/libperdition_adt.so
%attr(755,root,root) %{prefix}/lib/libperdition_adt.so.0
%attr(755,root,root) %{prefix}/lib/libperdition_adt.so.0.0.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_gdbm.so
%attr(755,root,root) %{prefix}/lib/libperditiondb_gdbm.so.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_gdbm.so.0.0.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_mysql.so
%attr(755,root,root) %{prefix}/lib/libperditiondb_mysql.so.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_mysql.so.0.0.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_postgresql.so
%attr(755,root,root) %{prefix}/lib/libperditiondb_postgresql.so.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_postgresql.so.0.0.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_posix_regex.so
%attr(755,root,root) %{prefix}/lib/libperditiondb_posix_regex.so.0
%attr(755,root,root) %{prefix}/lib/libperditiondb_posix_regex.so.0.0.0
/etc/pam.d/perdition
/etc/rc.d/init.d/perdition
/etc/perdition/Makefile
%config /etc/perdition/popmap
%config /etc/perdition/popmap.re
%config /etc/perdition/perdition.conf
%config /etc/perdition/mysql/makedb
%config /etc/perdition/mysql/perdition.sql
%config /etc/perdition/postgresql/makedb

%files devel
%attr(644,root,root) %{prefix}/include/dynamic_array.h
%attr(644,root,root) %{prefix}/include/jain.h
%attr(644,root,root) %{prefix}/include/key_value.h
%attr(644,root,root) %{prefix}/include/perdition_adt.h
%attr(644,root,root) %{prefix}/include/queue.h
%attr(644,root,root) %{prefix}/lib/libjain.a
%attr(644,root,root) %{prefix}/lib/libjain.la
%attr(644,root,root) %{prefix}/lib/libperdition_adt.a
%attr(644,root,root) %{prefix}/lib/libperdition_adt.la
%attr(644,root,root) %{prefix}/lib/libperditiondb_gdbm.a
%attr(644,root,root) %{prefix}/lib/libperditiondb_gdbm.la
%attr(644,root,root) %{prefix}/lib/libperditiondb_mysql.a
%attr(644,root,root) %{prefix}/lib/libperditiondb_mysql.la
%attr(644,root,root) %{prefix}/lib/libperditiondb_posix_regex.a
%attr(644,root,root) %{prefix}/lib/libperditiondb_posix_regex.la


%files libtcp_socket
%doc libtcp_pipe/COPYING AUTHORS
%attr(755,root,root) %{prefix}/lib/libtcp_socket.so
%attr(755,root,root) %{prefix}/lib/libtcp_socket.so.0
%attr(755,root,root) %{prefix}/lib/libtcp_socket.so.0.0.0

%files libtcp_socket-devel
%attr(644,root,root) %{prefix}/include/tcp_socket.h
%attr(644,root,root) %{prefix}/lib/libtcp_socket.a
%attr(644,root,root) %{prefix}/lib/libtcp_socket.la

%changelog
* Thu Apr 20 2000 Horms <horms@vergenet.net>
- added postgresql files

* Tue Jan  4 2000 Horms <horms@vergenet.net>
- added libraries
- added headers
- made devel package
- made libtcp_socket and libtcp_socket-devel package
- Included mysql and posix_regex stuff in /etc

* Mon Nov 29 1999 Horms <horms@vergenet.net>
- Added perdition.conf

* Sat Sep 18 1999 Horms <horms@vergenet.net>
- updated for 0.1.0

* Sat May 29 1999 Horms <horms@vergenet.net>
- inital release
