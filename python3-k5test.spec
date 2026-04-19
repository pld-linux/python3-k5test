# NOTE: probably works only with MIT Kerberos (with heimdal kadmin stops asking some questions from tty, not even stdin)
Summary:	Library for testing Python applications in self-contained Kerberos 5 environments
Summary(pl.UTF-8):	Biblioteka do testowania aplikacji Pythona w samodzielnych środowiskach Kerberosa 5
Name:		python3-k5test
Version:	0.10.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/k5test/
Source0:	https://files.pythonhosted.org/packages/source/k/k5test/k5test-%{version}.tar.gz
# Source0-md5:	aba377eee66b0eec007bdea04508e1c1
URL:		https://pypi.org/project/k5test/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:40.6.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# kadmin command
Requires:	krb5-server
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k5test is a library for setting up self-contained Kerberos 5
environments, and running Python unit tests inside those environments.
It is based on the file of the same name found alongside the MIT
Kerberos 5 unit tests.

%description -l pl.UTF-8
k5test to biblioteka do konfigurowania samodzielnych środowisk
Kerberosa 5 i uruchamiania w nich testów jednostkowych Pythona. Jest
oparta na pliku o tej samej nazwie, jaki można znaleźć w testach
jednostkowych Kerberosa 5.

%prep
%setup -q -n k5test-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc K5TEST-LICENSE.txt LICENSE.txt README.md
%{py3_sitescriptdir}/k5test
%{py3_sitescriptdir}/k5test-%{version}-py*.egg-info
