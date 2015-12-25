#
# Conditional build:
%bcond_without	tests	# perform "make test"

%define		pdir	DateTime
%include	/usr/lib/rpm/macros.perl
Summary:	DateTime - representation of date/time combinations
Summary(pl.UTF-8):	DateTime - reprezentacja kombinacji daty i czasu
Name:		perl-DateTime
Version:	1.18
Release:	4
Epoch:		2
License:	Artistic 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{version}.tar.gz
# Source0-md5:	58160bea9744a7bc9d7737f7dad9fa72
URL:		http://datetime.perl.org/
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Time::Local) >= 1.04
BuildRequires:	perl-DateTime-Format-Strptime >= 1.2000
BuildRequires:	perl-DateTime-Locale >= 0.41
BuildRequires:	perl-DateTime-TimeZone >= 3:1.74
BuildRequires:	perl-Math-Round
BuildRequires:	perl-Params-Validate >= 0.76
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple >= 0.88
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
%{__perl} Build.PL \
	installdirs=vendor \
	--config cc="%{__cc}" \
	--config ld="%{__cc}" \
	--config optimize="%{rpmcflags}"

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/DateTime/DateTime.bs

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
%{perl_vendorarch}/DateTimePP.pm
%{perl_vendorarch}/DateTimePPExtra.pm
%{perl_vendorarch}/DateTime/*.pm
%dir %{perl_vendorarch}/auto/DateTime
%attr(755,root,root) %{perl_vendorarch}/auto/DateTime/DateTime.so
%{_mandir}/man3/DateTime*.3pm*
