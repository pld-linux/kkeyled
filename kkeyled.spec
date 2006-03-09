#
# TODO:
# - fix files
#
Summary:	Displays the status of the keyboard leds
Summary(pl):	Wy¶wietlanie statusu diod klawiatury
Name:		kkeyled
Version:	0.8.11
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.truesoft.ch/dieter/kkeyled/software/%{name}-%{version}.tar.gz
# Source0-md5:	c34c80c8865a0aa5a9525ed7ee0da4a2
URL:		http://www.truesoft.ch/dieter/index.html
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A little program wich helps you to watch your display leds for the
numlock, scrollock and the capslock keys.

%description -l pl
Ma³y programik, który pomaga w obserwowaniu diod klawiatury dla
klawiszy numlock, scrollock i capslock.

%prep
%setup -q -n %{name}

%build
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kkeyled
%{_datadir}/*
