Summary:	Netsurf browser buildsystem
Summary(pl.UTF-8):	Pliki do budowania bibliotek związanych z netsurf
Name:		netsurf-buildsystem
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Building
Source0:	buildsystem.tar.xz
# Source0-md5:	4a8d8ff9a51d112742cbfeebaa012007
URL:		http://www.netsurf-browser.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netsurf shared buildsystem.

%prep
%setup -q -n buildsystem

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/netsurf-buildsystem
