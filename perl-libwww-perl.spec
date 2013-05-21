%define upstream_name  libwww-perl
%define upstream_version 6.04

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Authen::NTLM\\)|perl\\(HTTP::GHTTP\\)'
%else
%define _requires_exceptions Authen::NTLM\\|HTTP::GHTTP\\|Win32
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	The World-Wide Web library for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz
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
BuildArch:	noarch

%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface (API) to the World-Wide Web. The
main focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-6mdv2012.0
+ Revision: 765389
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-5
+ Revision: 763905
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.20.0-4
+ Revision: 763086
- rebuild

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.20.0-3
+ Revision: 674559
- add dependency on HTTP::Cookies

* Fri May 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.20.0-2
+ Revision: 669906
- force dependency on Net::HTTP

* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.20.0-1
+ Revision: 667395
- new version

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 5.837.0-2
+ Revision: 656984
- rebuild for updated spec-helper

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 5.837.0-1mdv2011.0
+ Revision: 628784
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 5.836.0-2mdv2011.0
+ Revision: 564759
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.836.0-1mdv2011.0
+ Revision: 552377
- update to 5.836

* Sun Nov 22 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.834.0-1mdv2010.1
+ Revision: 468890
- update to 5.834

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.833.0-1mdv2010.1
+ Revision: 460727
- update to 5.833

* Tue Sep 22 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.832.0-1mdv2010.0
+ Revision: 447133
- update to 5.832

* Sun Aug 16 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.831.0-1mdv2010.0
+ Revision: 416949
- update to 5.831

* Mon Jul 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 5.830.0-1mdv2010.0
+ Revision: 400648
- update to 5.830
- using %%perl_convert_version
- fixed license field

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.829-1mdv2010.0
+ Revision: 393794
- update to new version 5.829

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.828-1mdv2010.0
+ Revision: 389778
- update to new version 5.828

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.827-1mdv2010.0
+ Revision: 387009
- update to new version 5.827

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.826-1mdv2010.0
+ Revision: 371939
- update to new version 5.826

* Tue Feb 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.825-1mdv2009.1
+ Revision: 341230
- update to new version 5.825

* Sun Feb 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.824-1mdv2009.1
+ Revision: 340534
- update to new version 5.824

* Tue Jan 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.823-1mdv2009.1
+ Revision: 328904
- update to new version 5.823

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.822-1mdv2009.1
+ Revision: 311976
- update to new version 5.822

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.821-1mdv2009.1
+ Revision: 307057
- update to new version 5.821

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.820-1mdv2009.1
+ Revision: 300702
- update to new version 5.820

* Wed Oct 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.819-1mdv2009.1
+ Revision: 296393
- update to new version 5.819

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.818-1mdv2009.1
+ Revision: 294665
- update to new version 5.818

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.817-1mdv2009.1
+ Revision: 292945
- update to new version 5.817

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.816-1mdv2009.1
+ Revision: 292194
- update to new version 5.816

* Thu Sep 04 2008 Pascal Terjan <pterjan@mandriva.org> 5.814-2mdv2009.0
+ Revision: 280288
- Add back /usr/bin/{GET,HEAD,POST}

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.814-1mdv2009.0
+ Revision: 270389
- update to new version 5.814

* Wed Jun 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.813-1mdv2009.0
+ Revision: 224893
- update to new version 5.813

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.812-1mdv2009.0
+ Revision: 195103
- new version

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 5.808-2mdv2008.1
+ Revision: 180827
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 5.808-1mdv2008.0
+ Revision: 60112
- new version

* Thu Jul 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 5.806-1mdv2008.0
+ Revision: 55602
- new version


* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-10 09:44:40 (63282)
- rebuild

* Sat Oct 07 2006 Oden Eriksson <oeriksson@mandriva.com>
+ 2006-10-06 07:10:19 (62904)
- Import perl-libwww-perl

* Mon Mar 06 2006 Buchan Milne <bgmilne@mandriva.org> 5.805-2mdk
- Rebuild
- use mkrel

* Mon Dec 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.805-1mdk
- 5.805

* Mon Dec 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.803-1mdk
- New version 5.803

* Fri Dec 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.802-2mdk
- Restore installation of GET, HEAD and POST in /usr/bin

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.802-1mdk
- new version

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.801-1mdk
- new version

* Thu Jun 17 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.800-1mdk
- new version

* Sun Apr 18 2004 Guillaume Rousse <guillomovitch@mandrake.org> 5.79-1mdk
- new version

* Wed Apr 14 2004 Guillaume Rousse <guillomovitch@mandrake.org> 5.78-1mdk
- new version
- let spechelper compute dependency

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.76-3mdk
- own dir
- rebuild

* Mon Dec 01 2003 Stefan van der Eijk <stefan@eijk.nu> 5.76-2mdk
- remove patch0: merged upstream

* Sun Nov 30 2003 Stefan van der Eijk <stefan@eijk.nu> 5.76-1mdk
- 5.76

* Thu Nov 06 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.75-1mdk
- 5.75
- cosmetics

* Wed Nov 05 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 5.69-4mdk
- rebuild for new perl
- disable test

