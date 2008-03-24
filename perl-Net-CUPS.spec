#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	CUPS
Summary:	CUPS C API Interface
Summary(pl.UTF-8):	Interfejs do API C CUPS-a
Name:		perl-Net-CUPS
Version:	0.37
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9c77ac7c9cac195130a8a378691c51b
URL:		http://search.cpan.org/dist/Net-CUPS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CUPS C API Interface.

%description -l pl.UTF-8
Interfejs do API C CUPS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%dir %{perl_vendorarch}/Net/CUPS
%{perl_vendorarch}/Net/CUPS/Network.pm
%{perl_vendorarch}/Net/CUPS/PPD.pm
%{perl_vendorarch}/Net/CUPS/Printer.pm
%dir %{perl_vendorarch}/auto/Net/CUPS
%dir %{perl_vendorarch}/auto/Net/CUPS/Network
%{perl_vendorarch}/auto/Net/CUPS/Network/Network.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/CUPS/Network/Network.so
%dir %{perl_vendorarch}/auto/Net/CUPS/PPD
%{perl_vendorarch}/auto/Net/CUPS/PPD/PPD.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/CUPS/PPD/PPD.so
%dir %{perl_vendorarch}/auto/Net/CUPS/Printer
%{perl_vendorarch}/auto/Net/CUPS/Printer/Printer.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/CUPS/Printer/Printer.so
%{_mandir}/man3/*
