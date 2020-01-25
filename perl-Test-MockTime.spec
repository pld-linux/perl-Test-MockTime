#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	MockTime
Summary:	Test::MockTime - Replaces actual time with simulated time
#Summary(pl.UTF-8):	
Name:		perl-Test-MockTime
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de726192bcdd0cef68a07ffdf11d7300
URL:		http://search.cpan.org/dist/Test-MockTime/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was created to enable test suites to test code at specific 
points in time. Specifically it overrides localtime, gmtime and time at
compile time and then relies on the user supplying a mock time via 
set_relative_time, set_absolute_time or set_fixed_time to alter future 
calls to gmtime,time or localtime.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
