%define upstream_name    Log-Any-Adapter
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Implements Log::Any class methods to specify where logs should be sent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Any-Adapter-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Guard)
BuildRequires: perl(Devel::GlobalDestruction)
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Log::Any)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Test::More)
Requires:	perl(Log::Any)
Requires:	perl(Scope::Guard)
BuildArch:	noarch

%description
The 'Log-Any-Adapter' distribution implements Log::Any class methods to
specify where logs should be sent. It is a separate distribution so as to
keep 'Log::Any' itself as simple and unchanging as possible.

You do not have to use anything in this distribution explicitly. It will be
auto-loaded when you call one of the methods below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.30.0-4mdv2011.0
+ Revision: 658196
- more req

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.30.0-3
+ Revision: 658165
- add runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2
+ Revision: 656937
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 624836
- import perl-Log-Any-Adapter


