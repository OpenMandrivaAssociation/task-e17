Name:    task-e17
Version: 2009.0
Release: %mkrel 1
Summary: Metapackage for the E17
Group:   Graphical desktop/Enlightenment
License: GPL
URL:	 http://wiki.mandriva.com/en/Development/Ideas/E17
Source : %name.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root

Provides: E17

# prefered apps
suggests: thunar
suggests: exaile
suggests: file-roller
Requires: mozilla-firefox
Requires: evince
Requires: lftp
Requires: brasero
Requires: itask
suggests: gimp
Requires: screen
#Requires: xchat
Requires: xterm
#Requires: pidgin
Requires: aumix
Requires: gtk-chtheme
#Requires: terminal
#Requires: Eterm
Requires: mrxvt

# E17 apps
Requires: e
Requires: eet
#Requires: e_utils
#Requires: enity
Requires: edje
Requires: imlib2
Requires: emotion
Requires: epsilon
Requires: etk
Requires: efreet
Requires: ewl
Requires: epeg
Requires: ecore
Requires: edb
Requires: eet
Requires: embryo
#Requires: ephoto
#Requires: exhibit
#Requires: engrave
Requires: entrance
#Requires: estickies
#Requires: empower
#Requires: edje_viewer
Requires: e_modules
Requires: esmart
#Requires: e_dbus
#Requires: evfs
#Requires: expedite
#Requires: extrackt
#Requires: emphasis
#Requires: eclair

%description
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies.

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{_prefix}/share/%name/doc/
cp README ${RPM_BUILD_ROOT}/%{_prefix}/share/%name/doc/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/share/%name/doc/README
