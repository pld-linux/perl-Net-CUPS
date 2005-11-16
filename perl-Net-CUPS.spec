#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	CUPS
Summary:	CUPS C API Interface
Name:		perl-%{pdir}-%{pnam}
Version:	0.37
Release:	0.1
License:	same as Perl	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9c77ac7c9cac195130a8a378691c51b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CUPS C API Interface.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Net/CUPS.pm
%{perl_vendorarch}/Net/CUPS/Network.pm
%{perl_vendorarch}/Net/CUPS/PPD.pm
%{perl_vendorarch}/Net/CUPS/Printer.pm
%{perl_vendorarch}/auto/Net/CUPS/Network/Network.bs
%{perl_vendorarch}/auto/Net/CUPS/Network/Network.so
%{perl_vendorarch}/auto/Net/CUPS/PPD/PPD.bs
%{perl_vendorarch}/auto/Net/CUPS/PPD/PPD.so
%{perl_vendorarch}/auto/Net/CUPS/Printer/Printer.bs
%{perl_vendorarch}/auto/Net/CUPS/Printer/Printer.so
%{_mandir}/man3/*
