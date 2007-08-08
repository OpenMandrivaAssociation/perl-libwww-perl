%define	_requires_exceptions Authen::NTLM\\|HTTP::GHTTP\\|Win32

%define	module	libwww-perl

Summary:	Libwww-perl module for perl
Name:		perl-%{module}
Version:	5.808
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{module} module for perl

%prep

%setup -q -n %{module}-%{version}

%build
/usr/bin/yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
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
