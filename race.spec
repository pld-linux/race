Summary:	A race game
Summary(pl):	Gra - wy¶cigi samochodowe
Name:		race
Version:	0.7.0
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	http://race.sourceforge.net/files/Race-%{version}-2_src.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-cflags.patch
URL:		http://race.sourceforge.net/
BuildRequires:	ClanLib-devel >= 0.6.1-4
BuildRequires:	autoconf
BuildRequires:	gcc-c++
Requires:	/bin/sh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%build
autoconf
%configure \
	--enable-sound 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Games

cp race $RPM_BUILD_ROOT%{_libdir}
cat>$RPM_BUILD_ROOT%{_bindir}/race<<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec %{_libdir}/%{name}
EOF
cp -a race.{dat,scr} track_list.lst tracks $RPM_BUILD_ROOT%{_datadir}/race
cp %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
%{_applnkdir}/*/*
