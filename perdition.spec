Summary:	Mail Retrieval Proxy
Name:		perdition
Version:	0.1.5
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.vergenet.net/pub/perdition/%{name}-%{version}.tar.gz
URL:		http://vergenet.net/linux/perdition/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perdition is allows users to connect to a content-free POP3 or IMAP4
server that will redirect them to their real POP3 or IMAP4 server.
This enables mail retrieval for a domain to be split across multiple
backend servers on a per user basis. This can also be used to as a
POP3 or IMAP4 proxy especially in firewall applications. Perdition
supports arbitrary library based map access to determine the server
for a user. POSIX Regular Expression, GDBM and MySQL libraries ship
with the distribution.

%package devel
Summary:	Headers and static libraries for perditiondb library development
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}-%{release}

%description devel
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
headers and libraries that may be useful in the development of
perditiondb librarys.

%package libtcp_socket
Summary:	Library to imliment simple TCP client/server connections
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
License:	LGPL
Provides:	%{name}-libtcp_socket = %{version}-%{release}

%description libtcp_socket
Library that allows fast imlementation of tcp client/server
conenctions. The library provides calls to set up and listen on a
port, connect to a port and transfer data between a listening server
port and a connected client port.

%package libtcp_socket-devel
Summary:	Headers and static libraries required to compile against libtcp_socket
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
License:	LGPL
Requires:	%{name}-libtcp_socket = %{version}-%{release}

%description libtcp_socket-devel
Headers and static libraries required when writing programmes that use
libtcp_socket.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{,etc/{,rc.d/init.d,perdition/{mysql,postgresql},pam.d}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etc/rc.d/init.d/perdition $RPM_BUILD_ROOT/etc/rc.d/init.d/perdition
install etc/pam.d/perdition $RPM_BUILD_ROOT/etc/pam.d/perdition
  
install etc/perdition/mysql/makedb $RPM_BUILD_ROOT%{_sysconfdir}/perdition/mysql/makedb
install etc/perdition/mysql/perdition.sql $RPM_BUILD_ROOT%{_sysconfdir}/perdition/mysql/perdition.sql

install perdition-%{version}%{_sysconfdir}/perdition/postgresql/makedb \
	$RPM_BUILD_ROOT%{_sysconfdir}/perdition/postgresql/makedb

install etc/perdition/popmap $RPM_BUILD_ROOT%{_sysconfdir}/perdition/popmap
install etc/perdition/popmap.re $RPM_BUILD_ROOT%{_sysconfdir}/perdition/popmap.re
install etc/perdition/Makefile $RPM_BUILD_ROOT%{_sysconfdir}/perdition/Makefile
install etc/perdition/perdition.conf $RPM_BUILD_ROOT%{_sysconfdir}/perdition/perdition.conf
install etc/perdition/Makefile $RPM_BUILD_ROOT%{_sysconfdir}/perdition/Makefile

ln -s perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.0
ln -s perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
make -q	-C /etc/perdition/
DESC="perdition daemon"; %chkconfig_add

%preun
%chkconfig_del

%postun -p /sbin/ldconfig

%post   libtcp_socket -p /sbin/ldconfig
%postun libtcp_socket -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.perditiondb AUTHORS ChangeLog NEWS CODING_LOCATIONS TODO
%attr(755,root,root) %{_bindir}/makegdbm
%attr(755,root,root) %{_sbindir}/perdition
%attr(755,root,root) %{_sbindir}/perdition.0
%attr(755,root,root) %{_sbindir}/perdition.1
%attr(755,root,root) %{_libdir}/libjain.so.*.*
%attr(755,root,root) %{_libdir}/libperdition_adt.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_gdbm.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_mysql.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_postgresql.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_posix_regex.so.*.*
/etc/pam.d/perdition
%attr(754,root,root) /etc/rc.d/init.d/perdition

%{_sysconfdir}/perdition/Makefile
%config %{_sysconfdir}/perdition/popmap
%config %{_sysconfdir}/perdition/popmap.re
%config %{_sysconfdir}/perdition/perdition.conf
%config %{_sysconfdir}/perdition/mysql/makedb
%config %{_sysconfdir}/perdition/mysql/perdition.sql
%config %{_sysconfdir}/perdition/postgresql/makedb

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files libtcp_socket
%defattr(644,root,root,755)
%doc libtcp_pipe/COPYING AUTHORS
%attr(755,root,root) %{_libdir}/libtcp_socket.so.*.*

%files libtcp_socket-devel
%defattr(644,root,root,755)
%{_includedir}/tcp_socket.h
%{_libdir}/libtcp_socket.a
%{_libdir}/libtcp_socket.la
