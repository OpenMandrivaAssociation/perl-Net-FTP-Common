%define upstream_name	 Net-FTP-Common
%define upstream_version 7.0.d

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simplify common usages of Net::FTP 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Net::FTP)

BuildArch:	noarch

%description
This module is intended to make the common uses of Net::FTP a one-line,
no-argument affair. In other words, you have 100% programming with
Net::FTP. With Net::FTP::Common you will have 95% configuration and 5%
programming.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make} test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Net/FTP
%{perl_vendorlib}/TestConfig.pm
%{_mandir}/*/*

%changelog
* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 7.0.0-1mdv2010.0
+ Revision: 432826
- update to 7.0.d

* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 6.1-5mdv2010.0
+ Revision: 430509
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 6.1-4mdv2009.0
+ Revision: 258011
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 6.1-3mdv2009.0
+ Revision: 246115
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 01 2007 Olivier Thauvin <nanardon@mandriva.org> 6.1-1mdv2008.1
+ Revision: 104290
- disable test, don't work inside bs
- unsynch source
- 6.1


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 6.0-1mdv2007.0
+ Revision: 131680
- 0.6

* Thu Dec 28 2006 Olivier Thauvin <nanardon@mandriva.org> 5.32-1mdv2007.1
+ Revision: 102183
- 5.32
- Import perl-Net-FTP-Common

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 5.31-1mdk
- New release 5.31
- fix directory ownership
- better summary
- better source URL

* Thu Sep 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.2g-1mdk
- new version

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 5.2b-1mdk
- initial Mandriva package

