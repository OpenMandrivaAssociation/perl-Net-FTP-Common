%define module	Net-FTP-Common
%define name	perl-%{module}
%define version 6.1
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simplify common usages of Net::FTP 
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Net::FTP)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is intended to make the common uses of Net::FTP a one-line,
no-argument affair. In other words, you have 100% programming with
Net::FTP. With Net::FTP::Common you will have 95% configuration and 5%
programming.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%if 0
%check
%{__make} test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Net/FTP
%{perl_vendorlib}/TestConfig.pm
%{_mandir}/*/*


