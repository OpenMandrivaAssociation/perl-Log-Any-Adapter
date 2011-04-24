%define upstream_name    Log-Any-Adapter
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Log::Any)
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Test::More)
Requires: perl(Log::Any)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'Log-Any-Adapter' distribution implements Log::Any class methods to
specify where logs should be sent. It is a separate distribution so as to
keep 'Log::Any' itself as simple and unchanging as possible.

You do not have to use anything in this distribution explicitly. It will be
auto-loaded when you call one of the methods below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


