%global goipath    github.com/ulikunitz/xz
Version: 0.5.4

%global common_description %{expand:
This Go language package supports the reading and writing of xz compressed
streams. It includes also a gxz command for compressing and decompressing data.
The package is completely written in Go and doesn't have any dependency on any C
code.

The package is currently under development. There might be bugs and APIs are not
considered stable. At this time the package cannot compete with the xz tool
regarding compression speed and size. The algorithms there have been developed
over a long time and are highly optimized. However there are a number of
improvements planned and I'm very optimistic about parallel compression and
decompression. Stay tuned!}

%gometa

Name:           %{goname}
Release:        3%{?dist}
Summary:        Pure golang package for reading and writing xz-compressed files
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%build
%gobuildroot
for cmd in cmd/* ; do
  %gobuild -o _bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%goinstall
install -m 0755 -vd        %{buildroot}%{_bindir}
install -m 0755 -vp _bin/* %{buildroot}%{_bindir}/

%check
%gochecks

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%files devel -f devel.file-list

%changelog
* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.4-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.5.4-1
- initial package for Fedora
