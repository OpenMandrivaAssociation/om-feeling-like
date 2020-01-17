Summary: Desktop preset selection tool
Name: om-feeling-like
Version: 0.1
Release: 1
Url: http://openmandriva.org/
Source0: https://github.com/OpenMandrivaSoftware/om-feeling-like/archive/%{version}/%{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: cmake ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
Requires: qt5-qttools-qtdbus
Requires: distro-plasma-config

%description
Desktop preset selection tool

%{name} makes life easier for people switching from another
operating system by customizing the OpenMandriva desktop to
behave mpre like what they're expecting.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/om-feeling-like
%{_bindir}/om-feeling-like-ui
%{_datadir}/applications/om-feeling-like.desktop
%{_datadir}/om-feeling-like
%{_datadir}/icons/*/*/*/*
