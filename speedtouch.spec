Summary:	ALCATEL SpeedTouch USB ADSL modem user-space driver
Summary(pl):	Sterownik przestrzeni u¿ytkownika dla modemów ADSL ALCATEL SpeedTouch na USB
Name:		speedtouch
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/speedtouch/%{name}-%{version}.tar.bz2
# Source0-md5:	fa55748175d14dcf8ebe22577df408b3
URL:		http://speedtouch.sf.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALCATEL SpeedTouch USB ADSL modem user-space driver. This package
contains all the necessary software to use your SpeedTouch USB modem
under Linux. It currently support only PPPoA encapsulation. It
contains also modem_run utility necessary to load modem firmware when
using kernel mode drivers (speedtch and pppoatm).

Note: modem_run needs file with modem firmware from Alcatel (mgmt.o,
alcaudsl.sys or firmware.bin).

%description -l pl
Dzia³aj±cy w przestrzeni u¿ytkownika sterownik dla modemów ADSL
ALCATEL SpeedTouch pod³±czanych przez port USB. Ten pakiet zawiera
ca³e oprogramowanie potrzebne do u¿ywania modemu SpeedTouch USB pod
Linuksem. Aktualnie obs³uguje tylko opakowanie PPPoA. Zawiera tak¿e
narzêdzie modem_run niezbêdne do wczytywania firmware modemu w
przypadku u¿ywania sterowników w przestrzeni j±dra (speedtch i
pppoatm).

Uwaga: modem_run potrzebuje pliku z firmware modemu od Alcatela
(mgmt.o, alcaudsl.sys lub firmware.bin).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-syslog \
	--enable-install=`id -nu`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}

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
%{_mandir}/man1/modem_run.1*
%{_mandir}/man1/pppoa2.1*
%{_mandir}/man1/pppoa3.1*
