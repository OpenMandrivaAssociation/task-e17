Name:		task-e17
Version:	%distro_release
Release:	2
Summary:	Metapackage for the E17
Group:		Graphical desktop/Enlightenment
License:	GPL
URL:		http://www.rosalinux.com
BuildArch:	noarch
Requires:	%{name}-minimal
Requires:	editje
Requires:	edje_viewer
Requires:	emprint
Requires:	enki
Requires:	enlil
Requires:	exalt
Requires:	eweather
Requires:	e_modules
Requires:	ephoto
Requires:	enjoy
Requires:	python-ecore
Requires:	python-e_dbus
Requires:	python-edje
Requires:	python-egenix-mx-base
Requires:	python-elementary
Requires:	python-emotion
Requires:	python-ethumb
Requires:	python-evas
# Some stuff we don't have yet
Suggests:	eve
# prefered apps
Suggests:	lxdm

%description
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies. It also install some suggests

%package minimal
Summary:	Metapackage minimal for the E17
Group:		Graphical desktop/Enlightenment
License:	GPL
Provides:	E17
Requires:	eet
Requires:	evas
Requires:	ecore
Requires:	embryo
Requires:	edje
Requires:	efreet
Requires:	e_dbus
Requires:	eeze
Requires:	expedite
Requires:	evas_generic_loaders
Requires:	emotion
Requires:	ethumb
Requires:	elementary
Requires:	e
Requires:	terminology

%description minimal
This package is a meta-package, meaning that its purpose is to contain
all E17 application and librairies.

%files

%files minimal

