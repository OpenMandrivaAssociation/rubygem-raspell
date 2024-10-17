# Generated from raspell-1.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	raspell

Summary:	An interface binding for the Aspell spelling checker
Name:		rubygem-%{rbname}

Version:	1.3
Release:	2
Group:		Development/Ruby
License:	GPLv2+
URL:		https://blog.evanweaver.com/files/doc/fauna/raspell/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		raspell-1.3-format-string-fixes.patch
Requires:	aspell
BuildRequires:	aspell-devel
BuildRequires:	rubygems >= 1.2
BuildRequires:	ruby-devel

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
%patch0 -p1 -b .str_fmt~

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
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3-1
+ Revision: 774512
- README file has been renamed README.rdoc..
- format string fixes (P0)
- new version
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Oct 03 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.2-1
+ Revision: 702535
- new version
- imported package rubygem-raspell


* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2-1
- Initial package
