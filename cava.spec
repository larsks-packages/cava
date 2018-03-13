Name:           cava
Version:        0.6.0
Release:        8%{?dist}
Summary:        Console-based Audio Visualizer for Alsa

License:        MIT
URL:            https://github.com/karlstav/cava
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  iniparser-devel

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%setup -q
./autogen.sh


%build
%configure
make %{?_smp_mflags} cava_LDFLAGS=


%install
%make_install
rm -f %{buildroot}%{_libdir}/libiniparser.{a,la,so}

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
%{_datadir}/consolefonts

%changelog
* Mon Mar 12 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-8
- fixes from review (rhbz#1553999): remove defattr
- correct typo in URL
- stop mixing spaces and tabs

* Sat Mar 10 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-5
- fixes from review (rhbz#1553999): remove bundled iniparser

* Sat Mar 10 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-3
- rpmlint fixes

* Fri Mar 09 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-2
- initial package
