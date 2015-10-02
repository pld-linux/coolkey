Summary:	CoolKey PKCS #11 module
Summary(pl.UTF-8):	Moduł PKCS #11 CoolKey
Name:		coolkey
Version:	1.1.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://directory.fedoraproject.org/download/coolkey/%{name}-%{version}.tar.gz
# Source0-md5:	815a1811a46bf9b8782107c073149cbe
Patch0:		%{name}-includes.patch
Patch1:		%{name}-pcsc.patch
Patch2:		%{name}-sh.patch
URL:		http://pki.fedoraproject.org/wiki/CoolKey
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
# for obsolete pk11install
#BuildRequires:	nss-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
# dlopened
Requires:	pcsc-lite-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Driver support for the CoolKey and CAC products. 

%description -l pl.UTF-8
Wsparcie sterownika linuksowego dla produktów CoolKey oraz CAC.

%package devel
Summary:	Header files for CoolKey Applet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CoolKey Applet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CoolKey Applet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CoolKey Applet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libckyapplet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libckyapplet.so.1
%attr(755,root,root) %{_libdir}/pkcs11/libcoolkeypk11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libckyapplet.so
%{_includedir}/cky_*.h
%{_pkgconfigdir}/libckyapplet.pc
