Summary:	Mail Retrieval Proxy
Summary(pl):	Proxy do ¶ci±gania poczty
Name:		perdition
Version:	0.1.9
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.vergenet.net/pub/perdition/%{name}-%{version}.tar.gz
URL:		http://vergenet.net/linux/perdition/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	vanessa_adt-devel
BuildRequires:	vanessa_logger-devel
BuildRequires:	vanessa_socket-devel
Prereq:		/sbin/chkconfig
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

%description -l pl
Perdition pozwala u¿ytkownikom ³±czyæ siê z nie zawieraj±cym nic
serwerem POP3 lub IMAP4, który przekierowuje ich do prawdziwego
serwera POP3 lub IMAP4. Pozwala to na ¶ci±ganie poczty dla domen
rozbitych na wiele serwerów na podstawie nazwy u¿ytkownika. Mo¿e byæ
tak¿e u¿ywane jako proxy POP3 lub IMAP4 na firewallach. Perdition
pozwala u¿yæ dowolnej biblioteki do przypisywania serwerów
u¿ytkownikom. W dystrybucji s± biblioteki do wyra¿eñ regularnych
zgodnych z POSIX oraz baz GDBM i MySQL.

%package devel
Summary:	Headers for perditiondb library development
Summary(pl):	Pliki nag³ówkowe do bibliotek permitiondb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
libraries that may be useful in the development of perditiondb
libraries.

%description devel -l pl
Perdition pozwala na u¿ycie dowolnych bibliotek dostêpu poprzez
biblioteki dzielone w stylu glibcowych NSS. Ten pakiet dostarcza
biblioteki przydatne do robienia bibliotek permitiondb.

%package static
Summary:	Static libraries for perditiondb library development
Summary(pl):	Biblioteki statyczne do bibliotek permitiondb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
static libraries that may be useful in the development of perditiondb
libraries.

%description static -l pl
Perdition pozwala na u¿ycie dowolnych bibliotek dostêpu poprzez
biblioteki dzielone w stylu glibcowych NSS. Ten pakiet dostarcza
biblioteki statyczne przydatne do robienia bibliotek permitiondb.



%prep
%setup -q

%build
sed -e s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{,etc/{,rc.d/init.d,perdition,pam.d,sysconfig}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install etc/rc.d/init.d/perdition.rh $RPM_BUILD_ROOT/etc/rc.d/init.d/perdition
install etc/sysconfig/perdition $RPM_BUILD_ROOT/etc/sysconfig/perdition

ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.0
ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.1

gzip -9nf README AUTHORS ChangeLog NEWS CODING_LOCATIONS TODO

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
f [ "$1" = "0" ]; then
	/sbin/chkconfig --del perdition
	/etc/rc.d/init.d/perdition stop
fi

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/makegdbm
%attr(755,root,root) %{_bindir}/perditiondb_ldap_makedb
%attr(755,root,root) %{_bindir}/perditiondb_mysql_makedb
%attr(755,root,root) %{_bindir}/perditiondb_postgresql_makedb
%attr(755,root,root) %{_sbindir}/perdition*
%attr(755,root,root) %{_libdir}/libjain.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_gdbm.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_ldap.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_mysql.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_nis.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_posix_regex.so.*.*
%attr(755,root,root) %{_libdir}/libperditiondb_postgresql.so.*.*

%dir %{_sysconfdir}/perdition
%{_sysconfdir}/perdition/Makefile
%config %{_sysconfdir}/perdition/popmap
%config %{_sysconfdir}/perdition/popmap.re
%config %{_sysconfdir}/perdition/perdition.conf
%attr(754,root,root) /etc/rc.d/init.d/perdition
%config(noreplace) %verify(not mtime, size, md5) /etc/pam.d/perdition
%config(noreplace) %verify(not mtime, size, md5) /etc/sysconfig/perdition

%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.0
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
