%define _buildid .2

Name:           perl-URI-db
Version:        0.15
Release:        1%{?_buildid}%{?dist}
Summary:        Perl module for database URIs
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/URI-db/
Source0:        http://cpan.metacpan.org//authors/id/D/DW/DWHEELER/URI-db-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008001
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::Nested) >= 0.10
Requires:       perl(URI) >= 1.40
Requires:       perl(URI::Nested) >= 0.10
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

This class provides support for database URIs. They're inspired by JDBC URIs
and PostgreSQL URIs, though they're a bit more formal.

%prep
%setup -q -n URI-db-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 01 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 0.15-1
- Adapt for AL/LL
- Add package support URL
- Update spec file
- Import `URI-db-0.15.tar.gz`
- Import spec file

* Fri Jan 10 2014 David E. Wheeler <david.wheeler@iovation.com> 0.12-1
- Update to v0.12.

* Fri Jan 3 2014 David E. Wheeler <david.wheeler@iovation.com> 0.11-1
- Update to v0.11.

* Fri Dec 20 2013 David E. Wheeler <david.wheeler@iovation.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
