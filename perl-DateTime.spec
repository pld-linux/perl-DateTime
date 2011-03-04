#
# Conditional build:
%bcond_without	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
Summary:	DateTime - representation of date/time combinations
Summary(pl.UTF-8):	DateTime - reprezentacja kombinacji daty i czasu
Name:		perl-DateTime
Version:	0.66
Release:	1
Epoch:		2
License:	Artistic 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/DROLSKY/%{pdir}-%{version}.tar.gz
# Source0-md5:	9399b5b430da65ac0b9056c0182a805b
URL:		http://datetime.perl.org/
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Time::Local) >= 1.04
BuildRequires:	perl-DateTime-Locale >= 0.41
BuildRequires:	perl-DateTime-TimeZone >= 1:1.09
BuildRequires:	perl-Params-Validate >= 0.76
BuildRequires:	perl-Test-Exception
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

# for noarch DateTime::* modules
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/{Event,Format}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README CREDITS TODO leaptab.txt
%dir %{perl_vendorlib}/DateTime/Event
%dir %{perl_vendorlib}/DateTime/Format
%{perl_vendorarch}/DateTime.pm
%{perl_vendorarch}/DateTimePP.pm
%{perl_vendorarch}/DateTimePPExtra.pm
%{perl_vendorarch}/DateTime/*.pm
%dir %{perl_vendorarch}/auto/DateTime
%{perl_vendorarch}/auto/DateTime/DateTime.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DateTime/DateTime.so
%{_mandir}/man3/DateTime*.3pm*
