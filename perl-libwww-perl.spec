%define modname	libwww-perl
%define modver 6.06

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Authen::NTLM\\)|perl\\(HTTP::GHTTP\\)'
%else
%define _requires_exceptions Authen::NTLM\\|HTTP::GHTTP\\|Win32
%endif

Summary:	The World-Wide Web library for Perl

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode) >= 2.120.0
BuildRequires:	perl(Encode::Locale)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Listing) >= 6.0.0
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::HeadParser)
BuildRequires:	perl(HTTP::Cookies) >= 6.0.0
BuildRequires:	perl(HTTP::Daemon) >= 6.0.0
BuildRequires:	perl(HTTP::Date) >= 6.0.0
BuildRequires:	perl(HTTP::Negotiate) >= 6.0.0
BuildRequires:	perl(HTTP::Request) >= 6.0.0
BuildRequires:	perl(HTTP::Request::Common) >= 6.0.0
BuildRequires:	perl(HTTP::Response) >= 6.0.0
BuildRequires:	perl(HTTP::Status) >= 6.0.0
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(LWP::MediaTypes) >= 6.0.0
BuildRequires:	perl(MIME::Base64) >= 2.100.0
BuildRequires:	perl(Net::FTP) >= 2.580.0
BuildRequires:	perl(Net::HTTP) >= 6.0.0
BuildRequires:	perl(URI) >= 1.100.0
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(WWW::RobotRules) >= 6.0.0
BuildRequires:	perl-devel
Requires:	perl(Net::HTTP)
Requires:	perl(HTTP::Cookies)

%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface (API) to the World-Wide Web. The
main focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%prep
%setup -qn %{modname}-%{modver}

%build
/usr/bin/yes | %__perl Makefile.PL --aliases INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc README README.SSL Changes
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*



