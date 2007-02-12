Summary:	ALCATEL SpeedTouch USB ADSL modem user-space driver
Summary(pl.UTF-8):   Sterownik przestrzeni użytkownika dla modemów ADSL ALCATEL SpeedTouch na USB
Name:		speedtouch
Version:	1.3.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/speedtouch/%{name}-%{version}.tar.bz2
# Source0-md5:	0848a120ae0eeab6c8ab378e11dc4fa2
Patch0:		%{name}-do_not_strip_g.patch
URL:		http://speedtouch.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
Requires:	ppp-plugin-pppoatm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALCATEL SpeedTouch USB ADSL modem user-space driver. This package
contains all the necessary software to use your SpeedTouch USB modem
under Linux. It currently support only PPPoA encapsulation. It
contains also modem_run utility necessary to load modem firmware when
using kernel mode drivers (speedtch and pppoatm).

Note: modem_run needs file with modem firmware from Alcatel (mgmt.o,
alcaudsl.sys or firmware.bin).

%description -l pl.UTF-8
Działający w przestrzeni użytkownika sterownik dla modemów ADSL
ALCATEL SpeedTouch podłączanych przez port USB. Ten pakiet zawiera
całe oprogramowanie potrzebne do używania modemu SpeedTouch USB pod
Linuksem. Aktualnie obsługuje tylko opakowanie PPPoA. Zawiera także
narzędzie modem_run niezbędne do wczytywania firmware modemu w
przypadku używania sterowników w przestrzeni jądra (speedtch i
pppoatm).

Uwaga: modem_run potrzebuje pliku z firmware modemu od Alcatela
(mgmt.o, alcaudsl.sys lub firmware.bin).

%prep
%setup -q
%patch0 -p0
sed -i 's/static int verbose/int verbose/' src/modem_run.c

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-syslog \
	--enable-install=`id -nu`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%doc doc-linux/{BUGS,FAQ,HDLC_BUG,pppoax-doc-en.txt,results.txt,howto/SpeedTouch-HOWTO-en.html}
%lang(de) %doc doc-linux/howto/SpeedTouch-HOWTO-de.html
%lang(es) %doc doc-linux/howto/SpeedTouch-HOWTO-es.html
%lang(fr) %doc doc-linux/howto/SpeedTouch-HOWTO-fr.html
%lang(it) %doc doc-linux/howto/SpeedTouch-HOWTO-it.html
%lang(nl) %doc doc-linux/howto/SpeedTouch-HOWTO-nl.html
%attr(755,root,root) %{_sbindir}/modem_run
%attr(755,root,root) %{_sbindir}/pppoa2
%attr(755,root,root) %{_sbindir}/pppoa3
%{_datadir}/speedtouch
%{_mandir}/man8/modem_run.8*
%{_mandir}/man8/pppoa2.8*
%{_mandir}/man8/pppoa3.8*
# don't include speedtouch-{setup,start,stop} and hotplug* in current state,
# they are ugly (only for 2.4.x + user-space, incompatible with rc-scripts
# and not aware of our modutils etc.)
