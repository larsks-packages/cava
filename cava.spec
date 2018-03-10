Name:		cava
Version:	0.6.0
Release:	2%{?dist}
Summary:	Console-based Audio Visualizer for Alsa

License:	MIT
URL:		https://github.com/karlstav/cava
Source0:	https://github.com/karlstav/%{name}/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz

BuildRequires:	alsa-lib-devel
BuildRequires:	fftw-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%setup -q
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
%make_install
rm -f %{buildroot}%{_libdir}/libiniparser.{a,la,so}



%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
%{_libdir}/libiniparser.so.4*
/usr/share/consolefonts/cava.psf

%changelog
* Fri Mar 09 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-2
- initial package
