#
# TODO:
# - cdb, daemon subpackages
# - fix perdition_ldap.pdf build
#
Summary:	Mail Retrieval Proxy
Summary(pl.UTF-8):	Proxy do ściągania poczty
Name:		perdition
Version:	1.18
Release:	0.8
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.vergenet.net/linux/perdition/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0baec303d27073f053cc03488bf8d98b
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-daemon.patch
URL:		http://www.vergenet.net/linux/perdition/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
# ps2pdf
#BuildRequires:	ghostscript
#BuildRequires:	ghostscript-fonts-std
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	mysql-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.304
#BuildRequires:	tetex-dvips
#BuildRequires:	tetex-fonts-adobe
#BuildRequires:	tetex-format-latex
#BuildRequires:	texlive-latex-psnfss
#BuildRequires:	tetex-tex-babel
BuildRequires:	unixODBC-devel
BuildRequires:	vanessa_adt-devel
BuildRequires:	vanessa_logger-devel >= 0.0.8
BuildRequires:	vanessa_socket-devel >= 0.0.10
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Requires:	vanessa_adt >= 0.0.4
Requires:	vanessa_logger >= 0.0.8
Requires:	vanessa_socket >= 0.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		schemadir	/usr/share/openldap/schema

%description
Perdition allows users to connect to a content-free POP3 or IMAP4
server that will redirect them to their real POP3 or IMAP4 server.
This enables mail retrieval for a domain to be split across multiple
backend servers on a per user basis. This can also be used to as a
POP3 or IMAP4 proxy especially in firewall applications. Perdition
supports arbitrary library based map access to determine the server
for a user. POSIX Regular Expression, GDBM and MySQL libraries ship
with the distribution.

%description -l pl.UTF-8
Perdition pozwala użytkownikom łączyć się z nie zawierającym nic
serwerem POP3 lub IMAP4, który przekierowuje ich do prawdziwego
serwera POP3 lub IMAP4. Pozwala to na ściąganie poczty dla domen
rozbitych na wiele serwerów na podstawie nazwy użytkownika. Może być
także używane jako proxy POP3 lub IMAP4 na firewallach. Perdition
pozwala użyć dowolnej biblioteki do przypisywania serwerów
użytkownikom. W dystrybucji są biblioteki do wyrażeń regularnych
zgodnych z POSIX oraz baz GDBM i MySQL.

%package bdb
Summary:	BerkeleyDB database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy BerkeleyDB dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description bdb
BerkeleyDB database library for perdition.

%description bdb -l pl.UTF-8
Biblioteka obsługująca bazy BerkeleyDB dla perdition.

%package gdbm
Summary:	GDBM database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy GDBM dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
GDBM database library for perdition.

%description gdbm -l pl.UTF-8
Biblioteka obsługująca bazy GDBM dla perdition.

%package ldap
Summary:	LDAP database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy LDAP dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ldap
LDAP database library for perdition.

%description ldap -l pl.UTF-8
Biblioteka obsługująca bazy LDAP dla perdition.

%package mysql
Summary:	MySQL database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy MySQL dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL database library for perdition.

%description mysql -l pl.UTF-8
Biblioteka obsługująca bazy MySQL dla perdition.

%package nis
Summary:	NIS database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy NIS dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description nis
NIS database library for perdition.

%description nis -l pl.UTF-8
Biblioteka obsługująca bazy NIS dla perdition.

%package odbc
Summary:	ODBC database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy ODBC dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description odbc
ODBC database library for perdition.

%description odbc -l pl.UTF-8
Biblioteka obsługująca bazy ODBC dla perdition.

%package postgresql
Summary:	PostgreSQL database library for perdition
Summary(pl.UTF-8):	Biblioteka obsługująca bazy PostgreSQL dla perdition
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description postgresql
PostgreSQL database library for perdition.

%description postgresql -l pl.UTF-8
Biblioteka obsługująca bazy PostgreSQL dla perdition.

%package -n openldap-schema-perdition
Summary:	Perdition LDAP schema
Summary(pl.UTF-8):	Schemat LDAP dla perdition
Group:		Networking/Daemons
Requires:	openldap-servers

%description -n openldap-schema-perdition
This package contains LDAP schema for use with perdition.

%description -n openldap-schema-perdition -l pl.UTF-8
Ten pakiet zawiera schemat LDAP do używania z perdition.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ldap-schema-directory=%{schemadir}

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
/sbin/chkconfig --add %{name}
%{__make} -q -C /etc/perdition
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
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
%attr(755,root,root) %{_sbindir}/perdition
%attr(755,root,root) %{_sbindir}/perdition.*
%attr(755,root,root) %{_libdir}/libperditiondb_posix_regex.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_posix_regex.so.0

%dir %{_sysconfdir}/perdition
%{_sysconfdir}/perdition/Makefile
%{_sysconfdir}/perdition/Makefile.popmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/perdition/popmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/perdition/popmap.re
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/perdition/perdition.conf
%attr(754,root,root) /etc/rc.d/init.d/perdition
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/perdition
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/perdition

%{_mandir}/man5/perditiondb.5*
%{_mandir}/man8/perdition.8*
%{_mandir}/man8/perdition.*.8*

%files bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makebdb
%attr(755,root,root) %{_libdir}/libperditiondb_bdb.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_bdb.so.0
%{_mandir}/man1/makebdb.1*

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makegdbm
%attr(755,root,root) %{_libdir}/libperditiondb_gdbm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_gdbm.so.0
%{_mandir}/man1/makegdbm.1*

%files ldap
%defattr(644,root,root,755)
# %%doc perdition/db/ldap/doc/perdition_ldap.pdf
%attr(755,root,root) %{_sbindir}/perditiondb_ldap_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_ldap.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_ldap.so.0
%{_mandir}/man8/perditiondb_ldap_makedb.8*

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/perditiondb_mysql_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_mysql.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_mysql.so.0
%{_mandir}/man8/perditiondb_mysql_makedb.8*

%files nis
%defattr(644,root,root,755)
%doc perdition/db/nis/README.perditiondb_nis
%attr(755,root,root) %{_libdir}/libperditiondb_nis.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_nis.so.0

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/perditiondb_odbc_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_odbc.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_odbc.so.0
%{_mandir}/man8/perditiondb_odbc_makedb.8*

%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/perditiondb_postgresql_makedb
%attr(755,root,root) %{_libdir}/libperditiondb_postgresql.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libperditiondb_postgresql.so.0
%{_mandir}/man8/perditiondb_postgresql_makedb.8*

%files -n openldap-schema-perdition
%defattr(644,root,root,755)
%{schemadir}/perdition.schema
