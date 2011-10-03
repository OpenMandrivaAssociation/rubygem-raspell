# Generated from raspell-1.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	raspell

Summary:	An interface binding for the Aspell spelling checker
Name:		rubygem-%{rbname}

Version:	1.2.2
Release:	1
Group:		Development/Ruby
License:	GPLv2+
URL:		http://blog.evanweaver.com/files/doc/fauna/raspell/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Requires:	aspell
BuildRequires:	aspell-devel
BuildRequires:	rubygems >= 1.2
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)

%description
An interface binding for the Aspell spelling checker.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_sitearchdir}/raspell.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
