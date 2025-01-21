#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Cairo
Version  : 1.109
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Cairo-1.109.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Cairo-1.109.tar.gz
Summary  : 'Perl interface to the cairo 2d vector graphics library'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Cairo-license = %{version}-%{release}
Requires: perl-Cairo-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Depends)
BuildRequires : perl(ExtUtils::PkgConfig)
BuildRequires : pkgconfig(cairo)

%description
Cairo
=====
Perl bindings to the cairo graphics library (http://www.cairographics.org).

%package dev
Summary: dev components for the perl-Cairo package.
Group: Development
Provides: perl-Cairo-devel = %{version}-%{release}
Requires: perl-Cairo = %{version}-%{release}

%description dev
dev components for the perl-Cairo package.


%package license
Summary: license components for the perl-Cairo package.
Group: Default

%description license
license components for the perl-Cairo package.


%package perl
Summary: perl components for the perl-Cairo package.
Group: Default
Requires: perl-Cairo = %{version}-%{release}

%description perl
perl components for the perl-Cairo package.


%prep
%setup -q -n Cairo-1.109
cd %{_builddir}/Cairo-1.109

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Cairo
cp %{_builddir}/Cairo-1.109/LICENSE %{buildroot}/usr/share/package-licenses/perl-Cairo/7b22ddaeae3dbf094f36bfd2b4ad23618573f60f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Cairo.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Cairo/7b22ddaeae3dbf094f36bfd2b4ad23618573f60f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
