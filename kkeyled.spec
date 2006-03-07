#
# TODO:
# - BRs
# - Rs
#
Summary:	Displays the status of the keyboard leds
Summary(pl):	Wy�wietla status diod klawiatury.
Name:		kkeyled
Version:	0.8.11
Release:	0.1
License:	GPL
Group:		X11/Applications
URL:		http://www.truesoft.ch/dieter/index.html
Source0:	http://www.truesoft.ch/dieter/kkeyled/software/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A little program wich helps you to watch your display leds for the numlock,
scrollock and the capslock keys.

%description -l pl
Ma�y programik, kt�ry pomaga Ci w obserwowaniu diod klawiatury dla klawiszy numlock,
scrollock i capslock.

%prep
%setup -q -n %{name}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install-strip \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kkeyled
%{_datadir}/*