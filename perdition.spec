Summary:	Mail Retrieval Proxy
Summary(pl):	Proxy do ∂ci±gania poczty
Name:		perdition
Version:	0.1.5
Release:	5
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.vergenet.net/pub/perdition/%{name}-%{version}.tar.gz
URL:		http://vergenet.net/linux/perdition/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/chkconfig

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
Perdition pozwala uøytkownikom ≥±czyÊ siÍ z nie zawieraj±cym nic
serwerem POP3 lub IMAP4, ktÛry przekierowuje ich do prawdziwego
serwera POP3 lub IMAP4. Pozwala to na ∂ci±ganie poczty dla domen
rozbitych na wiele serwerÛw na podstawie nazwy uøytkownika. Moøe byÊ
takøe uøywane jako proxy POP3 lub IMAP4 na firewallach. Perdition
pozwala uøyÊ dowolnej biblioteki do przypisywania serwerÛw
uøytkownikom. W dystrybucji s± biblioteki do wyraøeÒ regularnych
zgodnych z POSIX oraz baz GDBM i MySQL.

%package devel
Summary:	Headers for perditiondb library development
Summary(pl):	Pliki nag≥Ûwkowe do bibliotek permitiondb
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}-%{release}

%description devel
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
libraries that may be useful in the development of
perditiondb libraries.

%description devel -l pl
Perdition pozwala na uøycie dowolnych bibliotek dostÍpu poprzez
biblioteki dzielone w stylu glibcowych NSS. Ten pakiet dostarcza
biblioteki przydatne do robienia bibliotek permitiondb.

%package static
Summary:	Static libraries for perditiondb library development
Summary(pl):	Biblioteki statyczne do bibliotek permitiondb
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}-%{release}

%description static
Perdition allows for arbitrary user database access through shared
libraries much in the maner of NSS in glibc. This package provides
static libraries that may be useful in the development of
perditiondb libraries.

%description static -l pl
Perdition pozwala na uøycie dowolnych bibliotek dostÍpu poprzez
biblioteki dzielone w stylu glibcowych NSS. Ten pakiet dostarcza
biblioteki statyczne przydatne do robienia bibliotek permitiondb.

%package libtcp_socket
Summary:	Library to implement simple TCP client/server connections
Summary(pl):	Biblioteka do implementacji prostych po≥±czeÒ TCP klient/serwer
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
License:	LGPL
Provides:	%{name}-libtcp_socket = %{version}-%{release}

%description libtcp_socket
Library that allows fast imlementation of TCP client/server
connections. The library provides calls to set up and listen on a
port, connect to a port and transfer data between a listening server
port and a connected client port.

%description libtcp_socket -l pl
Biblioteka pozwalaj±ca na szybk± implementacjÍ po≥±czeÒ TCP
klient/serwer. Dostarcza funkcje do rozpoczÍcia s≥uchania na porcie,
po≥±czenia z portem i do przesy≥ania danych pomiÍdzy s≥uchaj±cym
serwerem a po≥±czonym klientem.

%package libtcp_socket-devel
Summary:	Headers required to compile against libtcp_socket
Summary(pl):	Pliki nag≥Ûwkowe do kompilacji programÛw uøywaj±cych libtcp_socket
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
License:	LGPL
Requires:	%{name}-libtcp_socket = %{version}-%{release}

%description libtcp_socket-devel
Headers required when writing programmes that use libtcp_socket.

%description libtcp_socket-devel -l pl
Pliki nag≥Ûwkowe potrzebne do tworzenia programÛw uøywaj±cych
biblioteki libtcp_socket.

%package libtcp_socket-static
Summary:	Static libtcp_socket library
Summary(pl):	Biblioteka statyczna libtcp_socket
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
License:	LGPL
Requires:	%{name}-libtcp_socket-devel = %{version}-%{release}

%description libtcp_socket-static
Static version of libtcp_socket library.

%description libtcp_socket-static -l pl
Statyczna wersja biblioteki libtcp_socket.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
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

ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.0
ln -sf perdition $RPM_BUILD_ROOT%{_sbindir}/perdition.1

gzip -9nf README README.perditiondb AUTHORS ChangeLog NEWS CODING_LOCATIONS TODO

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

%post   libtcp_socket -p /sbin/ldconfig
%postun libtcp_socket -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {README,README.perditiondb,AUTHORS,ChangeLog,NEWS,CODING_LOCATIONS,TODO}.gz
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
%config(noreplace) %verify(not mtime, size, md5) /etc/pam.d/perdition
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files libtcp_socket
%defattr(644,root,root,755)
%doc AUTHORS.gz
%attr(755,root,root) %{_libdir}/libtcp_socket.so.*.*

%files libtcp_socket-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtcp_socket.la
%{_includedir}/tcp_socket.h

%files libtcp_socket-static
%defattr(644,root,root,755)
%{_libdir}/libtcp_socket.a
