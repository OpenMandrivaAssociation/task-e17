Name:		task-e17
Version:	2015.0
Release:	2
Summary:	Metapackage for the E17
Group:		Graphical desktop/Enlightenment
License:	GPL
URL:		https://www.rosalinux.com
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
Requires:	python-efl
Requires:	python-egenix-mx-base
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
Requires:	eldbus
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

