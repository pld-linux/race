Summary:	A race game
Summary(pl):	Gra - wy¶cigi samochodowe
Name:		race
Version:	0.7.0
Release:	5
License:	GPL except music
Group:		X11/Applications/Games
Source0:	http://race.sourceforge.net/files/Race-%{version}-2_src.tar.gz
# Source0-md5:	e4442f72506f1c6d4086c7b051fb06e0
Source1:	%{name}.desktop
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-api_fix.patch
URL:		http://race.sourceforge.net/
BuildRequires:	ClanLib-devel >= 0.6.1-4
BuildRequires:	ClanLib-OpenGL-devel >= 0.6.1-4
BuildRequires:	ClanLib-Vorbis-devel >= 0.6.1-4
BuildRequires:	autoconf
BuildRequires:	gcc-c++
Requires:	/bin/sh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Race is a 3d car game. It is playable and has a few tracks but it
still lacks some features.

%description -l de
Race ist ein zweidimensionales Kraftwagen-Spiel. Es ist spielbar und
hat ein paar Trassen, aber ein paar Funktionen fehlen ihm nach.

%description -l pl
Race jest trójwymiarow± gr± samochodow±. Jest ona grywalna i wyposa¿ona
w kilka tras, lecz nadal brakuje jej kilku funkcji.

%prep
%setup -q -n Race-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure \
	--enable-sound

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name}/{data,themes,tracks,cars,resources}} \
	$RPM_BUILD_ROOT%{_desktopdir}

cp %{name} $RPM_BUILD_ROOT%{_libdir}
cat>$RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec %{_libdir}/%{name}
EOF
cp -a data/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/data
cp -a themes/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/themes
cp -a tracks/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/tracks
cp -a cars/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/cars
cp -a resources/* $RPM_BUILD_ROOT%{_datadir}/%{name}/resources
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* COPYING.music
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/race
%{_datadir}/%{name}
%{_desktopdir}/*
