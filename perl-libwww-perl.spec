%define	_requires_exceptions Authen::NTLM\\|HTTP::GHTTP\\|Win32

%define	module	libwww-perl

Summary:	The World-Wide Web library for Perl
Name:		perl-%{module}
Version:	5.818
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface (API) to the World-Wide Web. The
main focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%prep

%setup -q -n %{module}-%{version}

%build
/usr/bin/yes | %{__perl} Makefile.PL --aliases INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.SSL Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*
