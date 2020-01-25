#
# Conditional build:
%bcond_without	tests		# perform "make test"
%bcond_with	tests_i18n	# tests with localization (requires some DateTime::Locale language resources)

%define		pdir	DateTime
Summary:	DateTime - representation of date/time combinations
Summary(pl.UTF-8):	DateTime - reprezentacja kombinacji daty i czasu
Name:		perl-DateTime
Version:	1.51
Release:	2
Epoch:		2
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{version}.tar.gz
# Source0-md5:	714843957118d9d24c4b4c9fc7efe8a5
URL:		http://datetime.perl.org/
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Check >= 0.011
BuildRequires:	perl-CPAN-Meta-Requirements
BuildRequires:	perl-DateTime-Format-Mail >= 0.402
BuildRequires:	perl-DateTime-Format-Strptime >= 1.2000
BuildRequires:	perl-DateTime-Locale >= 1.06
BuildRequires:	perl-DateTime-TimeZone >= 3:2.02
BuildRequires:	perl-Math-Round
BuildRequires:	perl-Params-ValidationCompiler >= 0.26
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Specio >= 0.18
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Warnings >= 0.005
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-namespace-autoclean >= 0.19
%endif
%if %{with tests_i18n} && "%(ls /usr/share/perl5/vendor_perl/auto/share/dist/DateTime-Locale/{de,en-US-POSIX,fr,it}.pl >/dev/null 2>&1 ; echo $?)" != "0"
BuildRequires:	perl-DateTime-Locale(with_locales:de;en-US;fr;it)
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

%if %{with tests} && %{without tests_i18n}
%{__sed} -i -e "/^test_strftime_for_locale( '\(de\|it\)'/d" t/13strftime.t
%{__sed} -i -e "/locale.*'de'/ s/'de'/'en-US'/" t/23storable.t
%{__rm} t/14locale.t t/41cldr-format.t
%endif

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
