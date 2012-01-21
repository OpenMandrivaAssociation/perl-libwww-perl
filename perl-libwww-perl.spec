%define	upstream_name	 libwww-perl
%define upstream_version 6.02

%define	_requires_exceptions Authen::NTLM\\|HTTP::GHTTP\\|Win32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 5
Summary:	The World-Wide Web library for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Encode::Locale)
BuildRequires:	perl(File::Listing)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Cookies)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(HTTP::Message)
BuildRequires:	perl(HTTP::Negotiate)
BuildRequires:	perl(LWP::MediaTypes)
BuildRequires:	perl(Net::HTTP)
BuildRequires:	perl(URI)
BuildRequires:	perl(WWW::RobotRules)
Requires:       perl(Net::HTTP)
Requires:       perl(HTTP::Cookies)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface (API) to the World-Wide Web. The
main focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/yes | %{__perl} Makefile.PL --aliases INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.SSL Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/*/*
