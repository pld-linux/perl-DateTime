#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
Summary:	DateTime - representation of date/time combinations
Summary(pl):	DateTime - reprezentacja kombinacji daty i czasu
Name:		perl-DateTime
Version:	0.2901
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	f96816e634700ae3c8bd849f97856861
URL:		http://datetime.perl.org/
%if %{with tests}
BuildRequires:	perl-DateTime-Locale >= 0.21
BuildRequires:	perl-DateTime-TimeZone >= 0.26
BuildRequires:	perl-Params-Validate >= 0.76
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-base >= 1:5.8.7-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime is a class for the representation of date/time combinations,
and is part of the Perl DateTime project. For details on this project
please see <http://datetime.perl.org/>. The DateTime site has a FAQ
which may help answer many "how do I do X?" questions. The FAQ is at
<http://datetime.perl.org/faq.html>.

%description -l pl
DateTime to klasa do reprezentowania kombinacji daty i czasu, bêd±ca
czê¶ci± perlowego projektu DateTime. Szczegó³y dotycz±ce tego projektu
mo¿na znale¼æ pod adresem <http://datetime.perl.org/>. Serwis ten ma
swoje FAQ, gdzie mo¿na znale¼æ odpowiedzi na wiele pytañ - dostêpne
pod <http://datetime.perl.org/faq.html>.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/Format

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README CREDITS TODO leaptab.txt
%{perl_vendorarch}/DateTime*pm
%{perl_vendorarch}/DateTime/*.pm
%{perl_vendorarch}/auto/DateTime/DateTime.bs
%dir %{perl_vendorarch}/auto/DateTime
%{perl_vendorlib}/DateTime/*
%attr(755,root,root) %{perl_vendorarch}/auto/DateTime/DateTime.so
%{_mandir}/man3/*
