Summary:	Netsurf browser buildsystem
Summary(pl.UTF-8):	Pliki do budowania komponentów przeglądarki Netsurf
Name:		netsurf-buildsystem
Version:	1.2
Release:	1
License:	MIT
Group:		Development/Building
Source0:	http://download.netsurf-browser.org/libs/releases/buildsystem-%{version}.tar.gz
# Source0-md5:	0c77c2b9465044ffd469e5995262aa24
URL:		http://www.netsurf-browser.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netsurf shared buildsystem.

%description -l pl.UTF-8
Pliki systemu budowania komponentów przeglądarki Netsurf.

%prep
%setup -q -n buildsystem-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/%{name}
