Summary:	A race game
Name:		race
Version:	0.2.0
Release:	1
License:	GPL
Group:		Games
Group(pl):	Gry
Group(de):	Spiele
URL:		http://gamma.nic.fi/~race/
Source0:	http://gamma.nic.fi/~%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	ClanLib-devel
BuildRequires:	gcc-c++
Requires:	/bin/sh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Race is a 2d car game. It is playable and has a few tracks but it
still lacks some features.

%description -l de
Race ist ein zweidimensionales Kraftwagen-Spiel. Es ist spielbar und
hat ein paar Trassen, aber ein paar Funktionen fehlen ihm nach.

%description -l pl
Race jest dwuwymiarow± gr± samochodow±. Jest ona grywalna i wyposa¿ona
w kilka tras, lecz nadal brakuje jej kilku funkcji.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name},\
%{_applnkdir}/Games}
cp race $RPM_BUILD_ROOT%{_libdir}
cat>$RPM_BUILD_ROOT%{_bindir}/race<<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec %{_libdir}/%{name}
EOF
cp -a race.{dat,scr} track_list.lst tracks $RPM_BUILD_ROOT%{_datadir}/race
cp %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
gzip -9nf CREDITS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/%{name}
%{_applnkdir}/*/*
%doc *.gz
