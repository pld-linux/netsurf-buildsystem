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
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netsurf shared buildsystem.

%prep
%setup -q -n buildsystem

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/%{name}
