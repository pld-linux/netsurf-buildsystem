Summary:	Netsurf browser buildsystem
Summary(pl.UTF-8):	Pliki do budowania bibliotek związanych z netsurf
Name:		netsurf-buildsystem
Version:	1.0
Release:	2
License:	MIT
Group:		Development/Building
Source0:	http://download.netsurf-browser.org/libs/releases/buildsystem-%{version}.tar.gz
# Source0-md5:	88f2fd584b1608c78133563f452b79ec
URL:		http://www.netsurf-browser.org/
BuildRequires:	tar >= 1:1.22
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netsurf shared buildsystem.

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
%doc README
%{_datadir}/%{name}
