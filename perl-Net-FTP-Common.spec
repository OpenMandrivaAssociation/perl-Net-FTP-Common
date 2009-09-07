%define upstream_name	 Net-FTP-Common
%define upstream_version 7.0.d

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Simplify common usages of Net::FTP 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Net::FTP)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is intended to make the common uses of Net::FTP a one-line,
no-argument affair. In other words, you have 100% programming with
Net::FTP. With Net::FTP::Common you will have 95% configuration and 5%
programming.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc README
%{perl_vendorlib}/Net/FTP
%{perl_vendorlib}/TestConfig.pm
%{_mandir}/*/*
