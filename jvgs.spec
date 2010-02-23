Summary:	Arty platform game
Summary(pl.UTF-8):	Artystyczna gra platformowa
Name:		jvgs
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/jvgs/jvgs-0.5/%{name}-%{version}-src.tar.gz
# Source0-md5:	fa86846e183173c5074f142c8dfb5f3a
URL:		http://jvgs.sourceforge.net/
BuildRequires:	SDL >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	cmake >= 2.6
BuildRequires:	freetype-devel
BuildRequires:	swig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This game takes place in a world much like ours, which has started
fading away. At a point where nearly everything has gone, a poet finds
himself, alone in a strange world of danger. He starts a journey along
the broken stream of thoughts that's left.

%description -l pl.UTF-8
Akcja gry umieszczona jest w świecie podobnym do naszego, który zaczął
zanikać. W momencie, kiedy prawie wszystko przestało istnieć, poeta
odnalazł siebie, samotnego, w dziwnym świecie pełnym niebezpieczeństw.
Rozpoczyna on podróż poprzez przerwany potok myśli, które porzucił.

%prep
%setup -q -n %{name}-%{version}-src

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -a src/jvgs $RPM_BUILD_ROOT%{_bindir}/jvgs-run
cp -a main.lua $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a resources $RPM_BUILD_ROOT%{_datadir}/%{name}
cat > $RPM_BUILD_ROOT%{_bindir}/jvgs << EOF
#!/bin/sh

cd /usr/share/jvgs
/usr/bin/jvgs-run
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.markdown
%attr(755,root,root) %{_bindir}/jvgs*
%{_datadir}/%{name}
