Summary:	Mail Retrieval Proxy
Summary(pl):	Proxy do ¶ci±gania poczty
Name:		perdition
Version:	1.13
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.vergenet.net/linux/perdition/download/latest/%{name}-%{version}.tar.gz
# Source0-md5:	1b2d9baf96504d000587ea8b9afd4222
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-daemon.patch
Patch2:		%{name}-unknowndebug.patch
URL:		http://www.vergenet.net/linux/perdition/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
# ps2pdf
BuildRequires:	ghostscript
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-tex-babel
BuildRequires:	unixODBC-devel
BuildRequires:	vanessa_adt-devel >= 0.0.4
BuildRequires:	vanessa_logger-devel >= 0.0.4
BuildRequires:	vanessa_socket-devel >= 0.0.5
PreReq:		rc-scripts
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-gdbm = %{version}-%{release}
Requires:	vanessa_adt >= 0.0.4
Requires:	vanessa_logger >= 0.0.4
Requires:	vanessa_socket >= 0.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perdition allows users to connect to a content-free POP3 or IMAP4
server that will redirect them to their real POP3 or IMAP4 server.
This enables mail retrieval for a domain to be split across multiple
backend servers on a per user basis. This can also be used to as a
POP3 or IMAP4 proxy especially in firewall applications. Perdition
supports arbitrary library based map access to determine the server
for a user. POSIX Regular Expression, GDBM and MySQL libraries ship
with the distribution.

%description -l pl
Perdition pozwala u¿ytkownikom ³±czyæ siê z nie zawieraj±cym nic
serwerem POP3 lub IMAP4, który przekierowuje ich do prawdziwego
serwera POP3 lub IMAP4. Pozwala to na ¶ci±ganie poczty dla domen
rozbitych na wiele serwerów na podstawie nazwy u¿ytkownika. Mo¿e byæ
tak¿e u¿ywane jako proxy POP3 lub IMAP4 na firewallach. Perdition
pozwala u¿yæ dowolnej biblioteki do przypisywania serwerów
u¿ytkownikom. W dystrybucji s± biblioteki do wyra¿eñ regularnych
zgodnych z POSIX oraz baz GDBM i MySQL.

%package bdb
Summary:	BerkeleyDB database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy BerkeleyDB dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description bdb
BerkeleyDB database library for perdition.

%description bdb -l pl
Biblioteka obs³uguj±ca bazy BerkeleyDB dla perdition.

%package gdbm
Summary:	GDBM database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy GDBM dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
GDBM database library for perdition.

%description gdbm -l pl
Biblioteka obs³uguj±ca bazy GDBM dla perdition.

%package ldap
Summary:	LDAP database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy LDAP dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ldap
LDAP database library for perdition.

%description ldap -l pl
Biblioteka obs³uguj±ca bazy LDAP dla perdition.

%package mysql
Summary:	MySQL database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy MySQL dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL database library for perdition.

%description mysql -l pl
Biblioteka obs³uguj±ca bazy MySQL dla perdition.

%package nis
Summary:	NIS database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy NIS dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description nis
NIS database library for perdition.

%description nis -l pl
Biblioteka obs³uguj±ca bazy NIS dla perdition.

%package odbc
Summary:	ODBC database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy ODBC dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description odbc
ODBC database library for perdition.

%description odbc -l pl
Biblioteka obs³uguj±ca bazy ODBC dla perdition.

%package postgresql
Summary:	PostgreSQL database library for perdition
Summary(pl):	Biblioteka obs³uguj±ca bazy PostgreSQL dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description postgresql
PostgreSQL database library for perdition.

%description postgresql -l pl
Biblioteka obs³uguj±ca bazy PostgreSQL dla perdition.

%package devel
Summary:	Headers for perditiondb library development
Summary(pl):	Pliki nag³ówkowe do bibliotek permitiondb
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
headers that may be useful in the development of perditiondb
libraries.

%description devel -l pl
Perdition pozwala na u¿ycie dowolnych bibliotek dostêpu poprzez
biblioteki dzielone w stylu glibcowych NSS. Ten pakiet dostarcza
pliki nag³ówkowe przydatne do robienia bibliotek permitiondb.

%package static
Summary:	Static jain library
Summary(pl):	Biblioteka statyczne jain
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of jain library, which may be
(rarely) useful in the development of perditiondb libraries.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki jain, która mo¿e byæ
(rzadko jednak) przydatna przy tworzeniu bibliotek perditiondb.

%prep
%setup -q
%patch -p1
%patch1 -p0
%patch2 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ldap-schema-directory=/etc/openldap/schema

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sysconfdir}/perdition,/etc/pam.d,/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/perdition
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/perdition

ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.0
ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.1

rm -f $RPM_BUILD_ROOT%{_libdir}/libperditiondb_*.{so,la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add perdition
%{__make} -q -C /etc/perdition
if [ -f /var/lock/subsys/perdition.imap -o -f /var/lock/subsys/perdition.pop ]; then
	/etc/rc.d/init.d/perdition restart
else
	echo "Run \"/etc/rc.d/init.d/perdition start\" to start perdition daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del perdition
	/etc/rc.d/init.d/perdition stop
fi

%postun -p /sbin/ldconfig

%post	bdb -p /sbin/ldconfig
%postun	bdb -p /sbin/ldconfig

%post	gdbm -p /sbin/ldconfig
%postun	gdbm -p /sbin/ldconfig

%post	ldap -p /sbin/ldconfig
%postun	ldap -p /sbin/ldconfig

%post	mysql -p /sbin/ldconfig
%postun	mysql -p /sbin/ldconfig

%post	nis -p /sbin/ldconfig
%postun	nis -p /sbin/ldconfig

%post	odbc -p /sbin/ldconfig
%postun	odbc -p /sbin/ldconfig

%post	postgresql -p /sbin/ldconfig
%postun	postgresql -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS CODING_LOCATIONS TODO
%attr(755,root,root) %{_sbindir}/perdition*
%attr(755,root,root) %{_libdir}/libjain.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_posix_regex.so.*.*

%dir %{_sysconfdir}/perdition
%{_sysconfdir}/perdition/Makefile
%{_sysconfdir}/perdition/Makefile.popmap
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/perdition/popmap
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/perdition/popmap.re
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/perdition/perdition.conf
%attr(754,root,root) /etc/rc.d/init.d/perdition
%config(noreplace) %verify(not size mtime md5) /etc/pam.d/perdition
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/perdition

%{_mandir}/man5/perditiondb.5*
%{_mandir}/man8/perdition.8*
%{_mandir}/man8/perdition.*.8*

%files bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makebdb
%attr(755,root,root) %{_libdir}/libperditiondb_bdb.so.*.*
%{_mandir}/man1/makebdb.1*

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makegdbm
%attr(755,root,root) %{_libdir}/libperditiondb_gdbm.so.*.*
%{_mandir}/man1/makegdbm.1*

%files ldap
%defattr(644,root,root,755)
%doc perdition/db/ldap/doc/perdition_ldap.pdf
%attr(755,root,root) %{_bindir}/perditiondb_ldap_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_ldap.so.*.*
%{_mandir}/man8/perditiondb_ldap_makedb.8*
/etc/openldap/schema/perdition.schema

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perditiondb_mysql_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_mysql.so.*.*
%{_mandir}/man8/perditiondb_mysql_makedb.8*

%files nis
%defattr(644,root,root,755)
%doc perdition/db/nis/README.perditiondb_nis
%attr(755,root,root) %{_libdir}/libperditiondb_nis.so.*.*

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perditiondb_odbc_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_odbc.so.*.*
%{_mandir}/man8/perditiondb_odbc_makedb.8*

%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perditiondb_postgresql_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_postgresql.so.*.*
%{_mandir}/man8/perditiondb_postgresql_makedb.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjain.so
%{_libdir}/libjain.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjain.a
