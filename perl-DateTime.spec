#
# Conditional build:
%bcond_without	tests	# perform "make test"

%define		pdir	DateTime
%include	/usr/lib/rpm/macros.perl
Summary:	DateTime - representation of date/time combinations
Summary(pl.UTF-8):	DateTime - reprezentacja kombinacji daty i czasu
Name:		perl-DateTime
Version:	1.43
Release:	1
Epoch:		2
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{version}.tar.gz
# Source0-md5:	94d9fe0de84c2a473462ec9090f58ca6
URL:		http://datetime.perl.org/
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-DateTime-Format-Mail
BuildRequires:	perl-DateTime-Format-Strptime >= 1.2000
BuildRequires:	perl-DateTime-Locale >= 1.06
BuildRequires:	perl-DateTime-TimeZone >= 3:2.02
BuildRequires:	perl-Math-Round
BuildRequires:	perl-Params-ValidationCompiler >= 0.13
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Specio >= 0.18
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Warnings >= 0.005
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-namespace-autoclean >= 0.19
%endif
Requires:	perl-base >= 1:5.8.7-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime is a class for the representation of date/time combinations,
and is part of the Perl DateTime project. For details on this project
please see <http://datetime.perl.org/>. The DateTime site has a FAQ
which may help answer many "how do I do X?" questions. The FAQ is at
<http://datetime.perl.org/faq.html>.

%description -l pl.UTF-8
DateTime to klasa do reprezentowania kombinacji daty i czasu, będąca
częścią perlowego projektu DateTime. Szczegóły dotyczące tego projektu
można znaleźć pod adresem <http://datetime.perl.org/>. Serwis ten ma
swoje FAQ, gdzie można znaleźć odpowiedzi na wiele pytań - dostępne
pod <http://datetime.perl.org/faq.html>.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for noarch DateTime::* modules
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/{Event,Format}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS Changes TODO leaptab.txt
%dir %{perl_vendorlib}/DateTime/Event
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorarch}/DateTime.pm
%{perl_vendorarch}/DateTime/*.pm
%dir %{perl_vendorarch}/auto/DateTime
%attr(755,root,root) %{perl_vendorarch}/auto/DateTime/DateTime.so
%{_mandir}/man3/DateTime*.3pm*
